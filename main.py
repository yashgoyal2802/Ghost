import pyttsx3
from datetime import datetime

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    now = datetime.now().strftime("%I:%M:%S")
    speak(now)
