import streamlit as st
import pyttsx3
from io import BytesIO
import base64

def speak(selected_voice, text):
    converter = pyttsx3.init()
    converter.setProperty('voice', selected_voice)
    converter.setProperty('rate', 150)
    converter.setProperty('volume', 1)
    converter.save_to_file(text, 'output.mp3')
    converter.runAndWait()

def main():
    st.title("Text-to-Speech with Voice Selection")

    n = st.radio("Select a voice:", ("Male Voice", "Female Voice"))
    
    if n == "Male Voice":
        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    else:
        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

    text_input = st.text_area("Enter the text:")

    speak(voice_id, text_input)
    audio_file = open("output.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3")

    # Download audio
    if st.button("Download Audio"):
        audio_file = open("output.mp3", "rb")
        audio_bytes = audio_file.read()
        b64 = base64.b64encode(audio_bytes).decode()
        st.markdown(f'<a href="data:audio/mp3;base64,{b64}" download="output.mp3">Download Audio</a>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
