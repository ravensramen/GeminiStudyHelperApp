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
st.title("Welcome, test out the newest Gemini Model")

#user inputs info to prompt
prompt = st.text_input("What would you like help with today?") #message displayed in text box

#Program response if button clicked
if st.button("Generate Response"):  
    if prompt: #If text_input received, pass prompt to gemini model
        with st.spinner("Generating response..."): #load spinning wheel
            try: #use try block in case API doesn't work
               
                response = client.models.generate_content( #call generate content function based on prompt
                    model="gemini-3-flash-preview",
                    contents=prompt
                )
                
                # Display the response
                st.success("Response: ")
                st.write(response.text) #write response from gemini response

                
            except Exception as e: #if gemini fails, run this block
                st.error(f"Error generating response: {str(e)}") #str(e) details error specs
    else:
        st.warning("Please enter a prompt first")