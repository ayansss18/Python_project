import pyttsx3
import datetime
import wikipedia
import speech_recognition as rec
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        speak("Good morning boss")
    elif hour>=12 and hour<17:
        speak("Good afternoon boss")
    elif hour>=17 and hour<21:
        speak("Good evening boss")
    elif hour>=21 and hour<4:
        speak("Good night boss")
    speak("I am Spider. How may I help you?")
    
def command():
    sr=rec.Recognizer()
    with rec.Microphone() as mic:
        print("listening...")
        sr.energy_threshold=500
        sr.pause_threshold=0.8
        audio=sr.listen(mic)

    try:
        
        print("Recognizing...")
        query=sr.recognize_google(audio,language='en-in')
        
        if "stop" in query or "shut up" in query or "quit" in query:
            speak("exiting sir")
            
        else:
            print(f"You said: {query}\n")
            speak(f"You said: {query}\n")
            

    except:
        print("could not hear that! Please repeat again...")
        speak("could not hear that! Please repeat again...")
        return "None"
    return query
    
    

if __name__=="__main__":
    wishme()
    while True:
        query=command().lower()
        
        if "wikipedia" in query:
            print("Searching in wikipedia")
            speak("Searching in wikipedia")
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif "spider" in query:
            speak("hello sir! please tell me, how can i help you?")
           
        elif 'open youtube' in query:
            speak('opening youtube sir')
            webbrowser.open("youtube.com")
        
        elif 'close youtube' in query:
            speak("closing youtube sir")
            os.system("taskkill /im msedge.exe /f")
            
        elif 'open whatsapp' in query:
            wa='C:\\Users\\Ayan\\OneDrive\\Desktop\\WhatsApp'
            speak("opening whatsapp sir")
            os.startfile(wa)
        
        elif 'time' in query:
            time=datetime.datetime.now().strftime("%H %M %S")
            print("The time is now: ",time)
            speak("The time is now")
            speak(time)
            speak(" seconds, sir")
            
        elif "date" in query:
            date=datetime.datetime.now().strftime("%d %m %Y")
            print("Today's date is: ",date)
            speak("Today's date is")
            speak(date)
            speak('sir')
            
        elif " who are you" in query or "hu r u" in query or "you" in query:
            speak("I am spider AI and I am created by my boss Mr. Ayan.")
            
        elif "am i" in query or "my name" in query or "your boss" in query:
            speak("You are my boss sir and your name is Mr. Ayan")
            
        elif "movie" in query:
            speak("You should watch south movie Side B, sir")
            print("You should watch south movie Side B, sir")

            
        elif "play it" in query or "play" in query or "plate" in query or "playit" in query:
            movie='B:\\Movies\\side_b.mkv'
            os.startfile(movie)
        
        elif "please stop" in query or"stop" in query or 'spider stop' in query or "stop spider" in query or "quit" in query or "shut up" in query in query:
            exit()