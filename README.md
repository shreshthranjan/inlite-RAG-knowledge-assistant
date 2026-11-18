# 💡 Inlite Knowledge Assistant

An AI-powered document question-answering application built using Retrieval-Augmented Generation (RAG). It allows users to ask questions about their documents and receive context-aware answers using Google's Gemini API.

## 🚀 Features

- **Document Processing:** Loads and processes text documents.
- **Excel Support:** Reads `.xlsx` and `.xls` workbooks, including multiple worksheets.
- **Text Chunking:** Divides documents into smaller chunks with overlapping content.
- **Semantic Search:** Uses Sentence Transformers to generate embeddings.
- **Vector Search:** Uses FAISS to retrieve relevant document chunks.
- **AI-Powered Answers:** Integrates Google Gemini API to generate answers using retrieved context.
- **Interactive Interface:** Built with Streamlit.
- **Source References:** Displays retrieved document sources and similarity scores.
- **Document Upload:** Supports uploading text and Excel files through the interface.

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- Sentence Transformers
- FAISS
- Pandas
- NumPy
- OpenPyXL
- xlrd

## 📂 Project Structure

```text
inlite-knowledge-assistant/
│
├── app.py
├── rag.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── documents/
│   ├── client_services.txt
│   ├── marketing_strategies.txt
│   └── campaign_reports.txt
│
└── uploaded_documents/
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/shreshthranjan/inlite-knowledge-assistant.git
cd inlite-knowledge-assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your Gemini API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Obtain an API key through Google AI Studio.

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

`http://localhost:8501`

## 🔄 How It Works

1. Documents are loaded and their text is extracted.
2. The text is divided into smaller chunks with overlap.
3. Sentence Transformers converts the chunks into numerical embeddings.
4. FAISS indexes the embeddings for similarity search.
5. A user submits a question through the Streamlit interface.
6. The question is converted into an embedding.
7. FAISS retrieves the most relevant document chunks.
8. The retrieved context and question are passed to Gemini.
9. Gemini generates an answer based on the supplied context.
10. The answer and source references are displayed in the interface.

## 🔐 Environment Variables

The application requires a Gemini API key.

Never commit your `.env` file or expose your API key publicly.

## 📌 Future Improvements

- PDF and Word document support.
- Advanced Excel data analysis.
- Improved document management.
- Persistent vector storage.
- Deployment and cloud storage integration.

## 👨‍💻 Author

**Shreshth Ranjan**

Developed as a hands-on project to explore Python, Generative AI, Retrieval-Augmented Generation and semantic search.
