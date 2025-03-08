''' 
Ensure that the Request Module is installed: python3 -m pip install requests
Ensure that the Flask Module is installed: python3 -m pip install flask
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
    This function receives the text from the HTML interface and 
    runs emotion detection using the emotion_detector() function.
    '''
    text_to_analyze = request.args.get("textToAnalyze", "").strip()

    # ✅ If the input is blank, immediately return an error message
    if not text_to_analyze:
        return "Invalid text! Please try again!", 400

    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)

    # ✅ If status_code = 500 (Server error), return an error message
    if result["status_code"] == 500:
        return "Error: Could not process request. Please try again later.", 500

    # ✅ If dominant_emotion is None, return an invalid text error
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!", 400

    # ✅ If successful, format the response
    formatted_response = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_response

@app.route("/")
def render_index_page():
    ''' This function renders the main application page '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
