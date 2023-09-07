import streamlit as st
import pdftotextconverter
import texttopdfconverter

st.set_page_config(layout="wide")

def main():
    st.title("PDF to/from Text")

    # Sidebar with buttons for each application
    st.sidebar.title("Select an Application")
    app_selection = st.sidebar.radio("Go to:", ("PDF to Text Converter", "Text to PDF Converter"))

    if app_selection == "PDF to Text Converter":
        pdftotextconverter.main()
    elif app_selection == "Text to PDF Converter":
        texttopdfconverter.main()

if __name__ == "__main__":
    main()
