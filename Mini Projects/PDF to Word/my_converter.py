import os
from pdf2docx import Converter

# Get the directory where this script is saved
base_path = os.path.dirname(__file__)

# Join that path with your filename
input_pdf = os.path.join(base_path, "Invoice.pdf")
output_docx = os.path.join(base_path, "sample.docx")

def pdf_to_word(pdf_file, word_file):
    if not os.path.exists(pdf_file):
        print(f" Error: Could not find '{pdf_file}'")
        print(f"I am looking in: {os.path.abspath(pdf_file)}")
        return

    try:
        cv = Converter(pdf_file)
        cv.convert(word_file)
        cv.close()
        print(f" Success! Saved to {word_file}")
    except Exception as e:
        print(f" Error during conversion: {e}")
pdf_to_word(input_pdf, output_docx)