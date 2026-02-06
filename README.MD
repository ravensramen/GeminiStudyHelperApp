Everytime you open the terminal:
source venv/bin/activate

Make sure environmental variable/API key is set:
echo $GEMINI_API_KEY

sudo apt install python3-full python3-venv
python3 -m venv venv
source venv/bin/activate
pip install -U google-genai

//Trying Streamlit as the framework

streamlit run your_script.py [-- script args]
or 
python -m streamlit run your_script.py

//
Starting conceptually from scratch again, making a study app (turn voice into flash cards)