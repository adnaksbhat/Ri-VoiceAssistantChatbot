# 'Ri'-Voice-Assistant-Chatbot
Voice Assistant Chatbot. Python speech recognition and task handling project.
_____________________________________________________________________________
_____________________________________________________________________________
-> import libraries speechrecognition, pyttsx3, neuralintents.
   pyttsx3 is used to convert text to speech (tts)
   
-> intents.json contains tags or categories, has patterns and responses.
   currently used tags are, hello, exit, create_note, add_todo, show_todo
->recognize_google() function is used to take user audio and is converted to text

-> for each identified mappings, respective functions are called.

-> create_note() function takes user voice commands to create a file where filename and its contents are provided by the user.

-> show_todo() function reads out contents of the file



















