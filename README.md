# 📄 ChatPDF with AI Agent

A powerful Streamlit-based application that allows you to chat with your PDF and DOCX documents using AI. Built with LangChain and Ollama, this tool provides intelligent document analysis, summarization, and Q&A capabilities.

## 🌟 Features

- **📄 Multi-format Support**: Upload and process both PDF and DOCX files
- **🤖 AI-Powered Chat**: Ask questions about your documents and get intelligent responses
- **📝 Smart Summarization**: Get comprehensive summaries of entire documents
- **📚 Topic-wise Analysis**: Automatic topic detection and section-by-section explanations
- **💬 Chat History**: Maintain conversation history throughout your session
- **🎨 Modern UI**: Clean, responsive interface with beautiful styling
- **⚡ Real-time Processing**: Instant document processing and AI responses

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Ollama installed and running locally
- Llama3.1:8b model downloaded

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/abhay-2108/ChatPDF-with-AI-Agent.git
   cd ChatPDF-with-AI-Agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Ollama**
   ```bash
   # Install Ollama (if not already installed)
   # Visit: https://ollama.ai/
   
   # Download the required model
   ollama pull llama3.1:8b
   ```

4. **Run the application**
   ```bash
   streamlit run chatpdf.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8501`

## 📖 Usage Guide

### 1. Upload Your Document
- Click on the file uploader
- Select a PDF or DOCX file
- The document will be automatically processed

### 2. Start Chatting
- Type your questions in the chat input
- Get AI-powered responses based on your document content
- View the conversation history below

### 3. Use Advanced Features
- **Summarize Full Document**: Get a comprehensive summary of the entire document
- **Explain Topic-Wise**: Get section-by-section analysis of the document

## 🛠️ Technical Details

### Architecture
- **Frontend**: Streamlit for web interface
- **AI Backend**: LangChain with Ollama integration
- **Document Processing**: PyPDF2 for PDFs, python-docx for DOCX files
- **Text Processing**: Custom regex-based topic splitting and markdown removal

### Key Components

- **Document Extraction**: Supports PDF and DOCX formats with text extraction
- **Text Processing**: Removes markdown formatting and splits content by topics
- **AI Integration**: Uses Ollama with Llama3.1:8b model for natural language processing
- **Chat Interface**: Real-time chat with persistent session history

## 📋 Requirements

```
langchain-ollama
langchain-core
PyPDF2
python-docx
streamlit
```

## 🔧 Configuration

### Model Configuration
The application uses the `llama3.1:8b` model by default. You can modify the model in `chatpdf.py`:

```python
llm = OllamaLLM(model="llama3.1:8b")
```

### Available Models
- `llama3.1:8b` (default)
- `llama3.1:70b` (for better performance)
- `mistral:7b`
- `codellama:7b`

## 🎯 Use Cases

- **Academic Research**: Analyze research papers and academic documents
- **Business Documents**: Review contracts, reports, and business documents
- **Technical Documentation**: Understand technical manuals and guides
- **Legal Documents**: Extract key information from legal texts
- **Educational Content**: Study materials and textbooks


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Made with ❤️ by [abhay-2108](https://github.com/abhay-2108)** 