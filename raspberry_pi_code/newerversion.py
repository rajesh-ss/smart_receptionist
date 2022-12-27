'''
************************************************
________________________________________________
Contributers: Rajesh S, Nikhil M, Harshitha JP
Purpose: Basic text to speech and speech to text, 
         Communicate with ec2 where ML model will
         be running.
__________________________________________________

**************************************************
'''



'''
Importing essential libraries.
___________________________________________________________________

1. speech_recognition -> For speech to text convertion. Google API
2. pyttsx3 -> For text to speech convertion
3. Datetime -> For wishing user based on the timw of the day
___________________________________________________________________
'''
import speech_recognition as sr
import pyttsx3
import datetime
import os
import shutil
import nltk

from nltk.chat.util import Chat, reflections

import requests
import json
import face_detect
import cv2
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Servo
import time
import os
import demo
import subprocess
import mcarr_firebase

'''
____________________________________________________________________
--> Configuring specific voice, rate, volume of the speech (pyttsx3)
____________________________________________________________________
'''
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')

#____________________________________________________________________

engine.setProperty('rate', rate-25)
engine.setProperty('voice', voices[13].id)
engine.setProperty('volume', volume+0.5)


'''
____________________________________________________________________
--> Speech to text convertion with the specified properties. 
____________________________________________________________________
'''

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


'''
______________________________________________________
This Function listens to the user's speech and 
returns the corresponding text.

User can use different speech to text converter, 
available options are:
1. 
______________________________________________________
'''
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        #audio = r.listen(source, phrase_time_limit=5)
        #listens for specified seconds.
        audio = r.listen(source, 4, 4)
        
        try:
            print("Recognizing...")
            # google recognizer
            query = r.recognize_google(audio, language ='en-in')
            print(f"User said: {query}\n")
        
        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
            speak("Unable to Recognize your voice.")
            return "no recognition"

    return query

# speak(takeCommand())

'''
___________________________________________________________
Wishing the user based on the time
___________________________________________________________
'''

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir or Mam !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir or Mam !")

	else:
		speak("Good Evening Sir or Mam!")

	assname =("Robo receptionist 1 point o")
	speak("I am your Assistant")
	speak(assname)

# wishMe()

def username():
	speak("What should i call you as")
	uname = takeCommand()
	speak("Welcome user")
	speak(uname)
	columns = shutil.get_terminal_size().columns

	print("#####################".center(columns))
	print("########Welcome ", uname.center(columns))
	print("#####################".center(columns))

	speak("How can i Help you, sir or mam")

count = 0
interation = 0
cntQueries = 0

def chat():
    #print("Hi! I am a robo receptionist created by IOT group")
    #chat = Chat(pairs, reflections)
    #chat.converse('hola')
    global count
    global interation
    global cntQueries
    
    query = takeCommand()
    
    
    if query == "no recognition":
        count = count+1
        print("::--==__"+str(count))
        return
    
    
    
    elif query == "thank you":
        
        speak("Give us some feed back for improving the system   ")
        query = takeCommand()
        mcarr_firebase.mcarrAddFeedback(query)
        count=5
        return
        #main()
        
    count = 0
    
    response_API = requests.get('http://ec2-3-235-138-80.compute-1.amazonaws.com/reply/'+query)
    print(response_API.status_code)
    data = response_API.text
    print(data)
    speak(data)
    
    if data!= "null":
        interation = interation+1
    elif data=="null":
        print("Adding unanswered to firebase")
        mcarr_firebase.mcarrAddUnansweredQuery(query)
        
    #print(chat.converse("hello"))
    

'''
___________________________________________________________

___________________________________________________________
'''

if __name__ == '__main__':
    
    while True:
    
    
        #clear = lambda: os.system('cls')
        #clear()
        count = 0
        print("test1")
        
        face_detect.runface()
        print("test2")
    
        print("Face detected, robo receptionist can start")
            
        wishMe()
        username()

        while True:
            print("Inside true of while loop: "+str(count))
            cntQueries = cntQueries+1
            if count>4:
                break
            
            chat()

        mcarr_firebase.mcarrAddInteraction(cntQueries, interation)




'''
______________________________________________________________
______________________________________________________________
'''

