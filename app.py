from flask import Flask, request, jsonify
import speech_recognition as sr
from gtts import gTTS
import os
from difflib import SequenceMatcher
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Function to convert text to speech
def speak(text):
    tts = gTTS(text=text, lang="fr")
    tts.save("output.mp3")
    return "output.mp3"

# Speech recognition from uploaded file
def recognize_speech(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language="fr-FR")
        return text
    except sr.UnknownValueError:
        return "Could not understand the speech"
    except sr.RequestError:
        return "Error with speech recognition service"

# Route to check pronunciation
@app.route("/check_pronunciation", methods=["POST"])
def check_pronunciation():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files["audio"]
    audio_path = "temp.wav"
    audio_file.save(audio_path)

    recognized_text = recognize_speech(audio_path)
    reference_text = request.form.get("reference_text", "")

    if not reference_text:
        return jsonify({"error": "No reference text provided"}), 400

    similarity = SequenceMatcher(None, reference_text.lower(), recognized_text.lower()).ratio()

    return jsonify({
        "expected": reference_text,
        "recognized": recognized_text,
        "similarity": round(similarity * 100, 2)
    }), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
