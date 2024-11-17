import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from .image_text_window import ImageTextWindow
from .image_pre_processing_window import ImagePreProcessingWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.title_label = QLabel(self)
        self.image_label = QLabel(self)
        self.image_label.file_name = None
        self.select_button = QPushButton(self)
        self.edit_button = QPushButton(self)
        self.extract_button = QPushButton(self)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Urdu OCR')
        self.setFixedSize(1000, 800)

        self.title_label.setGeometry(350, 20, 300, 40)
        self.title_label.setText('Urdu OCR')
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignCenter)

        self.image_label.setGeometry(30, 30, 900, 600)
        self.image_label.setPixmap(QPixmap('./resources/add_image.png'))
        self.image_label.setAlignment(Qt.AlignCenter)

        self.select_button.setGeometry(200, 600, 600, 40)
        self.select_button.setText('Select Image')

        self.edit_button.setGeometry(70, 700, 120, 40)
        self.edit_button.setText('Edit')

        self.extract_button.setGeometry(800, 700, 120, 40)
        self.extract_button.setText('Extract')

        self.select_button.clicked.connect(self.select_button_click)
        self.edit_button.clicked.connect(self.edit_button_click)
        self.extract_button.clicked.connect(self.extract_button_click)

    def select_button_click(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                   "Image Files (*.png);;Image Files (*.jpg);;Image Files ("
                                                   "*.jpeg);;Image Files (*.bmp)", options=options)
        if file_name:
            pixmap = QPixmap(file_name)
            self.image_label.file_name = file_name
            self.image_label.setText("")
            self.image_label.setPixmap(pixmap)

    def edit_button_click(self):
        if self.image_label.file_name:
            self.hide()
            self.image_pre_processing_window = ImagePreProcessingWindow(self, self.image_label.file_name)
            self.image_pre_processing_window.show()
        else:
            QMessageBox.question(self, 'URDU OCR message', "Select an Image", QMessageBox.Ok)

    def extract_button_click(self):
        if self.image_label.file_name:
            self.hide()
            self.image_text_window = ImageTextWindow(self, self.image_label.pixmap())
            self.image_text_window.show()
        else:
            QMessageBox.question(self, 'URDU OCR message', "Select an Image", QMessageBox.Ok)
