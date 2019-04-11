import base64


class Predict:
    def __init__(self):
        # Initialize Model
        model_name = 'test4.hdf5'
        self.file = ''

    def upload(self, file='7.jpg'):
        self.file = file
        return self.input_process1()

    def input_process1(self, param1=20, param2=20, distance=15, minR=10, maxR=20):
        with open("data/"+self.file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            return encoded_string

    def process2(self, ratio=4, input_path='D:/RBC Classification Git New system/data', output_path='D:/RBC Classification Git New system/resize'):

        with open("data/"+self.file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            return encoded_string

    def input2_process3(self, param1=15, param2=15, distance=55, minR=50, maxR2=67):

        with open("data/"+self.file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            return encoded_string

    def process4(self):
        return [
            {
                "class": "A",
                "value": 20
            },
            {
                "class": "B",
                "value": 6
            }
        ]

        clean_file('resize')
        clean_file('data')
