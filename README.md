# 🤖 Hugging Face AI Assistant

A smart AI-powered assistant that helps users explore and understand the **Hugging Face documentation** using semantic search and LLMs.

---

##  Project Title & Description

**Hugging Face AI Assistant**  
An AI-powered chatbot that answers questions about Hugging Face documentation using semantic search and LLM reasoning.

---

##  Overview

This project solves a common problem:  
 *Hugging Face documentation is large and sometimes hard to navigate efficiently.*

Instead of manually searching through documentation, this assistant:
- Indexes the official Hugging Face documentation repository
- Uses **semantic search** to retrieve relevant content
- Generates structured and easy-to-read answers using an LLM

###  Why it's useful
- Saves time searching documentation
- Provides contextual answers instead of raw pages
- Combines **search + AI reasoning (RAG)**

---

##  Installation

###  Requirements
- Python **3.12+**
- A [Groq API key](https://console.groq.com/)

### Setup

```bash
#1. Clone the repository
git clone https://github.com/waad-moaness/Hero-Ai-Agent.git 
cd Hero-Ai-Agent

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

# 3. Install dependencies
pip install -e .

# Set your API key
export GROQ_API_KEY="your_groq_api_key_here"
```

---

## Usage

### Launch the web interface

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

###  Example Questions
- How do I deploy a model on Hugging Face Spaces?
- How to add API keys securely?
- What is Text Generation Inference (TGI)?

###  How it works
1. Downloads Hugging Face documentation from GitHub
2. Parses Markdown files and extracts content
3. Splits content into chunks
4. Indexes data using **minsearch**
5. User query → semantic search → LLM generates answer

---

##  Features

-  **Semantic Search** over Hugging Face docs
-  **AI Agent** powered by `pydantic-ai`
-  **Interactive Chat UI** using Streamlit
-  **Automatic GitHub Repo Indexing**
-  **Source Citations** with direct links
-  **Streaming-like Responses**
-  **Logging System** for interactions


---



##  Credits / Acknowledgments

- Hugging Face documentation repository
- `pydantic-ai` for agent framework
- `minsearch` for indexing and search
- Streamlit for UI

---

##  License

This project is licensed under the **MIT License**.

##  Demo 

Try the agent yourself [https://hero-ai-huggingface-agent.streamlit.app]

## Video Demo 

Watch demo video on how to setup the agent locally: [https://drive.google.com/file/d/1s-E7TBzOjn_uSEdDkU1DJXXnSQQgkV0j/view?usp=sharing]