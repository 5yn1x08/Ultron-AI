import random
import sys
import time
import webbrowser
import speedtest
from pywikihow import search_wikihow
import pyautogui
import pywhatkit as kit
import pyttsx3
import speech_recognition as sr
import datetime
import os
import urllib.request
import urllib.parse
import re
from requests import get
import wikipedia
import smtplib
import requests
from bs4 import BeautifulSoup
from playsound import playsound
import instaloader



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('vocies', voices[1].id)
engine.setProperty('rate', 190)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source,timeout=4,phrase_time_limit=7)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}")

    except Exception as e:
        speak('Say that again please...')
        return "none"
    query = query.lower()
    return query

#strtup sound
def sound():
    print("ultron Initializing.....")
    playsound('ultron.mp3')

def intro():
    print("Ultron Initializing.....")
    playsound('intro.mp3')

def personal():
    speak("I am Ultron, An advance AI system! ")
    speak("Now i hope you know me")


#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning sir!")
    elif hour> 12 and hour< 18:
        speak("good afternoon sir!")
    else:
        speak("good evening sir!")
    speak("i am online. please tell me how can i help you? ")

#to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'your password')
    server.sendmail('your email id', to, content)
    server.close()

#under development
# def run(self):
#     speak("please say wakeup to continue")
#     while True:
#         self.query = self.takecommand()
#         if "are you there" or "are you there" in self.query:
#             self.TaskExecution()



def TaskExecution():
    sound()
    wish()
    while True:
    #if 1:

        query = takecommand()

        #logic building for tasks
        if "hello" in query or "hey" in query:
            speak("hello sir, may i help you with something. ")

        elif "how are you" in query:
            speak("im fine sir, what about you?")

        elif "fine" in query or "also good" in query:
            speak("that's great to hear from you.")

        elif "thank you" in query or "thanks" in query:
            speak("it's my pleasure sir.")

        elif "open notepad" in query:
            speak("ok sir, Opening notepad!")
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        elif "shut up ultron" in query:
            speak('sir dont bully me or i will call your girlfriend')
        
        elif ("do you know anything" in query or "remember" in query):
            reminder_file = open("data.txt", 'r')
            speak("You said me to remember that: " + reminder_file.read())

        #to close any application
        elif "close notepad" in query:
            speak("okay sir!, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "open discord" in query:
            speak("opening discord")
            dpath = "C:\\Users\\NUCLEYA\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord"
            os.startfile(dpath)

        elif "close discord" in query:
            speak("okay sir!, closing discord")
            os.system("taskkill /f /im Discord.exe")

        elif "open youtube" in query:
            speak("what would you like to watch? ")
            sy = takecommand().lower()
            webbrowser.open(f'https://www.youtube.com/results?search_query={sy}')

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "volume up" in query:
            pyautogui.press("volumeup")

        elif "volume down" in query:
            pyautogui.press("volumedown")

        elif "mute" in query:
            pyautogui.press("volumemute")

        elif "what is my internet speed" in query:
            try:
                os.system('cmd /k "speedtest"')
            except:
                speak('there is some issue')


        elif "play music" in query:
            music_dir = "C:\\Users\\NUCLEYA\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip} ")

        #to check instagram profile
        elif 'check instagram profile' in query or 'profile on instagram' in query:
            speak('sir please enter the username.')
            name = input("enter the username here : ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            time.sleep(5)
            speak("sir would you like to download profile picture of this account..?")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir, profile picture is downloaded successfully..! ")
            else:
                pass

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            #print(results)

        elif "open google" in query:
            speak("sir, what should i search on google...?")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        #for the location
        elif "where i am" in query or "where we are" in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/' +ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                #print(geo_data)
                city = geo_data['city']
                #state = geo_data['state']
                country = geo_data['country']
                speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                speak('sorry sir, Dur to network issue i am not able to find where we are.')
                pass

        elif "send whatsapp message" in query:
            kit.sendwhatmsg("+919104179793", "this msg is sent by AI",13,15)

        elif "take screenshot" in query or "take a screenshot" in query:
            speak('sir, please tell me the name for this screenshot file')
            name = takecommand().lower()
            speak('please sir hold the screen for few seconds, i am taking screenshot..')
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak('i am done sir, the screenshot is saved!')

        elif "play song on youtube" in query:
            #kit.playonyt("see you again")
            #this feature is under development
            speak('okay sir, which song you would to listen..?')
            yt_song = takecommand().lower()
            #a = 'all the things'
            query_string = urllib.parse.urlencode({"search_query": yt_song})
            html_content = urllib.request.urlopen("https://www.youtube.com.hk/results?" + query_string)
            search_results = re.findall(r'url\"\:\"\/watch\?v\=(.*?(?=\"))', html_content.read().decode())
            if search_results:
                print("http://www.youtube.com/watch?v=" + search_results[0])
                webbrowser.open_new("http://www.youtube.com/watch?v={}".format(search_results[0]))


        elif "send email" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = "nisarg0806@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to sent this mail")

        elif "activate how to do mod" in query:
            speak("how to do mod is activated")
            while True:
                speak("please tell me what you want to know..?")
                how = takecommand()
                try:
                    if 'exit' in how or "close" in how:
                        speak("okay sir, how to do mod is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        #how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir, i am unable to find this")


        elif "you can sleep" in query or "sleep now" in query:
            speak("okay sir!, i am going to sleep you can call me anytime.")
            break

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rund1132.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "what is the current temperature" in query:
            search = "temperature in rajkot"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find('div',class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()

        #speak("sir, do you have any other work")
if __name__ == "__main__":
    while True:
        permission = takecommand()
        if "daddy's home" in permission:
            intro() and speak("Welcomeback sir!!")
            TaskExecution()
        if "wake up ultron" in permission:
            TaskExecution()
        elif "shutdown ultron" in permission:
            speak('thanks for using me sir and have a good day!')
            sys.exit()