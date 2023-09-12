# pip install pyttsx3
import pyttsx3
e = pyttsx3.init()
e.say(input("Enter your Text: "))
e.runAndWait()