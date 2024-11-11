from flask import Flask, request, jsonify
from flask_cors import CORS 
from textblob import TextBlob

app = Flask(__name__)
CORS(app)  


def detect_emotion(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.5:
        emotion = "Happy"
    elif polarity > 0:
        emotion = "Positive"
    elif polarity == 0:
        emotion = "Neutral"
    elif polarity < -0.5:
        emotion = "Sad"
    else:
        emotion = "Negative"

    return emotion

@app.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.get_json()
    text = data.get("text", "")
    emotion = detect_emotion(text)
    
    response = {
        "text": text,
        "emotion": emotion
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)




































# made by Siddhartha Bharali