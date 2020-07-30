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


def wishme():
    speak("Welcome Back Sir!")
    speak("Its")
    time()
    speak("and today is")
    date()
    hour = datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    speak("This is GHOST, How may I help you ?")
