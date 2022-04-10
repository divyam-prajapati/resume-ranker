import docx2txt
import fitz

def extract_text_from_doc(doc_path):
    temp = docx2txt.process(doc_path)
    text = [line.replace('\t', ' ') for line in temp.split('\n') if line]
    return ' '.join(text)

def extract_text_from_pdf(pdf_path):

    doc = fitz.open(pdf_path)
    text=""
    for page in doc:
        text += str(page.get_text())
    return text
