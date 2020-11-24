import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
from googlesearch import search
from googlesearch import search_news
from googlesearch import get_page
import webbrowser
import os
import random
import smtplib
import signal
import sys
from mutagen.mp3 import MP3
TIMEOUT=10
from bs4 import BeautifulSoup
 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('bhumishaghela33@gmail.com','swizerland')
    server.sendmail('bhumishaghela33@gmail.com',to,content)
    server.close()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    pass
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hello I am bela. How can I help you?")
        
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        speak("listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        speak("Recognizing...")
        query=r.recognize_google(audio,language='en-US')
        speak("User said:",query)
    except Exception as e:
        print(e)
        print("Say it again please");
        return "None"
    return query    
query="";
wishMe()
if not sys.argv[1]:
    query=takeCommand()
else:
    query=sys.argv[1]

i=0
#while True:

if 'wikipedia' in query:
    speak('Searching Wikipedia...')
    query=query.replace("wikipedia","")
    results=wikipedia.summary(query,sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results);
    #not working as expected news search
    #direction-geolocation should b done
elif 'google' in query:
    speak('Searching Google...')
    query=query.replace("google","")
    
    if 'youtube video' in query:
        speak("Directing to Youtube.com")
        if 'mostlysane' in query:
            webbrowser.open("https://www.youtube.com/channel/UCvCyIiKSCA1fHKSCOKJyjXA")
        if 'desivedesi cooking' in query:
            webbrowser.open("https://www.youtube.com/channel/UCu0pMnPnjuyjQ8VsPPGg4EA");
    elif 'news' in query:
        for results in search_news(query,num=1,stop=1,pause=1):
            speak("Directing to")
            webbrowser.open(results)
            speak(results)
    elif 'direction' in query:
        if 'car' in query:
            webbrowser.open("https://www.google.com/maps/dir/Pune,+Maharashtra//@18.5205085,73.8217241,13z/data=!3m1!4b1!4m9!4m8!1m5!1m1!1s0x3bc2bf2e67461101:0x828d43bf9d9ee343!2m2!1d73.8567437!2d18.5204303!1m0!3e0")
        elif 'bus' in query:
            webbrowser.open("https://www.google.com/maps/dir/Pune,+Maharashtra//@18.5205085,73.8217241,13z/data=!3m1!4b1!4m9!4m8!1m5!1m1!1s0x3bc2bf2e67461101:0x828d43bf9d9ee343!2m2!1d73.8567437!2d18.5204303!1m0!3e3")
        elif 'cycling' in query:
            webbrowser.open("https://www.google.com/maps/dir/Kaveri+College+of+Arts+Science+and+Commerce,+Pune,+Maharashtra//@18.5023602,73.7917972,13z/data=!3m1!4b1!4m9!4m8!1m5!1m1!1s0x3bc2bf8c470e2413:0x30f1c26c617b4c2f!2m2!1d73.8268168!2d18.502282!1m0!3e1")
        elif 'walk' in query:
            webbrowser.open("https://www.google.com/maps/dir/Kaveri+College+of+Arts+Science+and+Commerce,+Pune,+Maharashtra//@18.5023602,73.7917972,13z/data=!3m1!4b1!4m9!4m8!1m5!1m1!1s0x3bc2bf8c470e2413:0x30f1c26c617b4c2f!2m2!1d73.8268168!2d18.502282!1m0!3e2")
        elif 'flight' in query:
            webbrowser.open("https://www.google.com/maps/dir/Pune,+Maharashtra//@18.5205085,73.8217241,13z/data=!3m1!4b1!4m9!4m8!1m5!1m1!1s0x3bc2bf2e67461101:0x828d43bf9d9ee343!2m2!1d73.8567437!2d18.5204303!1m0!3e4")
    elif 'open classroom' in query:
        webbrowser.open("https://classroom.google.com/c/MjQzNzQ3MjEzMTJa")
    else:
        for results in search(query,num=1,stop=1,pause=1):
            speak("Directing to")
            speak(results)
            webbrowser.open(results)
    
elif 'open youtube' in query:
    webbrowser.open("youtube.com")
elif 'play playlist' in query:
    music_dir='C:\\Users\\Bhumi\\Desktop\\bhumiphone\\Download'
    songs=os.listdir(music_dir)
    random.shuffle(songs)
    speak("Playing Your favourite playlist...")
    i=0
    while int(datetime.datetime.now().strftime("%S"))>=40:
                count=0
    for i in range(0,len(songs)):
        if '.mp3' in songs[i]:
            print(songs[i])
           

            os.startfile(os.path.join(music_dir,songs[i]))
            strmin=datetime.datetime.now().strftime("%M")
            m=int(strmin)
           
            audio=MP3('C:\\Users\\Bhumi\\Desktop\\bhumiphone\\Download'+'\\'+songs[i])
            
            minute=int((audio.info.length)/60)
        
            
           
           
            while minute+m!=int(datetime.datetime.now().strftime("%M")):
                count=0
                count=count+1
                
                
            
elif 'play music' in query:
    music_dir='C:\\Users\\Bhumi\\Desktop\\bhumiphone\\Download'
    songs=os.listdir(music_dir)
    query=query.replace("play music","")
    if not query:
        speak("which song would you like to play")
        song=raw_input()
    else:
        song=query.replace(" ","",1);
    i=0
    for i in range(0,len(songs)):
        if '.mp3' in songs[i]:
            if song in songs[i].lower():
                print(songs[i])
                speak("playing")
                speak(songs[i])
                os.startfile(os.path.join(music_dir,songs[i]))
                
                
                break
            if(i==len(songs)-1):
                speak("Directing to Gaana.com")
                if " " in song:
                    song=song.replace(" ","-")
                webbrowser.open("https://gaana.com/song/"+song)
            

elif 'the time' in query:
    strTime=datetime.datetime.now().strftime("%H:%M:%S")
    speak("The time is");
    speak(strTime)
    #also telling time
elif 'date' in query:
    strDate=datetime.datetime.today()
    speak("Today is");
    speak(strDate)
elif 'open notepad' in query:
    codePath="C:\\Windows\\notepad.exe"
    os.startfile(codePath)
    #module not yet found
elif 'open calender' in query:
    codePath=""
elif 'email' in query:
    try:
        speak("whom should I send");
        to=raw_input()
        speak("what should I say");
        content=raw_input()
        sendEmail(to,content)
        speak("Email has been sent");
    except Exception as e:
        print(e)
        speak("email not sent");
elif 'open calculator' in query:
    Path="C:\\Windows\\System32\\calc.exe"
    os.startfile(Path)
elif 'open command prompt' in query:
    Path="C:\\Windows\\System32\\cmd.exe"
    os.startfile(Path)
elif 'open control panel' in query:
    path="C:\\Windows\\System32\\control.exe"
    os.startfile(path)
elif 'open chrome' in query:
    cpath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    os.startfile(cpath)
elif 'play game' in query:
    speak("Which game do you want to play")
    speak("chess,free cell,hearts,mahjong,minesweeper,purble place,solitiare,spider solitiare")
    game=raw_input()
    
    if 'chess' in game:
          cp="C:\\Program Files\\Microsoft Games\\Chess\\Chess.exe"
          os.startfile(cp)
    elif 'free cell' in game:
          cp="C:\\Program Files\\Microsoft Games\\FreeCell\\FreeCell.exe"
          os.startfile(cp)
    elif 'hearts' in game:
          cp="C:\\Program Files\\Microsoft Games\\Hearts\\Hearts.exe"
          os.startfile(cp)
    elif 'mahjong' in game:
          cp="C:\\Program Files\\Microsoft Games\\Mahjong\\Mahjong.exe"
          os.startfile(cp)
    elif 'minesweeper' in game:
          cp="C:\\Program Files\\Microsoft Games\\Minesweeper\\Minesweeper.exe"
          os.startfile(cp)
    elif 'purble place' in game:
          cp="C:\\Program Files\\Microsoft Games\\Purble Place\\PurblePlace.exe"
          os.startfile(cp)
    elif 'spider solitiare'in game:
          cp="C:\Program Files\Microsoft Games\SpiderSolitaire\SpiderSolitaire.exe"
          os.startfile(cp)
    elif 'solitaire' in game:
          cp="C:\\Program Files\\Microsoft Games\\Solitaire\\Solitaire.exe"
          os.startfile(cp)

elif 'open wordpad':
    path1="C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe"
    os.startfile(path1)


