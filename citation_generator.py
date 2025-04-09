aaaaa
from pybtex.database import parse_string
from pdf_processor import extract_metadata  # Import the metadata function

def generate_citation(text, style='apa'):
    metadata = extract_metadata(text)  # Extract metadata from the text
    
    # Create a BibTeX entry
    entry = f"""
@article{{key,
    author = {{{" and ".join(metadata['authors'])}}},
    title = {{{metadata['title']}}},
    year = {{{metadata['year']}}}
}}
    """
    
    # Parse the entry and generate citation
    bib_data = parse_string(entry, 'bibtex')
    return bib_data.entries['key'].to_string(style)
