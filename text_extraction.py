import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    """Extracts text from a given PDF file."""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n\n"
    return text
