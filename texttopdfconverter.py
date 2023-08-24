import streamlit as st
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(text, pdf_path):
    doc = SimpleDocTemplate(pdf_path, pagesize=landscape(letter))
    styles = getSampleStyleSheet()
    
    content = []
    content.append(Spacer(1, 12))
    
    for line in text.split('\n'):
        content.append(Paragraph(line, styles['Normal']))
    
    doc.build(content)

def main():
    st.title("Text to PDF Converter")
    st.info("Please note that this application works best for converting English text to PDF.")
    input_text = st.text_area("Enter the text you want to convert to PDF:", height=200)
    save_button = st.button("Convert and Save as PDF")
    
    if save_button:
        pdf_path = "converted_text.pdf"
        create_pdf(input_text, pdf_path)
        st.success(f"PDF generated and saved as {pdf_path}")

if __name__ == "__main__":
    main()
