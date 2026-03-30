from pdf2image import convert_from_path
from rapidocr import RapidOCR
import os
from PIL import Image

ocr_engine = RapidOCR()

def extract_text_from_pdf(pdf_path):
    pages = convert_from_path(pdf_path, dpi=300)
    full_text = []

    for page in pages:
        temp_path = "temp.jpg"
        page.save(temp_path, "JPEG")

        out = ocr_engine(temp_path)
        texts = out.txts

        if texts:
            full_text.append(" ".join(texts))

        os.remove(temp_path)

    return " ".join(full_text)


def extract_text_from_image(image):
    temp_path = "temp_img.jpg"
    image.save(temp_path)

    out = ocr_engine(temp_path)
    texts = out.txts

    os.remove(temp_path)

    if texts:
        return " ".join(texts)

    return ""