import fitz # PyMuPDF
import docx
import re
import os

class resumeReader:
    def __init__(self, file_path): # Constructor receives file path from the main class
        self.file_path = file_path
        self.text = ""

    def extractText(self): 
        if not os.path.exists(self.file_path): # Making sure the file exists
            raise FileNotFoundError("Resume file not found.") # Error handling

        ext = os.path.splitext(self.file_path)[1].lower()  # Splitting the file type, and converting the type to lowercase

        if ext == '.pdf':  # Accepting PDF files
            self.read_pdf()
            
        elif ext == '.docx':  # Accepting DOCX files
            self.read_docx()
            
        else:
            raise ValueError("Unsupported file type. Please provide a PDF or DOCX file.") # Handling unsupported types.
        return self.text # Returns plain text

    def read_pdf(self):
        with fitz.open(self.file_path) as doc: # Using fitz (PyMuPDF) to open PDF files
            for page in doc: # Going through every page of the document
                self.text += page.get_text() # Extracting text

    def read_docx(self):
        doc = docx.Document(self.file_path) # Using docx to open Word files
        for para in doc.paragraphs: # Going through every paragraph of the document
            self.text += para.text + "\n" # Extracting text

    def extractEmail(self):
        matches = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', self.text) # Using regex pattern, our keyword is "@". Any character, then "@", then any character, followed by ".", then letters only
        return matches[0] if matches else None # If there were more than one email, it will return the first one only. Otherwise, return None

    def extractName(self):
        lines = self.text.strip().split("\n") # Look through it line by line
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if re.match(r"^[A-Z][a-z]+(\s[A-Z][a-z]+)+$", line): # First capital letter, then space, followed by other capital letter
                return line
        return "Unknown" # Didn't find name

    def extractSkills(self): # Searching for keywords in the whole document
        skillsSet = [
            'python', 'java', 'c++', 'machine learning', 'html', 'css', 'javascript',
            'flask', 'django', 'pandas', 'numpy', 'react', 'android', 'kotlin',
            'data analysis', 'sql', 'excel', 'power bi', 'communication'
        ]
        found = []
        lowerText = self.text.lower() # Plain text all lowercase
        for skill in skillsSet:
            if skill in lowerText: 
                found.append(skill) # Adding any skill found to the candidate's skill set
        return list(set(found)) # Casting the set into a list
