import os
from docx2pdf import convert

def word_to_pdf(input_name):
    base_dir = os.path.dirname(__file__)
    
    word_path = os.path.join(base_dir, input_name)
    
    pdf_name = input_name.replace(".docx", ".pdf")
    pdf_path = os.path.join(base_dir, pdf_name)

    if not os.path.exists(word_path):
        print(f" Error: Cannot find '{input_name}' in this folder.")
        return

    try:
        print(f" Converting '{input_name}'... Please wait.")

        convert(word_path, pdf_path)
        print(f" Success! Your PDF is ready: {pdf_name}")
        
    except Exception as e:
        print(f" An error occurred: {e}")

if __name__ == "__main__":
    word_to_pdf("sample.docx")