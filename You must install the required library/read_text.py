# pip install pyttsx3
import pyttsx3

e = pyttsx3.init()
e.setProperty('rate', 110)
def read(x):
    e.say(x)
    e.runAndWait()

read(input("Enter your text: "))