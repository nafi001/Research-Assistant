aa
import pdfplumber
import re

def extract_text(pdf_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"Error extracting text: {str(e)}")
    return text

def extract_metadata(text):
    title = re.search(r"(?i)title:\s*(.+?)\n", text)
    authors = re.findall(r"(?i)author[ s]*:\s*(.+?)\n", text)
    year = re.search(r"(?i)year:\s*(\d{4})", text)
    
    return {
        "title": title.group(1).strip() if title else "Untitled",
        "authors": [author.strip() for author in authors] if authors else ["Unknown"],
        "year": year.group(1).strip() if year else "N/A"
    }
