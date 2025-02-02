from flask import Flask, request, jsonify
import speech_recognition as sr
# import pyttsx3
from gtts import gTTS
import os

from difflib import SequenceMatcher
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Allow frontend requests

# Initialize text-to-speech engine
def speak(text):
    tts = gTTS(text=text, lang="fr")
    tts.save("output.mp3")
    os.system("mpg321 output.mp3")  # Use ffplay or any available media player

# def speak(text):
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 125)  # Set slower speech rate

#     # Select a French voice
#     voices = engine.getProperty('voices')
#     for voice in voices:
#         if "fr" in voice.id or "French" in voice.name:
#             engine.setProperty('voice', voice.id)
#             break

#     engine.say(text)
#     engine.runAndWait()

# Speech recognition function
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="fr-FR")
        return text
    except sr.UnknownValueError:
        return "Could not understand the speech"
    except sr.RequestError:
        return "Error with speech recognition service"

@app.route("/")
def home():
    return "French Pronunciation API is running!"

@app.route("/speak", methods=["POST"])
def generate_speech():
    data = request.json
    phrase = data.get("phrase", "")

    if not phrase:
        return jsonify({"error": "No phrase provided"}), 400

    speak(phrase)
    return jsonify({"message": "Speech played successfully"}), 200

@app.route("/check_pronunciation", methods=["POST"])
def check_pronunciation():
    data = request.json
    reference_text = data.get("reference_text", "")

    if not reference_text:
        return jsonify({"error": "No reference text provided"}), 400

    spoken_text = recognize_speech()
    similarity = SequenceMatcher(None, reference_text.lower(), spoken_text.lower()).ratio()

    return jsonify({
        "expected": reference_text,
        "recognized": spoken_text,
        "similarity": round(similarity * 100, 2)
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
