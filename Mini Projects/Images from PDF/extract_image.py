import fitz  # PyMuPDF
import io
from PIL import Image
import os

def extract_images_from_pdf(pdf_path, output_folder="extracted_images"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pdf_file = fitz.open(pdf_path)
    
    image_count = 0

    for page_index in range(len(pdf_file)):
        page = pdf_file[page_index]
        image_list = page.get_images(full=True)

        if image_list:
            print(f"Found {len(image_list)} images on page {page_index + 1}")
        else:
            print(f"No images found on page {page_index + 1}")

        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            
            image = Image.open(io.BytesIO(image_bytes))
            
            image_filename = f"img_pg{page_index+1}_{img_index+1}.{image_ext}"
            image.save(os.path.join(output_folder, image_filename))
            image_count += 1

    pdf_file.close()
    print(f"\ Done! Total images extracted: {image_count}")
    print(f"Check the folder: '{output_folder}'")

if __name__ == "__main__":
    extract_images_from_pdf("sample.pdf")