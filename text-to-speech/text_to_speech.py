# The above code is reading the text from the file and converting it into speech.
from gtts import gTTS 
import os
file = open("/text-to-speech/abc.txt", "r").read()

speech = gTTS(text=file, lang='en', slow=False)
speech.save("/text-to-speech/voice.mp3")
os.system("/text-to-speech/voice.mp3")