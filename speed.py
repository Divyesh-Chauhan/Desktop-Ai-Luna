import speedtest 
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def speedI():
    wifi  = speedtest.Speedtest()
    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
    download_net = wifi.download()/1048576
    print("Upload Speed is", int(upload_net),"Mbps")
    print("download speed is ",int(download_net),"Mbps")
    speak(f"Upload speed is {int(upload_net)}Mbps.")
    speak(f"download speed is {int(download_net)}Mbps.")
    
speedI()
