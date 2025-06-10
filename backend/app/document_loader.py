# OCR Setup (PDF + Image support)

import pytesseract
from pdf2image import convert_from_path
from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            text += page.extract_text() or ""
    except:
        pass
    return text

def extract_text_from_scanned_pdf(pdf_path):
    text = ""
    try:
        images = convert_from_path(pdf_path)
        for image in images:
            text += pytesseract.image_to_string(image)
    except:
        pass
    return text

def process_document(path):
    extracted_text = extract_text_from_pdf(path)
    if not extracted_text.strip():
        extracted_text = extract_text_from_scanned_pdf(path)
    return extracted_text
