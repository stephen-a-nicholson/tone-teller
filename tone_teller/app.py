"""
A Flask application for performing sentiment analysis on text.
This module sets up a web server that allows users to input text through a web interface
and receive sentiment analysis results in real-time using a pre-trained NLP model from Hugging Face.
"""

from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

nlp = pipeline("sentiment-analysis")


@app.route("/")
def index():
    """
    Serve the main index page from a predefined HTML template.

    Returns:
        Rendered HTML template (index.html) for the main page.
    """
    return render_template("index.html")


@app.route("/analyse", methods=["POST"])
def analyse():
    """
    Analyse the sentiment of the text received in a JSON request.

    The function expects a JSON object with a key 'text' containing the string to be analyzed.
    It uses the preloaded NLP model to perform sentiment analysis and returns the result.

    Returns:
        JSON response containing the sentiment analysis result.
    """
    data = request.get_json()
    text = data["text"]
    result = nlp(text)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
