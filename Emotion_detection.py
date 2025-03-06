import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = {"raw_document": {"text": text_to_analyse}}

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    try:
        # Sending a POST request to the emotion analysis API
        response = requests.post(url, json=myobj, headers=headers)
        response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx

        # Parsing the JSON response
        formatted_response = response.json()

        # Extracting emotion scores from the response
        emotions = formatted_response.get("emotionPredictions", [{}])[0].get("emotion", {})

        # Ensure all emotions are included and set missing values to 0
        result = {
            'anger': emotions.get('anger', 0),
            'disgust': emotions.get('disgust', 0),
            'fear': emotions.get('fear', 0),
            'joy': emotions.get('joy', 0),
            'sadness': emotions.get('sadness', 0),
            'dominant_emotion': max(emotions, key=emotions.get, default='unknown')  # Get the emotion with the highest score
        }

        return result

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
