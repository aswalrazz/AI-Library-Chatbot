AI-Powered Research Paper Reviewer
 
Overview
The AI-Powered Research Paper Reviewer is a Streamlit-based web application designed to analyze research papers in PDF or DOCX format. It leverages advanced NLP models and AI APIs to provide summaries, readability scores, coherence analysis, improvement suggestions, and visualizations like word clouds and sentence length distributions. Additionally, it includes an AI-powered library chatbot and a research project finder using the Gemini 1.5 API.
Features

Document Processing: Extract text from PDF (using PyMuPDF) or DOCX (using python-docx) files.
Text Summarization: Generate concise summaries of research papers using a Hugging Face transformer model.
Readability Analysis: Calculate the Flesch Reading Ease score to assess text readability.
Coherence Analysis: Evaluate text coherence based on sentence-to-word ratio using SpaCy.
Improvement Suggestions: Provide actionable feedback for improving the paper using the Gemini 1.5 API.
Visualizations:
Word cloud to highlight frequent terms.
Sentence length distribution histogram with kernel density estimation.


AI Library Chatbot: Answer research-related questions using the Gemini 1.5 API.
Research Project Finder: Search for relevant research projects based on keywords using the Gemini 1.5 API.
Interactive UI: Streamlit-based interface for easy file uploads and result visualization.

Installation
Prerequisites

Python 3.8+
Tesseract OCR (optional, for advanced PDF text extraction if needed).
Gemini API key (replace the placeholder in the code with your own key).
Internet connection for Gemini API and Hugging Face model downloads.

Setup

Clone the repository:
git clone https://github.com/your-username/research-paper-reviewer.git
cd research-paper-reviewer


Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt


Configure the Gemini API key:

Replace the placeholder API key ("AIzaSyBovZqtc5X96w4aN24dafYKz3oxGaQgKt8") in the code with your own Gemini API key.


Run the application:
streamlit run app.py

Requirements
Create a requirements.txt file with the following:
streamlit==1.25.0
PyMuPDF==1.22.5
python-docx==0.8.11
textstat==0.7.3
transformers==4.31.0
spacy==3.5.3
google-generativeai==0.3.2
matplotlib==3.7.2
seaborn==0.12.2
pandas==2.0.3
wordcloud==1.9.2

Additionally, install the SpaCy language model:
python -m spacy download en_core_web_sm

Usage

Launch the App: Run streamlit run app.py and open the provided local URL (e.g., http://localhost:8501).
Upload a File: Upload a research paper in PDF or DOCX format.
View Analysis:
Summary: A concise summary of the paper.
Readability Score: Flesch Reading Ease score indicating text complexity.
Coherence Score: Sentence-to-word ratio for coherence assessment.
Improvement Suggestions: AI-generated feedback for enhancing the paper.
Visualizations: Word cloud and sentence length distribution.


Use AI Features:
Library Chatbot: Ask research-related questions (e.g., "How to structure a literature review?").
Research Project Finder: Enter keywords to find relevant research projects (e.g., "machine learning in healthcare").


Explore Results: Interact with visualizations and download feedback as needed.

Example

Upload a PDF research paper on "Machine Learning Applications."
Get a summary (e.g., "This paper explores machine learning techniques for predictive modeling...").
View readability score (e.g., 60.5, indicating moderate complexity).
Check coherence score (e.g., 0.05 sentences per word).
Receive feedback (e.g., "Consider adding more citations to support claims in Section 3...").
Visualize frequent terms in a word cloud and sentence length distribution in a histogram.

Project Structure
research-paper-reviewer/
├── data/
│   └── sample_paper.pdf        # Sample input file
├── app.py                      # Main Streamlit application
├── requirements.txt            # Dependencies
└── README.md                   # This file

Screenshots
   
Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For issues or suggestions, please open an issue on GitHub or contact your-email@example.com.
Acknowledgments

Powered by Streamlit, PyMuPDF, SpaCy, Hugging Face Transformers, and Google Gemini API.
Visualizations with Matplotlib, Seaborn, and WordCloud.
