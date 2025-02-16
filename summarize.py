import google.generativeai as genai
import streamlit as st

# Configure Google Gemini API
API_KEY = "ENTER YOUR API"  # Replace with your API key
genai.configure(api_key=API_KEY)

def summarize_text(text):
    """Summarizes the extracted financial report text using Google Gemini API."""
    if len(text) > 12000:
        text = text[:12000]  # Truncate large text to fit API limits
    
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Summarize this financial report: {text}")
    
    return response.text if response.text else "Summary not available."
