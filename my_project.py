import pyttsx3
import os
import random
import time
import webbrowser

start = ["run","execute","start","open","running","opening","starting","executing"]
exit = ["exit" , "quit" , "terminate" , "stop" , "close" , "end","bye"]
dont = ["do not","don't","dont","nothing"]
complement = ["good","gud","great","grt","sweet","humble","cute","outstanding","amazing","awesome"]
web = ["music","song","comedy","dance","stand up","stand-up","sketch","search","brows","find"]
annoy = ["annoy","anger","bother","idiot","irritat","angry","bad","worst","appolog","arogent"]
start_statement = ["here we go", "sure, why not", "enjoy your thing", "yaa sure" , "okay then"]

pyttsx3.speak('welcome, what can i do for you...')

while True:
	print("Chat with me with your requirements : "  , end='')
	p = input().lower()
	
	
	if ("weather" in p) or ("temperature" in p) or ("climate" in p):
		webbrowser.open('http://www.google.com/search?btnG=1&q=weather')
		pyttsx3.speak("here's what i found for you")
	
	elif any(ele in p for ele in web):
		webbrowser.open('http://www.google.com/search?btnG=1&q=%s'%p)
		pyttsx3.speak("here's what i found for you")
	
	elif any(ele in p for ele in dont) :
		pyttsx3.speak("please don't play with me")
	
	elif not(any(ele in p for ele in dont)) and (("chrome" in p) or ("google" in p) or ("internet" in p)):
		pyttsx3.speak(random.choice(start_statement))	  
		os.system("chrome &")
	
	elif not(any(ele in p for ele in dont)) and (("mozilla" in p) or ("firefox" in p)) :
		pyttsx3.speak(random.choice(start_statement))
		os.system("firefox &")
	
	elif not(any(ele in p for ele in dont)) and (("microsoft" in p) and ("edge" in p)) :
		pyttsx3.speak(random.choice(start_statement))
		os.system("msedge &")
	
	elif not(any(ele in p for ele in dont)) and (("notepad" in p) or ("editor" in p)) :
		pyttsx3.speak(random.choice(start_statement))
		os.system("notepad &")
	
	elif not(any(ele in p for ele in dont)) and (("player" in p) and ("media" in p)):
		pyttsx3.speak(random.choice(start_statement))
		os.system("wmplayer &")
	
	elif not(any(ele in p for ele in dont)) and (("calculator" in p) or ("calc" in p)):
		pyttsx3.speak(random.choice(start_statement))
		os.system("calc &")
	
	elif not(any(ele in p for ele in dont)) and (("this pc" in p) or ("my computer" in p) or ("computer" in p) or ("pc" in p)):
		pyttsx3.speak(random.choice(start_statement))
		os.system("start shell:mycomputerfolder")
	
	elif not(any(ele in p for ele in dont)) and (("calendar" in p)):
		pyttsx3.speak(random.choice(start_statement))
		os.system("start outlookcal:")
	
	elif not(any(ele in p for ele in dont)) and (("message" in p) or ("chat" in p)):
		pyttsx3.speak(random.choice(start_statement))
		os.system("start ms-chat:")
	
	elif not(any(ele in p for ele in dont)) and (("help" in p)):
		pyttsx3.speak(random.choice(start_statement))
		os.system("start ms-contact-support:")
	
	elif not(any(ele in p for ele in dont)) and (("clock" in p) or ("alarm" in p)):
		pyttsx3.speak(random.choice(start_statement))
		os.system("start ms-clock:")
	
	elif not(any(ele in p for ele in dont)) and (("camera" in p)):
		pyttsx3.speak(random.choice(start_statement))
		os.system("start microsoft.windows.camera:")
	
	elif not(any(ele in p for ele in dont)) and (("picture" in p) or ("photo" in p)):
		pyttsx3.speak(random.choice(start_statement))
		os.system("start ms-photos:")
	
	elif not(any(ele in p for ele in dont)) and (("3d" in p) or ("paint" in p)):
		pyttsx3.speak(random.choice(start_statement))
		os.system("start ms-paint:")
	
	elif not(any(ele in p for ele in dont)) and (("paint" in p)):
		pyttsx3.speak(random.choice(start_statement))
		os.system("mspaint")
	
	elif not(any(ele in p for ele in dont)) and (("mail" in p)):
		pyttsx3.speak(random.choice(start_statement))
		os.system("start outlookmail:")
	
	elif ("time" in p) or ("date" in p):
		print(time.asctime(time.localtime()))
		pyttsx3.speak(time.asctime(time.localtime()))
	
	elif not(any(ele in p for ele in dont)) and (("control" in p)):
		pyttsx3.speak(random.choice(start_statement))
		os.system("control")
	
	elif not(any(ele in p for ele in dont)) and (("setting" in p)):
		pyttsx3.speak(random.choice(start_statement))
		os.system("start ms-settings:")
	
	elif not(any(ele in p for ele in dont)) and (("disk" in p)):
		pyttsx3.speak(random.choice(start_statement))
		os.system("start diskmgmt.msc")
		
	elif (p==""):
		pyttsx3.speak("sorry , but I Haven't received any input from you!!!")
	
	elif any(ele in p for ele in annoy):
		pyttsx3.speak("I'm sorry for that. i'll try my best")
	
	elif ("hello" in p) or ("hi" in p) or ("hey" in p):
		pyttsx3.speak("hello, i hope it's goning great")
	
	elif ("thank" in p):
		pyttsx3.speak("it's my pleasure")
	
	elif any(ele in p for ele in complement):
		pyttsx3.speak("thanks for the complement")
	
	elif  any(ele in p for ele in exit):
		pyttsx3.speak('okay, good bye')
		break
	
	else:
		webbrowser.open('http://www.google.com/search?btnG=1&q=%s'%p)
		pyttsx3.speak("here's what i found for you")
