import pyttsx3

artie = pyttsx3.init()

def artie_says(phrase):
    artie.say(phrase)
    artie.runAndWait()

