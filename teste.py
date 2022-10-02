import sys
from PIL import Image
from PyQt5.QtCore import Qt, QObject
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from main import qtAppWidget
from flask import Flask
from flask import request
from flask_restful import Resource, Api, reqparse
import base64

app_server = Flask(__name__)
api = Api(app_server)


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 400)
        self.setAcceptDrops(True)
        main_layout = QVBoxLayout()
        self.photoViewer = qtAppWidget()
        main_layout.addWidget(self.photoViewer)
        self.setLayout(main_layout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.set_image(file_path)

            event.accept()
        else:
            event.ignore()

    def set_image(self, file_path):
        self.photoViewer.setupGUI(QPixmap(file_path))


# class ScreenSharing(Resource):
#
#     def __init__(self):
#         self.photoViewer = None
#
#     def post(self):
#         data = request.args.get('base64', default='*', type=str)
#         print(data)
#         imgdata = base64.b64decode(data)
#         filename = 'picture.jpg'
#         with open(filename, 'wb') as f:
#             f.write(imgdata)
#         img = Image.open('picture.jpg')
#         img.save('C:/Users/luizf/Desktop/imagens/picture.jpg', 'JPEG')
#         self.photoViewer = AppDemo()
#         # self.photoViewer.set_image(file_path='C:/Users/luizf/Desktop/imagens/picture.jpg')
#         return 'done', 200
#
#     pass
#

# api.add_resource(ScreenSharing, '/screen_sharing')
# app_server.run(host='0.0.0.0', port=8089)
app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())
