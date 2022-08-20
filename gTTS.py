from cgi import test
from gtts import gTTS
import os
import playsound

# speak text
def speak(text):
    tts = gTTS(text=text, lang="bn")

    filename = "test.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


speak("Hey, There How are you?")
