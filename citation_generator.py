pip install rake-nltk pybtex
from pybtex.database import parse_string

def generate_citation(text, style='apa'):
    metadata = extract_metadata(text)  # From pdf_processor
    
    entry = f"""
@article{{key,
    author = {{{" and ".join(metadata['authors'])}}},
    title = {{{metadata['title']}}},
    year = {{{metadata['year']}}}}
    """
    
    bib_data = parse_string(entry, 'bibtex')
    return bib_data.entries['key'].to_string(style)
