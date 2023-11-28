from gtts import gTTS
import os

# Text to be converted to speech
text = "Das ist eine Text to Speech Nachricht"

# Language in which you want to convert
language = 'de'

# Passing the text and language to the engine slow=False makes the speech faster
tts = gTTS(text=text, lang=language, slow=False)

# Save the converted audio to a file
tts.save("output.mp3")

# Play the audio file
os.system("start output.mp3")
