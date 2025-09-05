# AI-Powered Research Paper Reviewer & Chatbot

This Streamlit-based web application analyzes research papers in PDF or DOCX format using advanced NLP models and AI APIs. It provides summaries, readability scores, coherence analysis, improvement suggestions, and visualizations like word clouds and sentence length distributions. Additionally, it includes an AI-powered library chatbot and a research project finder powered by the Gemini 1.5 API.

## Features
- **Document Processing**: Extracts text from PDF (using PyMuPDF) or DOCX (using python-docx) files.
- **Text Summarization**: Generates concise summaries using a Hugging Face transformer model (e.g., BART or T5).
- **Readability Analysis**: Calculates Flesch Reading Ease score to assess text complexity.
- **Coherence Analysis**: Evaluates text coherence via sentence-to-word ratio using SpaCy.
- **Improvement Suggestions**: Provides actionable feedback using the Gemini 1.5 API.
- **Visualizations**:
  - Word cloud to highlight frequent terms.
  - Sentence length distribution histogram with kernel density estimation.
- **AI Library Chatbot**: Answers research-related questions via Gemini 1.5 API.
- **Research Project Finder**: Searches for relevant research projects based on keywords using Gemini 1.5 API.
- **Interactive UI**: Streamlit interface for easy file uploads and result visualization.

## Installation

### Prerequisites
- Python 3.8 or higher
- Tesseract OCR (optional, for advanced PDF text extraction)
- Gemini API key (sign up at [Google Cloud](https://makersuite.google.com/) for a key)
- Internet connection for API calls and model downloads

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/research-paper-reviewer.git
   cd research-paper-reviewer
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Install SpaCy language model:
   ```bash
   python -m spacy download en_core_web_sm
   ```
5. Configure the Gemini API key:
   - Replace the placeholder (`AIzaSyBovZqtc5X96w4aN24dafYKz3oxGaQgKt8`) in `app.py` with your Gemini API key.
6. Run the application:
   ```bash
   streamlit run app.py
   ```

## Requirements
The following dependencies are listed in `requirements.txt`:
- streamlit==1.25.0
- PyMuPDF==1.22.5
- python-docx==0.8.11
- textstat==0.7.3
- transformers==4.31.0
- spacy==3.5.3
- google-generativeai==0.3.2
- matplotlib==3.7.2
- seaborn==0.12.2
- pandas==2.0.3
- wordcloud==1.9.2

## Usage
1. **Launch the App**: Run `streamlit run app.py` and open the local URL (e.g., `http://localhost:8501`) in your browser.
2. **Upload a File**: Upload a research paper in PDF or DOCX format.
3. **View Analysis**:
   - **Summary**: A concise summary of the paper.
   - **Readability Score**: Flesch Reading Ease score (e.g., 60.5 for moderate complexity).
   - **Coherence Score**: Sentence-to-word ratio for coherence.
   - **Improvement Suggestions**: AI-generated feedback (e.g., "Add citations to Section 3").
   - **Visualizations**: Word cloud and sentence length histogram.
4. **Use AI Features**:
   - **Library Chatbot**: Ask questions like "How to structure a literature review?"
   - **Research Project Finder**: Enter keywords (e.g., "machine learning in healthcare") to find projects.
5. **Explore Results**: Interact with visualizations and download feedback if needed.

## Example
- **Input**: Upload a PDF on "Machine Learning Applications."
- **Output**:
  - Summary: "This paper explores machine learning techniques for predictive modeling..."
  - Readability: 60.5 (moderate complexity)
  - Coherence: 0.05 sentences/word
  - Suggestions: "Consider adding more citations to support claims in Section 3..."
  - Visualizations: Word cloud (frequent terms: "machine learning", "prediction") and sentence length histogram.

## Project Structure
```
research-paper-reviewer/
├── data/
│   └── sample_paper.pdf  # Sample input file (not included in repo)
├── app.py                # Main Streamlit application
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
└── LICENSE               # MIT License file
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a Pull Request on GitHub.

**Ideas for Improvement**:
- Add support for more file formats (e.g., LaTeX).
- Enhance chatbot with context-aware responses.
- Integrate additional NLP models (e.g., BERT for sentiment analysis).

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For issues or suggestions, open an issue on GitHub or email vaswal919@gmail.com

## Acknowledgments
- Powered by Streamlit, PyMuPDF, SpaCy, Hugging Face Transformers, and Google Gemini API.
- Visualizations with Matplotlib, Seaborn, and WordCloud.
