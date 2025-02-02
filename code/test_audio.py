from gtts import gTTS
from pydub import AudioSegment

# Generate speech in French
tts = gTTS("Bonjour", lang="fr")
tts.save("test_audio.mp3")

# Convert MP3 to WAV (Flask requires WAV)
audio = AudioSegment.from_mp3("test_audio.mp3")
audio.export("test_audio.wav", format="wav")

print("test_audio.wav generated successfully!")
