import requests
import json

def emotion_detector(text_to_analyse):
    # Handle blank input
    if not text_to_analyse.strip():
        return {"error": "Invalid text! Please try again!"}

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyse}}
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    try:
        response = requests.post(url, json=myobj, headers=headers)
        response.raise_for_status()  # Ensure we catch HTTP errors

        formatted_response = response.json()

        # Extract emotions safely
        emotions = formatted_response.get("emotionPredictions", [{}])[0].get("emotion", {})

        # Default to 0 if emotion values are missing
        anger = emotions.get('anger', 0)
        disgust = emotions.get('disgust', 0)
        fear = emotions.get('fear', 0)
        joy = emotions.get('joy', 0)
        sadness = emotions.get('sadness', 0)

        # Determine the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get, default=None)

        # Handle case where dominant_emotion is None
        if dominant_emotion is None:
            return {"error": "Invalid text! Please try again!"}

        # Ensure output format matches the requirement
        result = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }

        return result

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
