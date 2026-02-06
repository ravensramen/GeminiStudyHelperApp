import streamlit as st
import json
from google import genai
from google.genai import types

#set page title on tab
st.set_page_config(page_title="Flashcard App", layout="centered")

#loads my API key from the streamlit framework
api_key = st.secrets["GEMINI_API_KEY"]

#initialize client with API key
client = genai.Client(api_key=api_key)

#title of streamlit site
st.title("Voice to Study Notes App")

#write main program prompt
st.write("Talk about what you learned in lecture today, Gemini can turn it into structured"
" notes and flashcards that you can study with!"
)

#take in audio file from user
audio_file = st.audio_input("Record your topic")


#Button interactivity 
if st.button("Generate Notes & Flashcards"):  
    if not audio_file: #if button was clicked without input
        st.warning("Record some audio first!.")
else:
    with st.spinner("Generating..."):
        try:
            audio_part = types.Part( #convert audio to a format gemini can evaluate
                inline_data=types.Blob(
                    mime_type="audio/wav",
                    data=audio_file.getvalue()
                )
                )
            #call gemini and generate content


    #catch if error occured and print error info
        except Exception as e:
            st.error(f"Error generating from audio: {e}")