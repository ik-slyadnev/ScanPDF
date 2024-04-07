from methods.extractor import PDFDataExtractor
from methods.decode_barcode import extract_and_decode_barcodes


pdf_path1 = 'files/sample_file/test_task.pdf'
pdf_path2 = 'files/files_to_check/fail_test_task.pdf'


extractor1 = PDFDataExtractor(pdf_path1)
data1 = extractor1.extract_information()
barcodes1 = extract_and_decode_barcodes(pdf_path1)


extractor2 = PDFDataExtractor(pdf_path2)
data2 = extractor2.extract_information()
barcodes2 = extract_and_decode_barcodes(pdf_path2)


def compare_data(data1, data2):
    discrepancies = []
    for key in data1.keys():
        if key not in data2:
            discrepancies.append(f"Missing {key} in second PDF")
        elif data1[key] != data2[key]:
            discrepancies.append(f"Mismatch in '{key}': PDF1='{data1[key]}' vs PDF2='{data2[key]}'")
    return discrepancies


def compare_barcodes(barcodes1, barcodes2):
    if barcodes1 == barcodes2:
        return "Barcodes match."
    else:
        return "Barcodes do not match."


data_discrepancies = compare_data(data1, data2)
if data_discrepancies:
    print("Discrepancies found in data:")
    for discrepancy in data_discrepancies:
        print(discrepancy)
else:
    print("No discrepancies found in data.")

barcode_comparison_result = compare_barcodes(barcodes1, barcodes2)
print(barcode_comparison_result)
