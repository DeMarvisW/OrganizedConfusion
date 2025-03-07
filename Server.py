'''
Executing this function initiates the application of emotion
analysis to be executed over the Flask channel and deployed on
localhost:5000.
'''

from flask import Flask, render_template, request  # Import Flask modules
from emotion_detection import emotion_detector  # Import function

# Initiate the Flask app
app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_api():
    '''
    This code receives the text from the HTML interface and 
    runs emotion detection over it using emotion_detector()
    function. The output returned shows the label and its confidence 
    score for the provided text.
    '''
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze:
        return "Error: No text provided. Please enter a text input."

    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)

    # Format the response as required
    formatted_response = f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."

    return formatted_response

@app.route("/")
def render_index_page():
    '''
    This function initiates the rendering of the main application
    page over the Flask channel.
    '''
    return render_template("index.html")

if __name__ == "__main__":
    '''
    This function executes the flask app and deploys it on localhost:5000
    '''
    app.run(debug=True)
