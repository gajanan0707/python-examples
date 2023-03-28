# The above code is reading the text from the file and converting it into speech.

'''
This is a Python code that uses the "gtts" library to convert text from a file to an audio file (mp3 format) using Google's Text-to-Speech API.
The code opens a text file named "abc.txt" in read mode and reads the content of the file using the "read()" method.
Then, the "gTTS" function is called with the text content, language ("en" for English), and "slow" flag set to "False" for normal speech speed. The output is saved to an audio file named "voice.mp3" in the "text-to-speech" directory.
Finally, the "os" library is used to play the audio file using the "system" method, which executes a command in the shell (in this case, playing the mp3 file).
'''
from gtts import gTTS
import os
file = open("/text-to-speech/abc.txt", "r").read()

speech = gTTS(text=file, lang='en', slow=False)
speech.save("/text-to-speech/voice.mp3")
os.system("/text-to-speech/voice.mp3")
