#!python2

# -*- coding: utf-8 -*-

import Speech_Recognition as sr
import urllib3
import webbrowser
import pyttsx3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class SARVIS:
    def listener(self,recognizer, microphone):
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, phrase_time_limit=4)
            command = recognizer.recognize_google(audio, language="en-US")
            return command

    def sarvis(self,command):
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        voices = engine.getProperty('voices')
        engine.setProperty("rate", 130)
        sarviss = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        engine.setProperty('voice', sarviss)
        engine.say(command)
        engine.runAndWait()

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

s = SARVIS()
#rec = s.listener(recognizer, microphone)  Saves what you've said
#S.sarvis("What you've said "+rec) Reads the strings inside it.Here, it reads "What you've said" part first, then reads rec variable.

print("***************SARVIS V1.0***************")

while True:
    try:
        print("Listening boss...")
        rec = s.listener(recognizer, microphone) #Listens you and saves it to rec variable.For example you've said "Reddit", rec becomes "Reddit".
        print(rec)#Prints rec variable.
        if "search" in rec:#Looks for "search" string in rec variable.
            s.sarvis("Google is opening...")#Reads lout the string inside parantheses.
            webbrowser.open_new_tab("https://www.google.com/")
        elif "Reddit" in rec:#Looks for "Reddit" string in rec variable.
            s.sarvis("Reddit is opening...")#Reads lout the string inside parantheses.
            webbrowser.open_new_tab("https://www.reddit.com/")
    except sr.UnknownValueError:
        s.sarvis("Boss, I couldn't understand you.Say it again.")#Reads lout the string inside parantheses.
