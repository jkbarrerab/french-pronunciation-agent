import speech_recognition as sr
import pyttsx3
import sys
from difflib import SequenceMatcher

# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)  # Set slower speech rate
    
    # Get available voices
    voices = engine.getProperty('voices')
    for voice in voices:
        if "fr" in voice.id or "French" in voice.name:  # Select a French voice
            engine.setProperty('voice', voice.id)
            break
    
    engine.say(text)
    engine.runAndWait()

# Function to recognize spoken French phrase
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak the French phrase:")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)  # Capture audio input
    try:
        text = recognizer.recognize_google(audio, language="fr-FR")  # Convert speech to text
        return text
    except sr.UnknownValueError:
        return "Could not understand the speech"  # Error when speech is not recognized
    except sr.RequestError:
        return "Error with speech recognition service"  # Error with the recognition service

# Function to check pronunciation similarity
def check_pronunciation(reference_text):
    spoken_text = recognize_speech()  # Get the recognized speech
    similarity = SequenceMatcher(None, reference_text.lower(), spoken_text.lower()).ratio()  # Compare texts
    print(f"Expected: {reference_text}")
    print(f"Recognized: {spoken_text}")
    print(f"Similarity: {similarity*100:.2f}%")  # Display similarity percentage
    
    if similarity > 0.8:  # If similarity is high, give positive feedback
        speak("Bien joué!")
    else:  # If similarity is low, suggest improvement
        speak("Essayez encore.")

# Main execution block
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py '<French phrase>'")
        sys.exit(1)
    
    reference_phrase = sys.argv[1]  # Get the French phrase from command line argument
    speak(f"Veuillez dire: {reference_phrase}")  # Prompt user with the phrase
    check_pronunciation(reference_phrase)  # Evaluate pronunciation
