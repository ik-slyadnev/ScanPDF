from methods.extractor import PDFDataExtractor
from data.verification_sn_123123 import sn123123_info


def test_extract_information():
    pdf_path = '../files/sample_file/test_task.pdf'
    extractor = PDFDataExtractor(pdf_path)
    data = extractor.extract_information()

    for key, expected_value in sn123123_info.items():
        assert data.get(key) == expected_value, f"Mismatch for {key}: expected {expected_value}, got {data.get(key)}"
