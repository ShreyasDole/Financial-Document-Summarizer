import streamlit as st
from utils.text_extraction import extract_text_from_pdf
from utils.summarize import summarize_text

# Set Dark Mode Theme
st.set_page_config(
    page_title="📊 Financial Report Analyzer",
    layout="wide",
)

# Custom Dark Mode CSS
st.markdown(
    """
    <style>
        body {
            background-color: #121212;
            color: white;
        }
        .stApp {
            background-color: #121212;
        }
        .stFileUploader {
            border: 2px dashed #bb86fc !important;
            padding: 10px !important;
        }
        .stButton>button {
            background-color: #bb86fc !important;
            color: white !important;
            font-size: 16px !important;
            padding: 10px 20px !important;
            border-radius: 8px !important;
            border: none !important;
        }
        .stTextArea textarea {
            font-size: 14px !important;
            background-color: #1e1e1e !important;
            color: white !important;
            border-radius: 5px;
        }
        .stExpander {
            border: 1px solid #bb86fc !important;
            border-radius: 8px;
        }
        .stExpander div {
            background-color: #1e1e1e !important;
            color: white !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎯 Title & Description
st.title("📊 Financial Report Analyzer")
st.write("Easily extract and summarize financial reports with AI, now in **dark mode** 🌙.")

# 🚀 File Upload Section
st.subheader("📂 Upload a Financial Report (PDF)")
uploaded_file = st.file_uploader("", type="pdf")

if uploaded_file is not None:
    # 🔄 Extraction Process
    with st.spinner("Extracting text from the document... ⏳"):
        extracted_text = extract_text_from_pdf(uploaded_file)
    
    # ✅ Display Extracted Text (Collapsible)
    with st.expander("📜 **Extracted Report Text**", expanded=False):
        st.text_area(
            "Extracted Content",
            extracted_text[:2000] + "..." if len(extracted_text) > 2000 else extracted_text,
            height=300
        )

    # 📌 Summary Section
    if st.button("🔍 Generate Summary"):
        with st.spinner("Summarizing report... 🧠"):
            summary = summarize_text(extracted_text)
        
        # 🎯 Display Summary
        st.subheader("📑 AI-Generated Summary")
        st.success(summary)

# 🎨 Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>🌙 Built for Dark Mode with ❤️ using Streamlit & AI</p>",
    unsafe_allow_html=True
)
