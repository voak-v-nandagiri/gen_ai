#import streamlit as st
#from gradio_client import Client

#from flask import Flask
#app = Flask(__name__)

#@app.route("/")
#def index():
#    return "<h1>Voak Generative AI Tool - Landing Page</h1>"

import streamlit as st
from transformers import pipeline

pipe = pipeline('sentiment-analysis')

text = st.text_area('Enter some text for sentiment analysis')

if text:
    out = pipe(text)
    st.json(out)
