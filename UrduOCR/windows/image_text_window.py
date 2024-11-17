import os
from PyQt5.Qt import *
from ocr import OCR


class ImageTextWindow(QMainWindow):
    def __init__(self, parent, img):
        super(ImageTextWindow, self).__init__(parent)

        self.title_label = QLabel(self)
        self.output_editText = QTextEdit(self)
        self.back_button = QPushButton(self)
        self.save_button = QPushButton(self)

        file = QFile("temp.png")
        file.open(QIODevice.WriteOnly)
        img.save("temp.png", "PNG")

        result = OCR.convert_to_text("temp.png")
        data = result.split("\n")
        temp = "\n"
        for i in data:
            if len(i)>70:
                temp += "  " + i[:71] + "\n\n\n" + i[71:] + "\n\n"
            else:
                temp += "  " + i + "\n\n"

        self.output_editText.setText(temp)
        os.remove("temp.png")





        self.init_ui()


    def init_ui(self):
        self.setWindowTitle('Urdu OCR')
        self.setFixedSize(1000, 800)

        self.title_label.setGeometry(360, 20, 300, 40)
        self.title_label.setText('Extracted Text')
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignCenter)

        font = QFont()
        font.setFamily("Nafees")
        font.setPointSize(28)

        self.output_editText.setGeometry(30, 90, 950, 600)
        self.output_editText.setFont(font)
        self.output_editText.setLayoutDirection(Qt.RightToLeft)


        self.back_button.setGeometry(50, 720, 120, 40)
        self.back_button.setText('Back')

        self.save_button.setGeometry(750, 720, 120, 40)
        self.save_button.setText('Save Text')

        self.back_button.clicked.connect(self.back_button_click)
        self.save_button.clicked.connect(self.save_button_click)

    def back_button_click(self):
        self.close()
        self.parent().show()

    def save_button_click(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "Text Files (*.txt)", options=options)
        if fileName:
            print(fileName, _)
            text_file = open(fileName, "w")
            text_file.write(self.output_editText.toPlainText())
            text_file.close()

