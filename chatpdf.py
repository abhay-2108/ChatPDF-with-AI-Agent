from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from PyPDF2 import PdfReader
from docx import Document
import streamlit as st
import re

def extract_text(file, ext):
    if ext == "pdf":
        reader = PdfReader(file)
        return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    elif ext == "docx":
        doc = Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    return ""

def remove_markdown(text):
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    text = re.sub(r"#+\s*", "", text)
    text = re.sub(r"`(.*?)`", r"\1", text)
    return text.strip()

def split_by_topic(text):
    topics = re.split(r'\n(?=(?:Chapter|Section|Topic|Unit)\s+\d+[:\-]?)', text, flags=re.IGNORECASE)
    return [t.strip() for t in topics if len(t.strip()) > 100]

llm = OllamaLLM(model="llama3.1:8b")
parser = StrOutputParser()

st.set_page_config("📄 PDF Chatbot", layout="centered")
st.markdown("<h1 style='text-align: center;'>Chat with Your PDF / DOCX</h1>", unsafe_allow_html=True)

if "initialized" not in st.session_state:
    st.session_state.chat_history = []
    st.session_state.initialized = True

uploaded = st.file_uploader("📎 Upload a PDF or DOCX", type=["pdf", "docx"])
if uploaded:
    ext = uploaded.name.split('.')[-1].lower()
    doc_text = extract_text(uploaded, ext)
    if not doc_text:
        st.error("No text found.")
        st.stop()
    doc_text = remove_markdown(doc_text)

    st.success("File uploaded and processed.")

    st.markdown("### 💬 Ask Anything About the Document")
    user_input = st.chat_input("Type your question here...")

    if user_input:
        prompt_template = PromptTemplate.from_template(
            "You are a helpful document assistant. Use the context below to answer clearly.\n\nContext:\n{text}\n\nQuestion: {question}"
        )
        chain = prompt_template | llm | parser
        response = chain.invoke({"text": doc_text, "question": user_input})
        st.session_state.chat_history.append((user_input, response))

    st.markdown("""
        <style>
        .user-msg {
            background: #000000;
            padding: 10px 15px;
            border-radius: 15px;
            margin: 5px 0;
            max-width: 75%;
            align-self: flex-end;
            margin-left: auto;
            text-align: right;
        }
        .ai-msg {
            background: #000000;
            padding: 10px 15px;
            border-radius: 15px;
            margin: 5px 0;
            max-width: 75%;
            text-align: left;
        }
        </style>
    """, unsafe_allow_html=True)

    for q, a in st.session_state.chat_history:
        st.markdown(f"<div class='user-msg'>{q}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='ai-msg'>{a}</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Summarize Full Document"):
            summary_prompt = PromptTemplate.from_template("Summarize this document clearly:\n\n{text}")
            chain = summary_prompt | llm | parser
            summary = chain.invoke({"text": doc_text})
            st.session_state.chat_history.append(("Summarize the full document", summary))
            st.rerun()

    with col2:
        if st.button("Explain Topic-Wise"):
            topics = split_by_topic(doc_text)
            if topics:
                st.session_state.chat_history.append(("Explain topic-wise", "Summarizing top sections..."))
                for topic in topics[:3]:  # You can increase this if needed
                    topic_prompt = PromptTemplate.from_template("Summarize this section:\n\n{topic}")
                    chain = topic_prompt | llm | parser
                    topic_summary = chain.invoke({"topic": topic})
                    st.session_state.chat_history.append((topic.split("\n")[0], topic_summary))
                st.rerun()
            else:
                st.warning("⚠️ Couldn't find clear topic divisions.")
