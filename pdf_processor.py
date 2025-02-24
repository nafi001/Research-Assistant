pip install streamlit PyPDF2 pdfplumber transformers rake-nltk pybtex
import pdfplumber
import re

def extract_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_metadata(text):
    return {
        "title": re.search(r"(?i)title:\s*(.+?)\n", text) or "Untitled",
        "authors": re.findall(r"(?i)author[ s]*:\s*(.+?)\n", text),
        "year": re.search(r"(?i)year:\s*(\d{4})", text) or "N/A"
    }
