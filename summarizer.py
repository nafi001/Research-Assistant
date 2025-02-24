
from transformers import pipeline

def summarize_text(text, max_length=150):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return summarizer(text, max_length=max_length, min_length=30, do_sample=False)[0]['summary_text']
