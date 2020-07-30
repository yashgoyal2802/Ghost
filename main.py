import pyttsx3
from datetime import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    now = datetime.now().strftime("%I:%M:%S")
    speak("Its")
    speak(now)


def date():
    year = int(datetime.now().year)
    month = int(datetime.now().month)
    date = int(datetime.now().day)
    speak("Today is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome Back Sir!")
    time()
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


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language="en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that Agai please")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("abc@gmail.com", "123")
    server.sendmail("abc@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("Searching Sir...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif "search in chrome" in query:
            speak("What should i search sir ?")

        elif "send email" in query:
            try:
                speak("What should I say ?")
                content = takeCommand()
                to = "xyz@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send teh Email")

        elif 'offline' in query:
            quit()
