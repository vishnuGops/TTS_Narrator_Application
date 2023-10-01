from gtts import gTTS

# Input text
text = "This is the text you want to convert to speech."

# Create a gTTS object
tts = gTTS(text=text, lang='en')  # You can specify the language (e.g., 'en' for English)

# Save the speech as an MP3 file
tts.save("narration.mp3")

print("Speech saved as 'narration.mp3'")
