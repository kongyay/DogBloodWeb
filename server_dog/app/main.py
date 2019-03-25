from flask import Flask
from flask_mongoengine import MongoEngine
from models import DogData, Record

app = Flask(__name__)
app.config.from_pyfile('prod.cfg')
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
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return 'OK'


if __name__ == "__main__":
    app.run(debug=True)
