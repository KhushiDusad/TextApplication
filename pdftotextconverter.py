import streamlit as st
import PyPDF2
import os
import tempfile

def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()
    return text

def main():
    st.title("PDF to Text Converter")
    st.info("Please note that this application works best for PDFs containing text in English.")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        # Save the uploaded PDF to a temporary file
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_path = temp_file.name
            temp_file.write(uploaded_file.read())
        
        text = pdf_to_text(temp_path)
        
        # Display extracted text
        st.subheader("Extracted Text:")
        st.text(text)
        
        # Remove the temporary file
        os.remove(temp_path)

if __name__ == "__main__":
    main()
