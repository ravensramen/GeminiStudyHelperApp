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
prompt = st.text_input("Enter a prompt")

#testing button 
if st.button("Generate Response"):
    if prompt:
        with st.spinner("Generating response..."):
            try:
                # Call Gemini 3 API
                response = client.models.generate_content(
                    model="gemini-3-5-sonnet",
                    contents=prompt
                )
                
                # Display the response
                st.success("Response generated!")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error generating response: {str(e)}")
    else:
        st.warning("Please enter a prompt first")