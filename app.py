from flask import Flask, request, jsonify
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__)
CORS(app)  # This allows the JavaScript frontend to talk to this Python backend

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text', '')

    # The Logic: Analyze the text
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # Returns a number between -1 (Negative) and 1 (Positive)

    # Determine the "Vibe"
    if polarity > 0.1:
        vibe = "Positive 😊"
        color = "#d4edda" # Light Green
    elif polarity < -0.1:
        vibe = "Negative 😠"
        color = "#f8d7da" # Light Red
    else:
        vibe = "Neutral 😐"
        color = "#e2e3e5" # Grey

    return jsonify({
        'score': polarity,
        'vibe': vibe,
        'color': color
    })

if __name__ == '__main__':
    print("Starting Python Server on port 5000...")
    app.run(debug=True, port=5000)
