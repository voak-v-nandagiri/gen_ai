import streamlit as st
from gradio_client import Client

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Voak Generative AI Tool - Landing Page</h1>"



# Constants
TITLE = "Voak Generative AI Tool - Landing Page"
DESCRIPTION = """
Intro text here.
"""

# Initialize client
with st.sidebar:
    # system_promptSide = st.text_input("Optional system prompt:")
    temperatureSide = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.9, step=0.05)
    max_new_tokensSide = st.slider("Max new tokens", min_value=0.0, max_value=4096.0, value=4096.0, step=64.0)
    # ToppSide = st.slider("Top-p (nucleus sampling)", min_value=0.0, max_value=1.0, value=0.6, step=0.05)
    # RepetitionpenaltySide = st.slider("Repetition penalty", min_value=0.0, max_value=2.0, value=1.2, step=0.05)


# Streamlit UI
st.title(TITLE)
st.write(DESCRIPTION)


if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar=("🧑‍💻" if message["role"] == 'human' else '🦙')):
        st.markdown(message["content"])

