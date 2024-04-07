from methods.extractor import PDFDataExtractor, data
from data.verification_sn_123123 import sn123123_info


class PDFVerifier(PDFDataExtractor):
    def __init__(self, pdf_path, reference_data):
        super().__init__(pdf_path)
        self.reference_data = reference_data

    def verify_structure(self):
        test_data = self.extract_information()
        discrepancies = []


        for key in self.reference_data.keys():
            if key not in test_data:
                discrepancies.append(f"Missing field: {key}")
            elif test_data[key] != self.reference_data[key]:
                discrepancies.append(
                    f"Mismatch in '{key}': Expected '{self.reference_data[key]}', Found '{test_data[key]}'")


        for key in test_data.keys():
            if key not in self.reference_data:
                discrepancies.append(f"Unexpected field: {key}")

        return discrepancies


reference_data = data

pdf_verifier = PDFVerifier(pdf_path='files/sample_file/test_task.pdf', reference_data=reference_data)
discrepancies = pdf_verifier.verify_structure()

if discrepancies:
    print("\nFlaws found:")
    for discrepancy in discrepancies:
        print(discrepancy)
else:
    print("\nThe structure of the PDF is in line with expectations.")
