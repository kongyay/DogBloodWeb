from flask import Flask, flash, request, redirect, url_for
from flask_mongoengine import MongoEngine
from models import DogData, Record
from flask_cors import CORS
import os
import json
import base64
from application import Predict

script_dir = os.path.dirname(__file__)

app = Flask(__name__)
app.config.from_pyfile('prod.cfg')
CORS(app)
db = MongoEngine(app)
predictor = Predict()


@app.route("/")
def hello():
    return 'Hello everyone !'


@app.route("/dog/get")
def dog_get():
    return str(list(map(lambda x: x.to_json(), DogData.objects))), 200


@app.route("/dog/delete/<int:id>")
def dog_delete(id):
    try:
        dog = DogData.objects.get(dog_id=id)
        records = Record.objects(dog_data=dog)
        data = {
            'dog': dog.to_json(),
            'records': list(map(lambda x: x.to_json(), records))
        }
        records.delete()
        dog.delete()
    except (Exception):
        return json.dumps({'error': 'Not Found!'}), 200
    return str(data), 200


@app.route("/record/get")
def records_get():
    return str(list(map(lambda x: x.to_json(), Record.objects)))


@app.route("/record/find/<int:id>")
def records_find(id):
    try:
        dog = DogData.objects.get(dog_id=id)
        records = Record.objects(dog_data=dog)
        result = list(map(lambda x: x.to_json(), records))
    except (Exception):
        return json.dumps({'error': 'Not Found!'}), 200

    return json.dumps(result), 200


@app.route("/dog/add", methods=['POST'])
def dog_add():
    if request.method == 'POST':
        data = request.json

        if data['image'] is None:
            return json.dumps({'error': 'No valid request body, json missing!'}), 200
        else:
            filename = "%s_%s_%s" % (
                data['ownerName'], data['dogName'], data['imageName'])
            img_data = data['image']

            save_image(filename, img_data)

            image = predictor.upload(file=filename)

            return json.dumps({'image': fix_b64(image), 'filename': filename}), 200

    return "", 500


@app.route("/dog/resize/<int:step>", methods=['POST'])
def dog_resize(step):
    if request.method == 'POST':
        data = request.json
        if step == 1:
            image = predictor.input_process1(param1=data['param1'], param2=data['param2'],
                                             distance=data['distance'], minR=data['minradius'], maxR=data['maxradius'])
        elif step == 2:
            image = predictor.input2_process3(param1=data['param1'], param2=data['param2'],
                                              distance=data['distance'], minR=data['minradius'], maxR=data['maxradius'])

        return json.dumps({'image': fix_b64(image)}), 200

    return "", 500


@app.route("/dog/confirm/<int:step>", methods=['POST'])
def dog_confirm(step):
    if request.method == 'POST':
        data = request.json

        if step == 1:
            image = predictor.process2(input_path=get_path(
                'data'), output_path=get_path('resize'))
            return json.dumps({'image': fix_b64(image)}), 200
        elif step == 2:
            result = predictor.process4()

            try:
                dog = DogData.objects.get(dog_id=data['dogId'])
            except (Exception):
                print("New Dog")
                dog = DogData(owner_name=data['ownerName'],
                              dog_name=data['dogName'],
                              dog_id=data['dogId'])
                dog.save()
            record = Record(dog_data=dog,
                            classify_data=result)
            record.save()

            return json.dumps(result), 200

    return "", 500


def get_path(folder):
    return os.path.abspath(folder)


def save_image(filename, b64_string):
    b64_string = ','.join(b64_string.split(',')[1:])  # Cut the header
    with open("data/%s" % filename, "wb") as fh:
        fh.write(base64.decodestring(b64_string.encode()))


def read_image(filename):
    with open("data/%s" % filename, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return "data:image/jpeg;base64,"+encoded_string


def fix_b64(text):
    text = text.decode().split('\'')
    if len(text) == 1:
        text = text[0]
    else:
        text = text[1]
    return 'data:image/jpeg;base64,' + text


if __name__ == "__main__":
    app.run(debug=True)
