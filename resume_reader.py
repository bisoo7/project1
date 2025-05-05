import fitz  # type: ignore
import docx
import re
import os

class ResumeReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = ""

    def extract_text(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError("Resume file not found.")

        ext = os.path.splitext(self.file_path)[1].lower()

        if ext == '.pdf':
            self._read_pdf()
        elif ext == '.docx':
            self._read_docx()
        else:
            raise ValueError("Unsupported file type. Please provide a .pdf or .docx file.")
        return self.text

    def _read_pdf(self):
        with fitz.open(self.file_path) as doc:
            for page in doc:
                self.text += page.get_text()

    def _read_docx(self):
        doc = docx.Document(self.file_path)
        for para in doc.paragraphs:
            self.text += para.text + "\n"

    def extract_email(self):
        matches = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', self.text)
        return matches[0] if matches else None

    def extract_name(self):
        lines = self.text.strip().split("\n")
        return lines[0] if lines else "Unknown"

    def extract_skills(self):
        common_skills = [
            'python', 'java', 'c++', 'machine learning', 'html', 'css', 'javascript',
            'flask', 'django', 'pandas', 'numpy', 'react', 'android', 'kotlin',
            'data analysis', 'sql', 'excel', 'power bi', 'communication'
        ]
        found = []
        lower_text = self.text.lower()
        for skill in common_skills:
            if skill in lower_text:
                found.append(skill)
        return list(set(found))