## **📌 HOW IT WORKS**  

### **1️⃣ Getting the API Key (Google Generative AI API)**  

This project uses **Google Generative AI API** for text summarization. Follow these steps to get your API key:  

1. **Go to Google AI Studio**:  
   - Visit [Google AI Studio](https://aistudio.google.com).  

2. **Sign in** using your Google account.  

3. **Generate an API Key**:  
   - Navigate to the **API Keys** section.  
   - Click **Generate API Key** and copy it.  

4. **Add the API key to the project**:  
   - Open the **`.env`** file in the project directory.  
   - Add this line:  
     ```plaintext
     GOOGLE_API_KEY=your_api_key_here
     ```  
   - Replace `your_api_key_here` with your actual API key.  

---

## **2️⃣ Code Structure**  

```plaintext
Financial-Report-Analyzer/
│── app.py                # Main Streamlit app
│── requirements.txt      # Required dependencies
│── README.md             # Project documentation
│── HOW_IT_WORKS.md       # Explanation of workflow
│
├── utils/
│   ├── text_extraction.py  # Extracts text from PDFs
│   ├── summarize.py        # AI-powered summarization
│
└── data/                 # Stores sample PDFs (optional)
```

---

## **3️⃣ Code Explanation**  

### **A) Text Extraction (`utils/text_extraction.py`)**  
This file extracts text from PDFs using **PyMuPDF (fitz)**.  

#### 🔹 **Code Example**  
```python
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    return text
```

#### 🔹 **How It Works?**  
- Opens the PDF  
- Extracts text page by page  
- Returns the extracted text  

---

### **B) AI-Powered Summarization (`utils/summarize.py`)**  
This file uses the **Google Generative AI API** to summarize extracted text.  

#### 🔹 **Code Example**  
```python
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize API
genai.configure(api_key=api_key)

def summarize_text(text):
    """Generate an AI summary of the given text."""
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(text)
    return response.text
```

#### 🔹 **How It Works?**  
- Loads the API key  
- Sends extracted text to **Google Gemini** model  
- Returns the summarized text  

---

### **C) Streamlit Frontend (`app.py`)**  
This file provides the **User Interface (UI) using Streamlit**.  

#### 🔹 **Code Example**  
```python
import streamlit as st
from utils.text_extraction import extract_text_from_pdf
from utils.summarize import summarize_text

st.set_page_config(page_title="Financial Report Analyzer", layout="wide", theme="dark")

st.title("📊 Financial Report Analyzer")

uploaded_file = st.file_uploader("Upload a Financial Report (PDF)", type="pdf")

if uploaded_file is not None:
    with st.spinner("Extracting text..."):
        text = extract_text_from_pdf(uploaded_file)
        st.text_area("Extracted Text", text, height=300)

    if st.button("Summarize"):
        with st.spinner("Summarizing..."):
            summary = summarize_text(text)
            st.success("Summary Generated!")
            st.text_area("Summary", summary, height=200)
```

#### 🔹 **How It Works?**  
1. Uploads a **PDF file**  
2. Extracts **text from the PDF**  
3. Uses **AI to summarize the text**  
4. Displays the **extracted text and summary**  

---

## **4️⃣ Workflow Diagram**  

```plaintext
[ User Uploads PDF ]  
        ⬇  
[ Extract Text using PyMuPDF ]  
        ⬇  
[ Send to Google AI for Summarization ]  
        ⬇  
[ Display Extracted Text & Summary ]  
```

---

## **🎯 Conclusion**  
This document explains:  
✅ **How to get the API key**  
✅ **Project structure**  
✅ **How the code works**  
✅ **Workflow of the application**  

Now, you're ready to **analyze financial reports** with AI! 🚀
