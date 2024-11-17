import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *


class CropImageWindow(QMainWindow):
    def __init__(self, parent, img):
        super(CropImageWindow, self).__init__(parent)

        self.image_label = QLabel(self)
        self.image_label.setPixmap(img)

        self.cancel_button = QPushButton(self)
        self.continue_button = QPushButton(self)

        self.init_ui(img)

    def init_ui(self, img):
        self.setWindowTitle('Urdu OCR')
        self.setFixedSize(1000, 800)

        self.image_label.setGeometry(self.image_label.pixmap().rect())
        self.image_label.setAlignment(Qt.AlignCenter)

        self.cancel_button.setGeometry(50, 700, 120, 40)
        self.cancel_button.setText('Cancel')

        self.continue_button.setGeometry(750, 700, 120, 40)
        self.continue_button.setText('Ok')

        self.cancel_button.clicked.connect(self.cancel_button_click)
        self.continue_button.clicked.connect(self.continue_button_click)

    def mousePressEvent(self, eventQMouseEvent):
        self.originQPoint = eventQMouseEvent.pos()
        self.currentQRubberBand = QRubberBand(QRubberBand.Rectangle, self)
        self.currentQRubberBand.setGeometry(QRect(self.originQPoint, QSize()))
        self.currentQRubberBand.show()

    def mouseMoveEvent(self, eventQMouseEvent):
        self.currentQRubberBand.setGeometry(QRect(self.originQPoint, eventQMouseEvent.pos()).normalized())

    def mouseReleaseEvent(self, eventQMouseEvent):
        self.currentQRubberBand.hide()
        currentQRect = self.currentQRubberBand.geometry()
        self.currentQRubberBand.deleteLater()
        self.cropQPixmap = self.image_label.pixmap().copy(currentQRect)


    def continue_button_click(self):
        self.cropQPixmap = self.cropQPixmap.scaled(500, 500, Qt.KeepAspectRatio)
        self.close()
        self.parent().image_label.setPixmap(self.cropQPixmap)
        self.parent().show()

    def cancel_button_click(self):
        self.close()
        self.parent().show()
