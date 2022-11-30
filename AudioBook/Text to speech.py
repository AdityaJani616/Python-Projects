#pyttsx3 is an external library in python which is used to convert text to speech 

import pyttsx3,time

book=open(r"quotes.txt")

book_text=book.readlines()

engine=pyttsx3.init()

for i in book_text:
    engine.say(i)
    time.sleep(2)  #This will generate a delay of 2 seconds in reading a new line 
    engine.runAndWait()

book.close() # not compulsion but always a good practice