import datetime
import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import os
import pyautogui

#############################################################
from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
from pygame import mixer

mixer.init()

root = Tk()
root.geometry("1000x500")
root.eval('tk::PlaceWindow . center')

def play_gif():
    root.lift()
    root.attributes("-topmost", True)
    gif_path = "C:/Users/Divyesh/OneDrive/Desktop/ProjectFair/intro.gif"
    music_path = "C:/Users/Divyesh/OneDrive/Desktop/ProjectFair/music.mp3"

    lbl = Label(root)
    lbl.place(x=0, y=0)

    mixer.music.load(music_path)
    mixer.music.play()
    

    gif = Image.open(gif_path)

    for frame in ImageSequence.Iterator(gif):
        frame = frame.resize((1000, 500))
        frame = ImageTk.PhotoImage(frame)
        lbl.config(image=frame)
        root.update()
        time.sleep(0.05)

    root.destroy()
    mixer.music.pause()
    
play_gif()
root.mainloop()
#############################################################
###########################################################################
for i in range(3):
    a = input("Enter Password to open luna :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")
    
###########################################################################

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0,4)
    try:
        print("Understanding....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    
    except Exception as e:
        print("Say that again please....")
        return "None"
    
    return query


def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

if __name__ == "__main__":
    while True:
        query = takecommand().lower()
        if "wake up" in query or "hello luna" in query or "hey luna" in query:
            from greet import greetme
            greetme()
            
            while True:
                query = takecommand().lower()
                if "sleep" in query or "go to sleep" in query:
                    speak("Ok sir, Wake up when you need my help.")
                    break
                
                elif "tell me about you" in query or "who are you" in query:
                    speak("I am an proejct of A.I called luna. I use python version 3.11.7 64-bit andpython libraries. Project luna is build by CodeX. I'm an prototype not compelete project.")
                elif "hello luna" in query or "hi luna" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query or "i am good" in query:
                    speak("Sounds good.")
                    speak("How can i help you sir ?")
                elif "i am not fine" in query or "i am not well" in query:
                    speak("Ohh sounds so weird, what happened sir ?")
                elif "how you luna" in query or "how are you luna" in query:
                    speak("Wait i check my code... umm perfect , sir.")
                elif "thanks " in query or "thankyou" in query or "thank you" in query:
                    speak("It's my pleasure, sir.")
                elif "favorite music" in query :
                    speak("oh, i love all kinds of music! but if i had to pick one, Hope by xxxtentacion. How about you?")
                elif "hobbies" in query :
                    speak("oh, definitely! i love to assist people. How about you?")
                elif "what kind of movies you like" in query:
                    speak("I like sci-fi movies like Ironman and Avengers-Endgame. which kind movies you like to watch?")
                elif "google" in query:
                    from Online import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from Online import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from Online import WikipediaSearch
                    WikipediaSearch(query)
                    
                elif "weather" in query:
                    search = "weather in jamnagar"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                    
                elif "time" in query:
                    strtime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strtime}")
                    
                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")
                    
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    #a = "14 and 09 and 00"
                    print(a)
                    alarm(a)
                    speak("Done,sir")
                    
                elif "send email" in query or "email to" in query:
                    speak("Ok sir, Please enter the email address to send email")
                    recivermail = input("Enter Email:")
                    speak("Whats the subject of email:")
                    subject = input("Enter Subject:")
                    speak("Enter the message that sends to the email:")
                    message = input("Enter message:")
                    from Online import sendemail
                    sendemail(recivermail,subject,message)
                    
                    
                elif "calculate" in query:
                    from Calculatenumbers import Calc
                    Calc(query)
                
                
                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                            os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                            break
                elif "restart the system" in query:
                    speak("Ok sir.")
                    os.system("shutdown -r -t 0")
                
                elif "internet speed" in query:
                    from speed import speedI
                    speedI()

                elif "screenshot" in query:
                    ss = pyautogui.screenshot()
                    ss.save("ss.jpg")
                    
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.sleep(2)
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(6)
                    speak("SMILE")
                    pyautogui.sleep(4)
                    pyautogui.press("enter")
                
                elif "open" in query:
                    query = query.replace("open"," ")
                    query = query.replace("luna"," ")
                    pyautogui.press("super")
                    pyautogui.sleep(2)
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")
                
                elif "stop" in query or "pause" in  query or "play" in  query:
                    pyautogui.press("k")
                # elif "play" in query:
                #     pyautogui.press("k")
                elif "mute" in query or "unmute" in query:
                    pyautogui.press("m")
                elif "volumeup" in query or "volume up" in  query:
                    from Keyboard import volumeup
                    volumeup()
                elif "volumedown" in query or "volume down" in  query:
                    from Keyboard import volumedown
                    volumedown()
                    
                elif "open" in query:
                    from Apps import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Apps import closeappweb
                    closeappweb(query) 
                elif "turn off" in query or "terminate" in query or "good bye" in query:
                    speak("Good bye sir, take care of yourself.")
                    exit()
                    
                elif "remember that" in query:
                    r = query.replace("remember that ","")
                    r = query.replace("remember ","")
                    r = query.replace("luna ","")
                    speak("You told me to" + r)
                    remember = open("Remember.txt","w")
                    remember.write(r)
                    remember.close()
                
                elif "what you rememberk " in query or "what I told you to remember" in query:
                    remember  = open("Remember.txt","r")
                    speak("you told me " + remember.read())
                    
                elif "search" in query:
                    from Online import chatgpt
                    chatgpt(query)
                    query = query.replace("search","")
                    query = query.replace("search on","")
                    speak("Okay sir searching: " + query)
                    time.sleep(7)
            