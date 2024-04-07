import fitz
import re


class PDFDataExtractor:

    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extract_information(self):
        with fitz.open(self.pdf_path) as doc:
            text = ""
            for page in doc:
                text += page.get_text()

        data = {
            "PN": self._search(r"PN:\s*(\S+)", text),
            "DESCRIPTION": self._search(r"DESCRIPTION:\s*([^\n]+)", text),
            "LOCATION": self._search(r"LOCATION:\s*(\d+)", text),
            "RECEIVER#": self._search(r"RECEIVER#:\s*(\d+)", text),
            "EXP DATE": self._search(r"EXP DATE:\s*(\S+)", text),
            "CERT SOURCE": self._search(r"CERT SOURCE:\s*(\w+)", text),
            "REC.DATE": self._search(r"REC.DATE:\s*(\S+)", text),
            "BATCH#": self._search(r"BATCH# :\s*(\d+)", text),
            "SN": self._search(r"SN:\s*(\d+)", text),
            "CONDITION": self._search(r"CONDITION:\s*(\S+)", text),
            "UOM": self._search(r"UOM:\s*(\S+)", text),
            "PO": self._search(r"PO:\s*(\S+)", text),
            "MFG": self._search(r"MFG:\s*(\w+)", text),
            "DOM": self._search(r"DOM:\s*(\S+)", text),
            "REMARK": ""
        }

        remark_data = self.extract_remark(text)
        if remark_data:
            data.update(remark_data)

        return data

    def extract_remark(self, text):
        lines = text.split('\n')
        remark_dict = {}
        try:
            remark_index = lines.index('REMARK:')
            remark_text = ' '.join(lines[remark_index + 1:]).strip()
            remark_info = re.findall(r'(\w+#) : (\S+)|Qty: (\d+)|NOTES: (.+)', remark_text)
            for match in remark_info:
                if match[0]:
                    remark_dict[match[0]] = match[1]
                elif match[2]:
                    remark_dict["Qty"] = match[2]
                if match[3]:
                    remark_dict["NOTES"] = match[3].rstrip()
        except ValueError:
            pass
        return remark_dict

    def _search(self, pattern, text, flags=0):
        match = re.search(pattern, text, flags)
        return match.group(1).strip() if match else None


pdf_path = "../files/sample_file/test_task.pdf"
extractor = PDFDataExtractor(pdf_path)
data = extractor.extract_information()
print(data)
