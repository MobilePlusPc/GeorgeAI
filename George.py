# import libraries
import speech_recognition
import pyttsx3
import wikipedia
import pywhatkit
import datetime
import os
import webbrowser
import requests
from bs4 import BeautifulSoup
from playsound import playsound
import psutil
import pyjokes

recognizer = speech_recognition.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

name = "george"
city = "Hong Kong"
url = f"https://www.google.com/search?q=weather {city}"
html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")
woke_up = False
tell_temp_time = False

def speak(result):
     engine.say(result)
     engine.runAndWait()

while True:
     try:
          with speech_recognition.Microphone() as mic:
               print("listening...")
               playsound("sfx/beep.mp3")
               audio = recognizer.listen(mic)
               print("Recognizing...")
               result = recognizer.recognize_google(audio)
               result = result.lower()
               print(f"Result: {result}")

               if not woke_up:
                    if "hey" in result or name in result or "hello" in result:
                         if tell_temp_time:
                              if datetime.datetime.now().hour < 12:
                                   temp = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
                                   current_time = datetime.datetime.now().strftime("%H:%M %p")
                                   print(f"Current time: {current_time}\nTemperature: {temp}")
                                   speak(f"Good morning, sir. The current time is {current_time}. The Temperature outside is {temp}. What are we doing today?")
                                   result = ""
                                   woke_up = True
                              elif datetime.datetime.now().hour >= 12 and datetime.datetime.now().hour < 18:
                                   temp = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
                                   current_time = datetime.datetime.now().strftime("%H:%M %p")
                                   print(f"Current time: {current_time}\nTemperature: {temp}")
                                   speak(f"Good afternoon, sir. The current time is {current_time}. The Temperature outside is {temp}. What are we doing again?")
                                   result = ""
                                   woke_up = True
                              elif datetime.datetime.now().hour >= 18:
                                   temp = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
                                   current_time = datetime.datetime.now().strftime("%H:%M %p")
                                   print(f"Current time: {current_time}\nTemperature: {temp}")
                                   speak(f"Good night, sir. The current time is {current_time}. The Temperature outside is {temp}. It's late, sir.")
                                   result = ""
                                   woke_up = True
                         elif not tell_temp_time:
                              if datetime.datetime.now().hour < 12:
                                   speak(f"Good morning, sir.")
                                   result = ""
                                   woke_up = True
                              elif datetime.datetime.now().hour >= 12 and datetime.datetime.now().hour < 18:
                                   speak(f"Good afternoon, sir.")
                                   result = ""
                                   woke_up = True
                              elif datetime.datetime.now().hour >= 18:
                                   speak(f"Good night, sir.")
                                   result = ""
                                   woke_up = True
                    
               elif woke_up:
                    # search items
                    if "search" in result:
                         if "wikipedia" in result:
                              if name in result:
                                   item = result.replace(f"{name} search in wikipedia ", "")
                                   print(f"Search in wikipedia: {item}")
                                   search_result = wikipedia.summary(item, 1)
                                   print(f"Search result: {search_result}")
                                   speak(f"{search_result}, sir")
                              elif name not in result:
                                   item = result.replace(f"search in wikipedia ", "")
                                   print(f"Search in wikipedia: {item}")
                                   search_result = wikipedia.summary(item, 1)
                                   print(f"Search result: {search_result}")
                                   speak(f"{search_result}, sir")
                         elif "google" in result:
                              if name in result:
                                   item = result.replace(f"{name} search in google ", "")
                                   print(f"Search: {item}")
                                   speak(f"Searching in google {item}")
                                   webbrowser.open(f"https://www.google.com/search?q={item}")
                              elif name not in result:
                                   item = result.replace(f"search in google ", "")
                                   print(f"Search: {item}")
                                   speak(f"Searching in google {item}")
                                   webbrowser.open(f"https://www.google.com/search?q={item}")

                    # play videos on youtube
                    elif "play" in result:
                         if name in result:
                              video_title = result.replace(f"{name} play ", "")
                              print(f"Playing: {video_title}")
                              speak(f"Playing {video_title}")
                              pywhatkit.playonyt(video_title)
                         elif name not in result:
                              video_title = result.replace(f"play ", "")
                              print(f"Playing: {video_title}")
                              speak(f"Playing {video_title}")
                              pywhatkit.playonyt(video_title)

                    # time and temp and more
                    elif "what's" in result or "tell me" in result:
                         if "time" in result:
                              current_time = datetime.datetime.now().strftime("%H:%M %p")
                              print(f"Current time: {current_time}")
                              speak(f"The current time is {current_time}, sir")
                         elif "temperature" in result:
                              temp = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
                              print(f"Temperature: {temp}")
                              speak(f"The temperature outside is {temp}")
                         elif "usage" in result or "percentage" in result:
                              if "cpu" in result:
                                   currect_cpu_usage = psutil.cpu_percent(4)
                                   print(f"Current CPU usage: {currect_cpu_usage}%")
                                   speak(f"The current CPU usage is {currect_cpu_usage}%")
                              elif "ram" in result:
                                   currect_ram_usage = psutil.virtual_memory()[2]
                                   print(f"Current RAM usage: {currect_ram_usage}%")
                                   speak(f"The current RAM usage is {currect_ram_usage}%")

                    # open apps and websites
                    elif "open" in result:
                         if "edge" in result:
                              speak("Opening Microsoft Edge")
                              os.startfile("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
                         elif "code" in result:
                              speak("Opening Visual Studio Code")
                              os.startfile("C:/Users/Richard/AppData/Local/Programs/Microsoft VS Code/Code.exe")
                         elif "zoom" in result:
                              speak("Opening Zoom")
                              os.startfile("C:/Users/Richard/AppData/Roaming/Zoom/bin/Zoom.exe")
                         elif "paint" in result:
                              speak("Opening paint.net")
                              os.startfile("C:/Program Files/paint.net/paintdotnet.exe")
                    
                    # close apps
                    elif "close" in result:
                         if "notepad" in result:
                              speak("Closing notepad")
                              os.system("taskkill /f /im notepad.exe")
                         elif "edge" in result:
                              speak("Closing MicroSoft Edge")
                              os.system("taskkill /f /im msedge.exe")
                         elif "code" in result:
                              speak("Closing Visual Studio Code")
                              os.system("taskkill /f /im Code.exe")

                    # new files
                    elif "create" in result:
                         if "text" in result:
                              if name in result:
                                   file_name = result.replace(f"{name} create text file ", "")
                                   print(f"Creating new text file, {file_name}.txt")
                                   speak(f"Creating new text file, {file_name}.txt")
                                   os.system(f"notepad {file_name}")
                              elif name not in result:
                                   file_name = result.replace("create text file ", "")
                                   print(f"Creating new text file, file name {file_name}")
                                   speak(f"Creating new text file, file name {file_name}")
                                   os.system(f"notepad {file_name}")
                         elif "python" in result:
                              if name in result:
                                   file_name = result.replace(f"{name} create python file ", "")
                                   print(f"Creating new python file, {file_name}.py")
                                   speak(f"Creating new python file, {file_name}.py")
                                   os.system(f"type nul >> \"{file_name}.py\"")
                              if name not in result:
                                   file_name = result.replace("create python file ", "")
                                   print(f"Creating new python file, {file_name}.py")
                                   speak(f"Creating new python file, {file_name}.py")
                                   os.system(f"type nul >> \"{file_name}.py\"")
                         elif "c" in result:
                              if name in result:
                                   file_name = result.replace(f"{name} create c file ", "")
                                   print(f"Creating new c file, {file_name}.c")
                                   speak(f"Creating new c file, {file_name}.c")
                                   os.system(f"type nul >> \"{file_name}.c\"")
                              if name not in result:
                                   file_name = result.replace("create c file ", "")
                                   print(f"Creating new c file, {file_name}.c")
                                   speak(f"Creating new c file, {file_name}.c")
                                   os.system(f"type nul >> \"{file_name}.c\"")
                         elif "html" in result:
                              if name in result:
                                   file_name = result.replace(f"{name} create html file ", "")
                                   print(f"Creating new html file, {file_name}.html")
                                   speak(f"Creating new html file, {file_name}.html")
                                   os.system(f"type nul >> \"{file_name}.html\"")
                              if name not in result:
                                   file_name = result.replace("create html file ", "")
                                   print(f"Creating new html file, {file_name}.html")
                                   speak(f"Creating new html file, {file_name}.html")
                                   os.system(f"type nul >> \"{file_name}.html\"")
                         elif "folder" in result:
                              if name in result:
                                   file_name = result.replace(f"{name} create folder file ", "")
                                   print(f"Creating new folder")
                                   speak(f"Creating new folder")
                                   os.system(f"mkdir {file_name}")
                              if name not in result:
                                   file_name = result.replace("create folder file ", "")
                                   print(f"Creating new folder")
                                   speak(f"Creating new folder")
                                   os.system(f"mkdir {file_name}")

                    # tell jokes
                    elif "bored" in result:
                         try:
                              with speech_recognition.Microphone() as mic:
                                   speak("Do you wanna hear a joke, sir?")

                                   print("listening...")
                                   playsound("sfx/beep.mp3")
                                   audio = recognizer.listen(mic)
                                   print("Recognizing...")
                                   result = recognizer.recognize_google(audio)
                                   result = result.lower()
                                   print(f"Result: {result}")

                                   if "yes" in result:
                                        joke = pyjokes.get_joke()
                                        print(f"Joke: {joke}")
                                        speak(joke)
                                   elif "no" in result:
                                        speak("Ok, sir")
                                   
                              recognizer = speech_recognition.Recognizer()
                         except:
                              recognizer = speech_recognition.Recognizer()
                              continue

                    # clear the console
                    elif "clear console" in result:
                         speak("Clearing console")
                         os.system("cls")

                    # sleep
                    elif "sleep" in result:
                         print(f"Sleep mode: {woke_up}")
                         speak("As you wish, Sir")
                         os.system("cls")
                         break

          result = ""
          recognizer = speech_recognition.Recognizer()

     except:
          recognizer = speech_recognition.Recognizer()
          continue
