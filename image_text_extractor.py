import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
def extract_text_from_image(image):
    try:
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print("An error occurred:", e)
        return None

def main():
    st.title("Image Text Extractor")
    st.write("Upload an image or paste an image URL to extract text.")

    image_upload = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    image_url = st.text_input("Paste image URL")

    if image_upload is not None:
        image = Image.open(image_upload)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        extracted_text = extract_text_from_image(image)
        if extracted_text:
            st.write("Extracted Text:")
            st.write(extracted_text)
        else:
            st.write("Text extraction failed.")

    elif image_url:
        try:
            response = requests.get(image_url)
            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                st.image(image, caption="Web Image", use_column_width=True)
                extracted_text = extract_text_from_image(image)
                if extracted_text:
                    st.write("Extracted Text:")
                    st.write(extracted_text)
                else:
                    st.write("Text extraction failed.")
            else:
                st.write("Image download failed. Status code:", response.status_code)
        except Exception as e:
            st.write("An error occurred:", e)

if __name__ == "__main__":
    main()
