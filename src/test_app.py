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

#test audio features of gemini
audio_file = st.audio_input("Input a recording")

#Program response if button clicked
if st.button("Generate Response"):  
    if audio_file: #If audio received, pass prompt to gemini model
        with st.spinner("Generating response..."): #load spinning wheel
            try: #use try block in case API doesn't work
               
                # Convert audio bytes to Part object with mime type
                audio_part = types.Part(
                    inline_data=types.Blob(
                        mime_type="audio/wav",
                        data=audio_file.getvalue()
                    )
                )
                
                response = client.models.generate_content( #call generate content function based on prompt
                    model="gemini-3-flash-preview",
                    contents=[audio_part],
                    config=types.GenerateContentConfig(
                        thinking_config=types.ThinkingConfig(
                            thinking_level=types.ThinkingLevel.HIGH
                        )
                    )
                )

                #testing image generation with gemini based on audio description
                image_prompt = response.text  # Use audio description as image prompt
                response2 = client.models.generate_content(
                    model="gemini-3-pro-image-preview",
                    contents=[image_prompt]
                )

                
                # display the response of audio prompt
                st.success("Response: ")
                st.write(response.text) #write response from gemini response

                #display generated image
                if response2.candidates[0].content.parts:
                    image_data = response2.candidates[0].content.parts[0].inline_data.data
                    st.image(image_data, caption="Generated Image from Audio")

            except Exception as e: #if any ai model fails, run this block
                st.error(f"Error generating response: {str(e)}") #str(e) details error specs
    else:
        st.warning("Please enter a prompt first")