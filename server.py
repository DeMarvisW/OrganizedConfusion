"""
Executing this function initiates the application of sentiment
analysis to be executed over the Flask channel and deployed on
localhost:5000.
"""

# Import necessary modules from Flask framework
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# Initiate the Flask app
app = Flask("Sentiment Analyzer")


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """
    Retrieve the text input from the request arguments, 
    analyze its sentiment, and return the sentiment label and score.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Handle case where no text is provided
    if not text_to_analyze:
        return "Invalid input! No text provided. Try again."

    response = sentiment_analyzer(text_to_analyze)
    label = response.get('label')  # Use .get() to prevent KeyError
    score = response.get('score')

    # Handle cases where sentiment analysis fails or returns None
    if label is None or score is None:
        return "Invalid input! Sentiment analysis failed. Try again."

    # Return sentiment label and score using f-string formatting
    return f"The given text has been identified as {label.split('_')[1]} with a score of {score}."


@app.route("/")
def render_index_page():
    """
    Render the index.html page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
