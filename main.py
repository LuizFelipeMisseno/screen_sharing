from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject, Qt, QThread, QTimer
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QWidget


class qtAppWidget(QLabel):

    def __init__(self):
        super().__init__()
        # Connect the singal to slot
        self.app_widget = None
        self.pixmap = None
        self.screen_height = None
        self.screen_width = None
        self.screens_available = None
        self.screen = None
        self.selected_screen = None
        self.app = None
        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
                            QLabel{
                                border: 4px dashed #aaa
                            }
                        ''')

    def setupGUI(self, image):
        self.app = QApplication.instance()
        self.selected_screen = 1  # Select the desired monitor/screen
        self.screens_available = self.app.screens()
        self.screen = self.screens_available[self.selected_screen]
        self.screen_width = self.screen.size().width()
        self.screen_height = self.screen.size().height()

        # Create a black image for init
        custom_pix_map = QPixmap(image).scaled(self.screen_width, self.screen_height)
        self.pixmap = custom_pix_map
        # Create QLabel object
        self.app_widget = QLabel()

        self.app_widget.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowDoesNotAcceptFocus | Qt.WindowStaysOnTopHint)
        # Hide mouse cursor
        self.app_widget.setCursor(Qt.BlankCursor)

        self.app_widget.setGeometry(0, 0, self.screen_width, self.screen_height)
        self.app_widget.setWindowTitle('myImageDisplayApp')
        self.app_widget.setAlignment(Qt.AlignCenter)
        self.app_widget.setPixmap(self.pixmap)
        self.app_widget.show()

        # Set the screen on which widget is on
        self.app_widget.windowHandle().setScreen(self.screen)
        # Make full screen
        self.app_widget.showFullScreen()

    def update_image(self, pattern_file=None):
        print('Pattern file given: ', pattern_file)
        self.app_widget.clear()  # Clear all existing content of the QLabel
        self.pixmap = QPixmap(pattern_file)  # Update pixmap with desired image
        self.app_widget.setPixmap(self.pixmap)  # Show desired image on Qlabel
