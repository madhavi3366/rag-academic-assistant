# 📚 AI Academic Assistant (RAG)

An AI-powered Academic Assistant that allows users to upload study materials in PDF format and ask questions based on the content using Retrieval-Augmented Generation (RAG).

## 🚀 Features

- Upload and process PDF study materials
- Extract text from multiple PDFs
- Split documents into searchable chunks
- Generate embeddings using Sentence Transformers
- Store embeddings in FAISS vector database
- Retrieve relevant content for user queries
- AI-powered question answering
- Source document display
- Streamlit web interface

---

## 🏗️ Project Architecture

User Question
↓
FAISS Similarity Search
↓
Retrieve Relevant Chunks
↓
Build Context
↓
Language Model
↓
Generate Answer

---

## 📂 Project Structure

```text
rag-academic-assistant/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── sample.pdf
│
└── __pycache__/
```

---

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- FAISS
- Hugging Face Embeddings
- Sentence Transformers
- PyPDF
- Transformers

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/rag-academic-assistant.git
cd rag-academic-assistant
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📄 Add PDF Documents

Place your PDF files inside the `data` folder.

Example:

```text
data/
├── sample.pdf
├── machine_learning_notes.pdf
└── ai_textbook.pdf
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 💡 How It Works

### Step 1
Load PDF documents from the `data` folder.

### Step 2
Split text into smaller chunks using:

- Chunk Size: 500
- Chunk Overlap: 100

### Step 3
Generate embeddings using:

```text
all-MiniLM-L6-v2
```

### Step 4
Store vectors in FAISS.

### Step 5
Retrieve top matching chunks for user queries.

### Step 6
Generate answers using a local transformer model.

---

## 📷 Application Workflow

1. Click **Load Documents**
2. Wait for document processing
3. Enter a question
4. Click **Send**
5. View generated answer
6. Optionally display source passages

---

## 🎯 Example Questions

- What is Machine Learning?
- Explain Neural Networks.
- What is Retrieval-Augmented Generation?
- Summarize Chapter 1.
- What are the advantages of AI?

---

## 🔒 Security

Sensitive files are excluded using `.gitignore`.

```text
.env
__pycache__/
*.pyc
```

---

## 📈 Future Enhancements

- Chat history memory
- Multi-document summarization
- Research paper analysis
- Quiz generation
- Voice interaction
- Web search integration
- AI Agent workflow using LangGraph
- Cloud deployment

---

## 🎓 Academic Relevance

This project demonstrates:

- Natural Language Processing (NLP)
- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Semantic Search
- Information Retrieval
- Large Language Model Integration

---

## 👨‍💻 Author

Madhavi

AI Academic Assistant using Retrieval-Augmented Generation (RAG)
