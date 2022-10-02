import sys

from PIL import Image
from PyQt5.QtWidgets import QWidget, QApplication
from flask import Flask
from flask import request
from flask_restful import Resource, Api, reqparse
import base64
from teste import AppDemo

app = Flask(__name__)
api = Api(app)


class ScreenSharing(Resource):

    def post(self):
        data = request.args.get('base64', default='*', type=str)
        print(data)
        # imgdata = base64.b64decode(data)
        # filename = 'picture.jpg'
        # with open(filename, 'wb') as f:
        # f.write(imgdata)
        # img = Image.open('picture.jpg')
        # img.save('C:/Users/luizf/Desktop/imagens/picture.jpg', 'JPEG')
        # self.photoViewer.set_image(file_path='C:/Users/luizf/Desktop/imagens/picture.jpg')
        return 'done', 200

    pass


api.add_resource(ScreenSharing, '/screen_sharing')

app.run(host='0.0.0.0', port=8089)
