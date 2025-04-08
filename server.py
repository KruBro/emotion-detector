"""Flask app to perform emotion detection on user-submitted text."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_detector():
    """Route for detecting emotions in submitted text."""
    text_to_detect = request.args.get('textToAnalyze')

    if not text_to_detect:
        return "Invalid text! Please try again."

    response = emotion_detector(text_to_detect)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """Render the main web page."""
    return render_template('index.html')

def main():
    """Run the Flask app."""
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    main()
