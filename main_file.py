#VOICE ASSISTANCE CHATBOT

from neuralintents import GenericAssistant
from math import trunc
import time
import speech_recognition
import pyttsx3 as tts
import sys
import os
#from playsound import playsound


recognizer=speech_recognition.Recognizer()
speaker=tts.__init__(self=True)
speaker.setProperty('rate',150)     #speed in which bot talks # dont change this bro
#todo_list=['Go Shopping', 'Clean Room', 'Record Video']
todo_list=[]


from string_calls import bigString
from string_calls import qq22 
from string_calls import sssq
bigString()

#os.system('python /Users/Skanda/Desktop/VAC/string_calls.py')

speaker.say(qq22)
speaker.runAndWait()
#playsound('/Users/Skanda/Desktop/Ri_VAC/StringAud/listen.wav')






def create_note():
    global recognizer
    sCreate="What do you want to write on your note?"
    
    speaker.say(sCreate)
    speaker.runAndWait()
   # playsound('/Users/Skanda/Desktop/Ri_VAC/StringAud/listen.wav')

    done=False         #coz if u dont say anything, it should repeat in loop na so.  it goes to exception

    while not done:
        try:

            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio=recognizer.listen(mic)
                note=recognizer.recognize_google(audio)    #make audio to text
                note=note.lower()

                speaker.say("Choose a filename!")
                speaker.runAndWait()
                #playsound('/Users/Skanda/Desktop/Ri_VAC/StringAud/listen.wav')

                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio=recognizer.listen(mic)
                filename=recognizer.recognize_google(audio)
                filename=filename.lower()

            with open(f"{filename}.txt",'a') as f:
                f.write(note+"\n")
                done=True
                speaker.say("I successfully created note")
                speaker.runAndWait()
               # playsound('/Users/Skanda/Desktop/Ri_VAC/StringAud/listen.wav')

        except speech_recognition.UnknownValueError:
            recognizer=speech_recognition.Recognizer()
            speaker.say("It went above my head. Please try again...:(")
            speaker.runAndWait()
            #playsound('/Users/Skanda/Desktop/Ri_VAC/StringAud/listen.wav')




def add_todo():
    global recognizer
    sAddtodo="What do you want to add?"
    speaker.say(sAddtodo)
    speaker.runAndWait()
   # playsound('/Users/Skanda/Desktop/Ri_VAC/StringAud/listen.wav')

    done=False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio=recognizer.listen(mic)
                item=recognizer.recognize_google(audio)
                item=item.lower()
                todo_list.append(item)
                ffFile=sssq+" TODO"
            with open(f"{ffFile}.txt",'a') as f:
                f.write(item+"\n")
                done=True


                

                speaker.say("i added item to to do list")
                speaker.runAndWait()
                #playsound('/Users/Skanda/Desktop/Ri_VAC/StringAud/listen.wav')
        except speech_recognition.UnknownValueError:
            recognizer=speech_recognition.Recognizer()
            speaker.say("It went above my head. Please try again...:(")
            speaker.runAndWait()
            #playsound('/Users/Skanda/Desktop/Ri_VAC/StringAud/listen.wav')







def show_todo():
    speaker.say("These are the items in your to do list")
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()
    #playsound('/Users/Skanda/Desktop/Ri_VAC/StringAud/listen.wav')


def hello():
    sHello="Hello. What can i do for you?"
    speaker.say(sHello)
    speaker.runAndWait()
    #playsound('/Users/Skanda/Desktop/Ri_VAC/StringAud/listen.wav')


def quit():
    sQuit="Bye! See you soon"
    speaker.say(sQuit)
    speaker.runAndWait()
    #playsound('/Users/Skanda/Desktop/Ri_VAC/StringAud/end.wav')
    sys.exit(0)















    
mappings={
    "greeting": hello,
    "create_note":create_note,
    "add_todo":add_todo,
    "show_todo":show_todo,
    "exit":quit
}

assistant=GenericAssistant('/Users/Skanda/Desktop/Ri_VAC/intents.json',intent_methods=mappings)

assistant.load_model()           #---------> it loads already trained model which is present in the folder
#assistant.train_model()         #---------> this u need to use if u make changes in intent file, so that u can re train the model again
#assistant.save_model()             #-----> saves model

while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic,duration=0.2)
            audio=recognizer.listen(mic)
            message=recognizer.recognize_google(audio)
            message=message.lower()
        

        assistant.request(message)   #selects mapping
    

    except speech_recognition.UnknownValueError:
        recognizer=speech_recognition.Recognizer()   #does nothing if it doesnt understand