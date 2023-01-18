import pyttsx3 as tts
from termcolor import colored
import datetime
import webbrowser
import os
import random
import wikipedia as wk
from pyautogui import hotkey
import speech_recognition as sr
import re

tts.init('sapi5')
engine = tts.Engine()
available_voices = engine.getProperty('voices')
current_voice = engine.setProperty('voice', available_voices[1].id)

ai_name = 's five siri'
error = "Something Went Wrong"

opening_diloges = [
    "Got it Opening ",
    "I'm gonna open ",
    'okay opening',
    'opening',
]

quotes = [
    "Don’t develop friendship with the enemy of your friend; otherwise your friend will turn into an enemy." ,
    "It is easier to turn a mountain into dust than to create love in a heart that is filled with hatred." ,
    "When the people of truth remain quiet against falsehood, the people of falsehood start believing it is the truth." ,
    "There is no good in silence when it comes to knowledge, just as there is no good in speaking when it comes to ignorance." ,
    "He who is deserted by friends and relatives will often find help and sympathy from strangers." ,
    "The tongue is like a lion, if you let it loose, it will wound someone."
]

greet_dialoges = [
    "Hi, whats up",
    "Hello, whats up. How can i help you",
    "Hi, how are you",
    "Hello, welcome back",
    "Hi, how are you"
]

def say(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    say(random.choice(greet_dialoges))

def clr_print(text):
    print(colored(text, 'green'))

if __name__ == "__main__":

        # Conditions
        if "hello" in user_input:
            greet()
        
        elif "what is" in user_input:
            query = user_input.replace('what is ', "")
            say(f"searching for{query} in wekipedia")
            try:
                data = wk.summary(query, sentences=1)
                data = re.sub("\(.*?\)","()",data)
                say("according to wekipedia")
                print(data)
                say(data)
            except:
                say(error_message)
                clr_print(error_message)

        elif "time" in user_input:
            current_time = time.now().strftime("%H:%M:%S")
            clr_print(current_time)
            say(f"the time is {current_time}")
            
        elif "who is" in user_input:
            query = user_input.replace('who is ', "")
            say(f"searching for{query} in wekipedia")
            try:
                data = wk.summary(query, sentences=1)
                data = re.sub("\(.*?\)","()",data)
                say("according to wekipedia")
                print(data)
                say(data)
            except:
                say(error_message)
                clr_print(error_message)
        
        elif "define" in user_input:
            query = user_input.replace('define ',"")
            say(f"searching for{query} in wekipedia")
            try:
                data = wk.summary(query, sentences=1)
                data = re.sub("\(.*?\)","()",data)
                say("according to wekipedia")
                print(data)
                say(data)
            except:
                say(error_message)
                clr_print(error_message)

        elif "open youtube" in user_input:
            say(random.choice(opening_diloge + 'youtube'))
            webbrowser.open('https://www.youtube.com/')

        elif "open browser" in user_input:
            say(random.choice(opening_diloge + 'browser'))
            os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        elif ("open google") in user_input:
            say("Got it, Opening google")
            webbrowser.open('https://www.google.com/')

        elif "search for" in user_input:
            say("Okay lets search it")
            query = user_input.replace('search for ', "")
            query = query.replace(' in google', "")
            webbrowser.open_new_tab(f'https://www.google.com/search?q={query}')

        elif "open facebook" in user_input:
            say(random.choice(opening_diloge + 'facebook'))
            webbrowser.open('https://www.facebook.com/')

        elif "open vs code" in user_input:
            say(random.choice(opening_diloge + 'vs code'))
            os.startfile('"C:\\Users\\s5 Rafi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"')
        
        elif "quote" in user_input:
            quote = random.choice(quotes)
            print(quote)
            say(quote)

        elif 'song' in user_input:
            say(f"I am playing a song")
            try:
                os.startfile("D:\\Songs\\my song.mp4") # You can set here your own path
            except:
                say("I can't find the file")

        elif "youtube studio" in user_input:
            say(random.choice(opening_diloge + 'youtobe studio'))
            webbrowser.open('https://studio.youtube.com/')
        
        elif "who are you" in user_input:
            say(f"I am {ai_name} as an assistanse by s five sajid")

        elif "your name" in user_input:
            say(f"My name is {ai_name}")
        
        elif "screenshot" in user_input:
            hotkey('win','shift','s')

        elif "exit" in user_input or "shut up" in user_input or "bye" in user_input:
            say("Bye Bye Sir")
            exit()
        
        elif "fine" in user_input:
            if 'not' in user_input:
                say("May God Give Bliss You")
            else:
                say("Good Luck with that")
        
        elif "thank" in user_input:
            say("You are welcome")

        else:
            say("I can't got that")