# Emotion Detection Web Application

## Overview
This project is a Flask-based web application that analyzes emotions in user-provided text using IBM Watson Natural Language Processing (NLP) services.  
It detects five emotions — **anger, disgust, fear, joy, and sadness** — and identifies the dominant emotion based on confidence scores.

The application demonstrates third-party API integration, backend request handling, and basic test-driven validation.

---

## Features
- **Real-time emotion analysis** of input text via a web interface  
- **Dominant emotion identification** based on highest confidence score  
- **Error handling** for empty inputs and invalid requests (HTTP 400)  
- **Unit testing** to validate emotion classification logic across sample inputs  

---

## Project Structure
emotion-detector/
├── server.py
├── EmotionDetection/
│ ├── init.py
│ ├── emotion_detection.py
│ └── requirements.txt
├── static/
│ └── mywebscript.js
├── templates/
│ └── index.html
├── test_emotion_detection.py
├── LICENSE
└── README.md


---

## Key Components
- **server.py**  
  Flask application entry point. Handles routing and HTTP requests.

- **EmotionDetection/emotion_detection.py**  
  Core logic for invoking the IBM Watson NLP API and parsing emotion scores.

- **static/mywebscript.js**  
  Client-side JavaScript for asynchronous requests and dynamic UI updates.

- **templates/index.html**  
  Web interface built using Bootstrap.

- **test_emotion_detection.py**  
  Unit tests validating expected emotion outputs for known inputs.

---

## Installation

### Prerequisites
- Python 3.x
- IBM Watson NLP API credentials

### Clone the Repository
```bash
git clone https://github.com/KruBro/emotion-detector.git
cd emotion-detector

Install Dependencies
pip install -r EmotionDetection/requirements.txt
Usage
Start the Flask Server
python3 server.py
The application will be available at:
http://0.0.0.0:5000
Analyze Text

Open the application in a web browser.

Enter text (example: I am glad this happened).

Click Run Sentiment Analysis.

View emotion scores and the detected dominant emotion.

Running Unit Tests

To verify that emotion detection behaves as expected:
python3 test_emotion_detection.py
The test suite includes cases such as:

Detecting joy for positive statements

Detecting anger for negative or aggressive statements

License

This project is licensed under the Apache License 2.0.
See the LICENSE file for full details.
