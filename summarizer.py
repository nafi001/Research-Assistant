from transformers import pipeline

def summarize_text(text, max_length=150):
    if not text or len(text.strip()) == 0:
        return "No text found to summarize."
    
    try:
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        # Split text into chunks if it's too long
        max_chunk_size = 1024  # BART's max token limit
        chunks = [text[i:i + max_chunk_size] for i in range(0, len(text), max_chunk_size)]
        
        summaries = []
        for chunk in chunks:
            summary = summarizer(chunk, max_length=max_length, min_length=30, do_sample=False)
            summaries.append(summary[0]['summary_text'])
        
        return " ".join(summaries)
    except Exception as e:
        return f"Error during summarization: {str(e)}"
