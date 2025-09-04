import streamlit as st
import fitz  # PyMuPDF for PDF text extraction
import docx
import textstat
from transformers import pipeline
import spacy
import google.generativeai as genai
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from wordcloud import WordCloud

# Load NLP Models
nlp = spacy.load("en_core_web_sm")
summarizer = pipeline("summarization")

# Configure Gemini API
genai.configure(api_key="AIzaSyBovZqtc5X96w4aN24dafYKz3oxGaQgKt8")

# Function to extract text from PDFs
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = "\n".join([page.get_text("text") for page in doc])
    return text.strip()

# Function to extract text from DOCX
def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    return "\n".join([para.text for para in doc.paragraphs]).strip()

# Function to summarize text
def summarize_text(text, max_words=200):
    if not text.strip():
        return "No content extracted for summarization."
    try:
        summary = summarizer(text, max_length=max_words, min_length=50, do_sample=False)
        return summary[0]['summary_text'] if summary else "Summarization failed."
    except Exception as e:
        return f"Error during summarization: {str(e)}"

# Function to analyze readability
def analyze_readability(text):
    return textstat.flesch_reading_ease(text) if text.strip() else "N/A"

# Function to check coherence
def check_coherence(text):
    if not text.strip():
        return "N/A"
    doc = nlp(text)
    return len(list(doc.sents)) / len(doc)  # Sentence-to-word ratio

# Function to generate improvement suggestions using Gemini 1.5
def generate_feedback(text):
    if not text.strip():
        return "No text available for review."
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(f"Review this research paper and suggest improvements: {text}")
        return response.text if response else "No feedback generated."
    except Exception as e:
        return f"Error generating feedback: {str(e)}"

# Function to generate word cloud
def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)

# Function to plot sentence length distribution
def plot_sentence_length_distribution(text):
    sentences = [len(sent.text.split()) for sent in nlp(text).sents]
    df = pd.DataFrame(sentences, columns=['Sentence Length'])
    fig, ax = plt.subplots()
    sns.histplot(df, bins=20, kde=True, ax=ax)
    ax.set_title("Sentence Length Distribution")
    ax.set_xlabel("Number of Words")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

# Function to simulate AI Library Chatbot
def ai_library_chatbot():
    st.subheader("📚 AI Library Chatbot")
    user_query = st.text_input("Ask a research-related question:")
    if user_query:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(f"Answer this library research question: {user_query}")
        st.write(response.text if response else "No response generated.")

# Function to find research projects
def research_project_finder():
    st.subheader("🔎 Research Project Finder AI")
    keyword = st.text_input("Enter keywords to find research projects:")
    if keyword:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(f"Find research projects related to: {keyword}")
        st.write(response.text if response else "No projects found.")

# Streamlit UI
st.title("📑 AI-Powered Research Paper Reviewer")
st.write("Upload a research paper (PDF/DOCX) to get insights, summaries, and feedback.")

uploaded_file = st.file_uploader("Upload Paper", type=["pdf", "docx"])

if uploaded_file:
    st.write("Processing file...")
    file_type = uploaded_file.name.split(".")[-1]
    text = extract_text_from_pdf(uploaded_file) if file_type == "pdf" else extract_text_from_docx(uploaded_file)
    
    st.subheader("🔍 Extracted Summary")
    summary = summarize_text(text)
    st.write(summary)
    
    st.subheader("📖 Readability Score")
    readability_score = analyze_readability(text)
    st.write(f"Readability Score: {readability_score}")
    
    st.subheader("🔗 Coherence Score")
    coherence_score = check_coherence(text)
    st.write(f"Coherence Score: {coherence_score}")
    
    st.subheader("📝 Improvement Suggestions")
    feedback = generate_feedback(text)
    st.write(feedback)
    
    st.subheader("🌥️ Word Cloud Visualization")
    generate_wordcloud(text)
    
    st.subheader("📊 Sentence Length Distribution")
    plot_sentence_length_distribution(text)
    
    st.success("Analysis Complete! 🎯")

# Additional AI Features
ai_library_chatbot()
research_project_finder()
