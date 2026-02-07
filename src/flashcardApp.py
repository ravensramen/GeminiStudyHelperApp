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
st.title("Voice → Study Notes")

#write main program prompt
st.write("Talk about what you learned in lecture today, Gemini can turn it into structured"
" notes and flashcards that you can study with!"
)

#take in audio file from user
audio_file = st.audio_input("Record what you learned today:")


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
                response = client.models.generate_content(
                    model="gemini-3-flash-preview",
                    contents=[
                        audio_part,
                        "Turn audio spoken into clear study notes and flashcards"
                    ],
                    config=types.GenerateContentConfig(
                        thinking_config=types.ThinkingConfig(
                            thinking_level=types.ThinkingLevel.HIGH
                        ),
                        response_mime_type="application/json",
                        response_schema={
                            "type": "object",
                            "properties": {
                                "title": {"type": "string"},
                                "summary": {"type": "string"},
                                "key_points": {
                                    "type": "array",
                                    "items": {"type": "string"}
                                },
                                "flashcards": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "question": {"type": "string"},
                                            "answer": {"type": "string"}
                                        },
                                        "required": ["question", "answer"]
                                    }
                                }
                            },
                            "required": ["title", "summary", "key_points", "flashcards"]
                        }
                    )
                )

                #parse gemini response 
                raw_text = response.candidates[0].content.parts[0].text
                data = json.loads(raw_text)

                # display results
                st.success("Here are your notes: ")
                st.header(data["title"])
                st.write(data["summary"])

                st.subheader("Key Points")
                for point in data["key_points"]: #iterate through extracted list
                    st.markdown(f"- {point}")

                st.subheader("Flashcards")
                for card in data["flashcards"]: #allow user to expand or collapse to view answer
                    with st.expander(card["question"]):
                        st.write(card["answer"])

                #export notes
                export_text = f"{data['title']}\n\n"
                export_text += "Key Points\n"
                for p in data["key_points"]: #append each key point in the export file
                    export_text += f"- {p}\n" #organized as bullet points
                
                export_text += "\nFlashcards\n"
                for c in data["flashcards"]: #iterate through each flashcard in the set, append to export file
                    export_text += f"Q: {c['question']}\nA: {c['answer']}\n\n"
                
                st.download_button( #download button
                    label="Download my Notes",
                    data=export_text,
                    file_name="my_study_notes.txt",
                    mime="text/plain"
                )

            #catch if error occured and print error info
            except Exception as e:
                st.error(f"Error generating from audio: {e}")