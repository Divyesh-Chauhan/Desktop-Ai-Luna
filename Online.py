import pyttsx3
import speech_recognition as sr
import pywhatkit
import webbrowser
from email.message import EmailMessage
import smtplib
import pyautogui
Email = "djdivyeshchauhan@gmail.com"
Password = "uunkjefgyhjcqcwl"

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
        print(f"You Said:", query)
    
    except Exception as e:
        print("Say that again please....")
        return "None"
    
    return query

query = takecommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googlescrap
        query = query.replace("nova","")
        query = query.replace("google search","")
        query = query.replace("search","")
        query = query.replace("google","")
        query = query.replace("Google","")
        speak("This is what found on Google")
        
        try:
            pywhatkit.search(query)
            result = googlescrap.summary(query,1)
            speak(result)
        
        except:
            speak("No speakable output found")

def searchYoutube(query):
            if "youtube" in query:
                speak("This is what i found on youtube!")
                query = query.replace("luna","")
                query = query.replace("search on youtube","")
                query = query.replace("youtube","")
                query = query.replace("Youtube","")
                web = "https://www.youtube.com/results?search_query=" + query
                webbrowser.open(web)
                pywhatkit.playonyt(query)
                speak("Done, sir")

def WikipediaSearch(query):
        if "wikipedia" in query:
            speak("This is what i found on wikipedia!")
            query = query.replace("luna","")
            query = query.replace("search on wikipedia","")
            query = query.replace("wikipedia","")
            query = query.replace("Wikipedia","")
            web = "https://en.wikipedia.org/wiki/" + query
            webbrowser.open(web)
def chatgpt(query):
        if "search" in query or "openai" in query or "search on openai" in query:
            query = query.replace("luna","")
            query = query.replace("search on openai","")
            query = query.replace("search","")
            query = query.replace("search on ","")
            query = query.replace("search on Openai","")
            query = query.replace("search on opnai","")
            query = query.replace("openai","")
            web = "https://chat.openai.com/c/12adc1bd-36b1-49fd-b504-151c0ee640c9"
            webbrowser.open(web)
            pyautogui.sleep(5)
            pyautogui.typewrite(query)
            pyautogui.press("enter")
                

def sendemail(reciveremail,subject,message):
    try:
        email = EmailMessage()
        email['To'] = reciveremail
        email['Subject'] = subject
        email['From'] = Email
        
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com",587)
        s.starttls()
        s.login(Email,Password)
        s.send_message(email)
        s.close()
        speak("Email has been sented.")
    except Exception as e:
        speak("Something is wrong!")