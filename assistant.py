import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

"""Dheeraj Naik, Project: Voice Assistant"""

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def greeTing():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am your Desktop Buddy, How can I help you")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

'''It takes microphone input from the user and returns string output'''
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening............")
        r.pause_threshold = 1 
        audio = r.listen(source)
    try: 
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        print("Say that again please....")
        return "None"
    return query

# def sendEmail(to, content):
#    server = smtplib.SMTP('smtp.gmail.com', 587)
#    server.ehlo()
#    server.starttls()
#    server.login('personalassistant@gmail.com','personalAssistant##')
#   #  ifpf kczn txmg djoz 
#    server.sendmail('personalassistant@gmail.com', to, content)
#    server.close()
   
   

if __name__ == "__main__":
   greeTing()
   while True:
       query = takeCommand().lower()
# Logic for executing task based on query
       if 'wikipedia' in query:
         speak('Searching Wikipedia...')
         query = query.replace("wikipedia","")
         results = wikipedia.summary(query, sentences=3)
         speak("According to Wikipedia")
         print(results)
         speak(results)

       elif 'open youtube' in query:
         speak("opening youtube for you")
         webbrowser.open("youtube.com")

       elif 'open google' in query:
         speak("opening google for you")
         webbrowser.open("google.com")

       elif 'open chrome' in query:
         speak("opening chrome for you")
         webbrowser.open("chrome.com")

       elif 'open stackoverflow' in query:
         speak("Opening stackoverflow for you")
         webbrowser.open("stackoverflow.com")

       elif 'play music' in query:
         music_dir = 'C://Users//dheer//OneDrive//Documents//Audio'
         songs = os.listdir(music_dir)
         print(songs)
         speak("playing music for you sir enjoy")
         os.startfile(os.path.join(music_dir, songs[1]))

       elif 'open 007' in query:
         game_dir = 'C://Users//dheer//OneDrive//Documents'
         speak("opening 007 for you")
         os.startfile(game_dir)

       elif 'the time' in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"Sir, the time is {strTime}")

       elif 'open code' in query:
          codePath = 'C//Users//dheer//OneDrive//Documents//Ea Sports Cricket 2007'
          speak('opening vs code for you')
          os.startfile(codePath)

       elif 'my portfolio' in query:
          link = 'https://dheeraj1908.github.io//'
          speak("This portfolio website showcases About Master Dheeraj and his hard and soft skills and even his experiences the website is also design and developed by master Dheeraj")
          webbrowser.open(link)

       elif 'show my portfolio' in query:
          link = 'https://dheeraj1908.github.io//'
          speak("This portfolio website showcases About Master Dheeraj and his hard and soft skills and even his experiences the website is also design and developed by master Dheeraj")
          webbrowser.open(link)

       elif 'portfolio' in query:
          linked = 'https://dheeraj1908.github.io//'
          speak("This portfolio website showcases About Master Dheeraj and his hard and soft skills and even his experiences the website is also design and developed by master Dheeraj")
          webbrowser.open(linked)

       elif 'team tejas' in query or 'sfit tejas' in query or 'dheeraj sfit tejas website' in query or "show me sfit tejas website" in query or "tejas website" in query or 'show me tejas webite' in query or 'tejas' in query or 'open tejas website' in query:
          link = 'https://mesa.sfit.ac.in//Tejas-Website-master//src//index.html'
          speak("Master Dheeraj, Master parth and Master louis are web dveloper of this website")
          webbrowser.open(link)
          

       elif 'gati sfit website' in query or 'team gati' in query or 'gati website' in query or 'open gati sfit' in query or 'gati sfit' in query or 'show me gati website' in query or 'gati' in query:
          link = 'https://gatee.sfit.ac.in//Home.html'
          speak("Master Dheeraj, Master parth and Master louis are web dveloper of this website")
          webbrowser.open(link)

       elif 'Massa sfit website' in query or 'mesa sfit website' in query or 'open mesa sfit' in query or 'show me mesa sfit website' in query:
          link = 'https://mesa.sfit.ac.in//'
          speak("Master Dheeraj, Master parth and Master louis are web dveloper of this website")
          webbrowser.open(link)

       elif 'quit' in query:
          speak("Bye sir, I hope you had a quality time with me, see you again!")
          exit()

       '''elif 'email to dheeraj' in query:
           try:
               speak("What should I say?")
               content = takeCommand()
               to = "personalassistant1908@gmail.com"
               sendEmail(to, content)
               speak("Email has been sent!")
           except Exception as e:
               print(e)
               speak("Sorry Sir I am not able to send the mail")'''

      

    

   
  