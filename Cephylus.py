import os
import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
import pyaudio
import wikipedia
import webbrowser

chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
webbrowser.get(chrome_path).open('www.google.com')

email = {'Dad':'pramod.agarwal@vodafoneide.com', 'Isha':'agrawal.ishaa@gmail.com', 'Mom':'agrawal.gudiaa@gmail.com'}

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning! I am Cephylus. Your friendly AI Assistant. How may I help you sir?")
    elif(hour>=12 and hour<17):
        speak("Good Afternoon! I am Cephylus. Your friendly AI Assistant. How may I help you sir?")
    elif(hour>=17 and hour<21):
        speak("Good Evening!I am Cephylus. Your friendly AI Assistant. How may I help you sir?")
    else:
        speak("Good Night & take care sir.")
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You are saying: {query}\n")

    except Exception as e:
        # print(e)
        print("Sorry, I didn't catch that. Say that again...")

        return "None"
    return query 

f = open("D:\\Plain Text Files\\cephylus.txt", "r")
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.startls()
    server.login("falakagrawal8@gmail.com", f.read())
    server.sendmail("falakagrawal8@gmail.com", to, content)

if __name__ == '__main__':
    wishMe()
    #while True:
    if 1: 
        query = takeCommand().lower()

        #logic for executing tasks 
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 5)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            speak("Here is your inbox.")
            webbrowser.open("gmail.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play me some music/song' in query:
            speak("Sure. Why not?")
            webbrowser.open("https://open.spotify.com/embed/playlist/02vb5BrzSRTBAqhchU55dC")

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Right now the time is {strtime}")

        elif 'open vs code' in query:
            codepath = "D:\\Microsoft VS Code\\Code.exe" 
            os.startfile(codepath)

        elif 'close vs code' in query:
            codepath = "D:\\Microsoft VS Code\\Code.exe"
            os.close(codepath)

        elif 'open visual studio' in query:
            path1 = "D:\\Microsoft Visual Studio 2019\\IDE\\Installer\\Common7\\IDE\\devenv.exe"
            os.startfile(path1)

        elif 'close visual studio' in query:
            path1 =  "D:\\Microsoft Visual Studio 2019\\IDE\\Installer\\Common7\\IDE\\devenv.exe"
            os.close(path1)

        elif 'open unreal engine' in query:
            path2 = "D:\\Unreal Engine\\UE_4.26\\Engine\\Binaries\\Win64\\UE4Editor.exe"
            os.startfile(path2)

        elif 'close unreal engine' in query:
            path2 = "D:\\Unreal Engine\\UE_4.26\\Engine\\Binaries\\Win64\\UE4Editor.exe"
            os.close(path2)

        elif 'shutdown the computer' in query:
            speak("Are you sure sir??")
            permission = takeCommand()
            if "yes" in permission:
                speak("shutting down the system")
                os.system("shutdown /s /t 30")
            elif "no cephylus" or "not yet cephylus"  in permission:
                speak("ok sir.")

        elif 'compose mail' in query:
            try:
                speak("Give me the message.")
                content = takeCommand()
                to = 'falakagrawal8@gmail.com'
                sendEmail(to, content)
                speak("Email sent.")
            
            except Exception as e:
                print(e)
                speak("I'm sorry. E-mail could not be sent.")
