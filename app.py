

import streamlit as st
import tempfile
from pdf_processor import extract_text
from summarizer import summarize_text
from citation_generator import generate_citation
from keyfindings_extractor import extract_key_findings

st.title("📚 Free Academic Research Assistant")

uploaded_file = st.file_uploader("Upload research paper (PDF)", type="pdf")

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.getvalue())
        text = extract_text(tmp.name)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Summary")
        summary = summarize_text(text)
        st.write(summary)
        
        st.header("Key Findings")
        findings = extract_key_findings(text)
        for i, finding in enumerate(findings, 1):
            st.write(f"{i}. {finding}")
    
    with col2:
        st.header("Citations")
        apa = generate_citation(text, 'apa')
        st.subheader("APA Style")
        st.code(apa)
        
        mla = generate_citation(text, 'mla')
        st.subheader("MLA Style")
        st.code(mla)
