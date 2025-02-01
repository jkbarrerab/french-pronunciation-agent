import speech_recognition as sr
import pyttsx3
from googletrans import Translator
from difflib import SequenceMatcher

# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)  # Set slower speech rate

    # Get available voices
    voices = engine.getProperty('voices')
    
    # Try to find a French voice
    french_voice_found = False
    for voice in voices:
        if "fr" in voice.id or "French" in voice.name:  # Adjust for system-specific naming
            engine.setProperty('voice', voice.id)
            french_voice_found = True
            break
    
    if not french_voice_found:
        print("Warning: No French voice found! Using default voice.")
    
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
        speak("Bien joué! Votre prononciation est bonne.")
    else:  # If similarity is low, suggest improvement
        speak("Essayez encore. Votre prononciation peut être améliorée.")

# Main execution block
if __name__ == "__main__":
    reference_phrase = input("Enter the French phrase you want to practice: ")  # Get user input
    speak(f"Veuillez dire: {reference_phrase}")  # Prompt user with the phrase
    check_pronunciation(reference_phrase)  # Evaluate pronunciation
