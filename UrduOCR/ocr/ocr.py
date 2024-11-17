import tesserocr
from PIL import Image
import os


class OCR:
    path = os.getcwd() + "/ocr/tessdata"

    @staticmethod
    def convert_to_text(img_path):
        img = Image.open(img_path)
        return tesserocr.image_to_text(img, lang="urd", path=OCR.path, psm=1)
