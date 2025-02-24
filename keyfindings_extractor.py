from rake_nltk import Rake

def extract_key_findings(text, num_points=5):
    r = Rake()
    r.extract_keywords_from_text(text)
    return r.get_ranked_phrases()[:num_points]
