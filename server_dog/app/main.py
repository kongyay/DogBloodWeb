from flask import Flask, flash, request, redirect, url_for
from flask_mongoengine import MongoEngine
from models import DogData, Record
from flask_cors import CORS
import os
import json
import base64

script_dir = os.path.dirname(__file__)

app = Flask(__name__)
app.config.from_pyfile('prod.cfg')
CORS(app)
db = MongoEngine(app)


@app.route("/")
def hello():
    return 'Hello everyone !'


@app.route("/dog/get")
def dog_get():
    return str(list(map(lambda x: str(x.to_json()), DogData.objects)))


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

            image = read_image(filename)

    return json.dumps({'image': image, 'filename': filename}), 200


@app.route("/dog/resize", methods=['POST'])
def dog_resize():
    if request.method == 'POST':
        data = request.json

    return json.dumps({'image': ''}), 200


@app.route("/dog/confirm", methods=['POST'])
def dog_confirm():
    if request.method == 'POST':
        data = request.json

    return json.dumps([{'class': 'A', 'value': 20}, {'class': 'B', 'value': 50}]), 200


def save_image(filename, b64_string):
    b64_string = ','.join(b64_string.split(',')[1:])  # Cut the header
    with open(os.path.join(script_dir, "user_img/%s" % filename), "wb") as fh:
        fh.write(base64.decodestring(b64_string.encode()))


def read_image(filename):
    with open(os.path.join(script_dir, "user_img/%s" % filename), "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return "data:image/jpeg;base64,"+encoded_string


if __name__ == "__main__":
    app.run(debug=True)
