import streamlit as st
import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from transformers import pipeline   # FREE MODEL

# Load environment variables
load_dotenv()

st.set_page_config(page_title="AI Academic Assistant", layout="wide")

st.title("📚 AI Academic Assistant (RAG)")
st.markdown("### Ask questions from your study materials")

# -------------------------
# CACHE HEAVY PROCESS
# -------------------------
@st.cache_resource
def load_vectorstore():
    documents = []
    for file in os.listdir("data"):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(f"data/{file}")
            documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.from_documents(chunks, embeddings)

# -------------------------
# LOAD FREE AI MODEL (FIXED)
# -------------------------
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="distilgpt2")  # ✅ FIXED

# -------------------------
# Load Documents
# -------------------------
if st.button("📂 Load Documents"):
    with st.spinner("Processing PDFs... Please wait ⏳"):
        st.session_state.vectorstore = load_vectorstore()
        st.success("Documents loaded successfully!")

# -------------------------
# Chat Memory
# -------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -------------------------
# User Input
# -------------------------
query = st.text_input("💬 Ask a question:")

if st.button("Send") and query:
    if "vectorstore" in st.session_state:

        docs = st.session_state.vectorstore.similarity_search(query, k=3)
        context = " ".join([doc.page_content for doc in docs])

        generator = load_model()

        prompt = f"""
Context:
{context}

Question: {query}

Answer in simple words:
"""

        result = generator(prompt, max_length=200)
        answer = result[0]["generated_text"]

        st.session_state.chat_history.append(("You", query))
        st.session_state.chat_history.append(("AI", answer))

        st.session_state.docs = docs

    else:
        st.warning("⚠️ Please click 'Load Documents' first!")

# -------------------------
# Display Chat
# -------------------------
for role, msg in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 AI:** {msg}")

# -------------------------
# Show Sources
# -------------------------
if st.checkbox("📄 Show Sources") and "docs" in st.session_state:
    for doc in st.session_state.docs:
        st.write(doc.page_content[:200])