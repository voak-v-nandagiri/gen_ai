from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Voak Generative AI Tool - Landing Page</h1>"
