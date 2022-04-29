from tokenize import String
import pyttsx3 as p

engine = p.init()

def say(words:String):
    engine.say(words)
    engine.runAndWait()