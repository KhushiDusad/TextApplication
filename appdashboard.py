import streamlit as st
import pdftotextconverter
import texttopdfconverter
import texttospeechconverter
import image_text_extractor

st.set_page_config(layout="wide")

def main():
    st.title("Textopia: All About Text")

    # Sidebar with buttons for each application
    st.sidebar.title("Select an Application")
    app_selection = st.sidebar.radio("Go to:", ("PDF to Text Converter", "Text to PDF Converter", "Text to Speech Converter", "Image Text Extractor"))

    if app_selection == "PDF to Text":
        pdftotextconverter.main()
    elif app_selection == "Text to PDF":
        texttopdfconverter.main()
    elif app_selection == "Text to Speech":
        texttospeechconverter.main()
    elif app_selection == "Image Text Extractor":
        image_text_extractor.main()

if __name__ == "__main__":
    main()
