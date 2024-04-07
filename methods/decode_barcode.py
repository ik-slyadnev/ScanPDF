import fitz  # PyMuPDF
from PIL import Image
import io
import pyzbar.pyzbar as pyzbar


def extract_and_decode_barcodes(pdf_path):
    doc = fitz.open(pdf_path)
    barcodes = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        for img_index, base_image in enumerate(page.get_images(full=True)):
            xref = base_image[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            pil_img = Image.open(io.BytesIO(image_bytes))
            decoded_objects = pyzbar.decode(pil_img)

            for obj in decoded_objects:
                barcodes.append({
                    'type': obj.type,
                    'data': obj.data.decode('utf-8'),
                })

    doc.close()
    return barcodes


pdf_path = '../files/sample_file/test_task.pdf'
barcodes = extract_and_decode_barcodes(pdf_path)
