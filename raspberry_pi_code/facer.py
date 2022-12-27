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
		audio = r.listen(source, 10, 10)

	try:
		print("Recognizing...")
        # google recognizer
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"

	return query

# speak(takeCommand())

'''
___________________________________________________________

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

'''
___________________________________________________________

___________________________________________________________
'''

if __name__ == '__main__':
	clear = lambda: os.system('cls')

	# This Function will clean any
	# command before execution of this python file
	clear()
	wishMe()
	username()