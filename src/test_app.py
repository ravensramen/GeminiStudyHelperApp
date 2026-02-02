import streamlit as st
from google import genai

from google.genai import types
from PIL import Image

import io

#loads my API key from the streamlit framework
api_key = st.secrets["GEMINI_API_KEY"]

#initialize client with API key
client = genai.Client(api_key=api_key)

#title of streamlit site
st.title("Welcome to Image Generator")

#text box prompt
prompt = st.text_input("Enter an image prompt")

#testing button 
if st.button("Click me"):
    st.write("Somethiing was clicked")