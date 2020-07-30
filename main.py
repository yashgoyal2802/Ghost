import pyttsx3
from datetime import datetime

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    now = datetime.now().strftime("%I:%M:%S")
    speak(now)


def date():
    year = int(datetime.now().year)
    month = int(datetime.now().month)
    date = int(datetime.now().day)
    speak(date)
    speak(month)
    speak(year)
