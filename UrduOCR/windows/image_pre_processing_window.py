import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
import cv2
import imutils
from .crop_image_window import CropImageWindow
from .image_text_window import ImageTextWindow


class ImagePreProcessingWindow(QMainWindow):
    def __init__(self, parent, file_name):
        super(ImagePreProcessingWindow, self).__init__(parent)

        self.title_label = QLabel(self)
        self.image_label = QLabel(self)
        self.image_label.file_name = file_name
        self.cancel_button = QPushButton(self)
        self.continue_button = QPushButton(self)

        self.rotate_image_button = QPushButton(self)
        self.crop_image_button = QPushButton(self)

        self.rotate_degree_textEdit = QTextEdit(self)

        self.cropped = False

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Urdu OCR')
        self.setFixedSize(1000, 800)

        self.title_label.setGeometry(350, 20, 300, 40)
        self.title_label.setText('Edit Image')
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignCenter)

        self.image_label.setGeometry(30, 30, 900, 600)
        self.image_label.setPixmap(QPixmap(self.image_label.file_name))
        self.image_label.setAlignment(Qt.AlignCenter)

        self.cancel_button.setGeometry(50, 700, 120, 40)
        self.cancel_button.setText('Cancel')

        self.continue_button.setGeometry(750, 700, 120, 40)
        self.continue_button.setText('Continue')

        self.rotate_image_button.setGeometry(350, 650, 120, 40)
        self.rotate_image_button.setText('Rotate')

        self.crop_image_button.setGeometry(500, 650, 120, 40)
        self.crop_image_button.setText('Crop')

        self.rotate_degree_textEdit.setGeometry(420, 590, 120, 40)
        self.rotate_degree_textEdit.setAlignment(Qt.AlignCenter)

        self.rotate_image_button.clicked.connect(self.rotate_image_button_click)
        self.crop_image_button.clicked.connect(self.crop_image_button_click)
        self.cancel_button.clicked.connect(self.cancel_button_click)
        self.continue_button.clicked.connect(self.continue_button_click)

    def save_image_button_click(self):
        if self.input_image.pixmap():
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file_name, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                       "Image Files (*.png)", options=options)
            if file_name:
                file = QFile(file_name + ".png")
                file.open(QIODevice.WriteOnly)
                self.input_image.pixmap().save(file, "PNG")

    def continue_button_click(self):
        self.hide()
        self.image_text_window = ImageTextWindow(self, self.image_label.pixmap())
        self.image_text_window.show()

    def cancel_button_click(self):
        self.close()
        self.parent().show()

    def rotate_image_button_click(self):
        rotate_angle = self.rotate_degree_textEdit.toPlainText()

        try:
            rotate_angle = int(rotate_angle)

            transform = QTransform()
            transform.rotate(rotate_angle)

            self.image_label.setPixmap(QPixmap(self.image_label.pixmap().transformed(transform)))
        except ValueError as verr:
            self.rotate_degree_textEdit.setText("")
        except Exception as ex:
            self.rotate_degree_textEdit.setText("")

    def crop_image_button_click(self):
        self.crop_image_window = CropImageWindow(self, self.image_label.pixmap())
        self.crop_image_window.show()
