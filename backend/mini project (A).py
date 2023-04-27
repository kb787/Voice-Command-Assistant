import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib as smtp
import pyautogui 

jarv = pyttsx3.init('sapi5')
voices = jarv.getProperty('voices')
jarv.setProperty('voice', voices[0].id)

def speak(audio):
    jarv.say(audio)
    jarv.runAndWait()

def greet():
      time = int(datetime.datetime.now().hour)
      if time >= 0 and time < 12:
       speak("Good Morning sir what can I do for you ")

      elif time>= 12 and time < 16:
       speak(" Good Afternoon sir what can I do for you ")   

      elif time>=16 and time < 20:
       speak("  Good Evening sir what can I do for you  ")  

      elif time>=20 and time < 24:
       speak(" Good Night sir what can I do for you  ")          

def listen():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        rec.adjust_for_ambient_noise(source, duration=2)
        print("Listening...")
        rec.pause_threshold = 1
        audio = rec.listen(source)
        print(" Understanding ...")    
        command = rec.recognize_google(audio, language='english')
        print(command)
    return command

if__name__ = "__main__"  
greet()

while True :
    listen()
    task = listen().lower()
    if "open wikipedia" in task :
       print(" Searching results for your command ") 
       task = task.replace("wikipedia", "" )
       display = wikipedia.summary(task, sentences = 4)
       speak(" According to researches ")
       print(display)
       speak(display)
    elif "open youtube" in task :
        webbrowser.open("https://www.youtube.com") 
    elif "open google"  in task :
        webbrowser.open("https://www.google.com/")
    elif "open github"  in task :
        webbrowser.open("https://github.com/")
    elif "open facebook" in task :
         webbrowser.open("https://www.facebook.com/")
    elif "open instagram" in task :
         webbrowser.open("https://www.instagram.com/")
    elif "open universitywebsite" in task :
         webbrowser.open("https://mu.ac.in/")
    elif "open hackerrank" in task :
         webbrowser.open("https://www.hackerrank.com/")
    elif "open amazon" in task:
         webbrowser.open("https://www.amazon.in/")
    elif "open flipkart" in task:
         webbrowser.open("https://www.flipkart.com/")
    elif "open swiggy" in task:
         webbrowser.open("https://www.swiggy.com/")
    elif "open zomato" in task:
         webbrowser.open("https://www.zomato.com/india")
    elif "open netflix" in task:
         webbrowser.open("https://www.netflix.com/in/")
    elif "open nptel" in task:
         webbrowser.open("https://nptel.ac.in/")
    elif "open coursera" in task:
         webbrowser.open("https://www.coursera.org/")
    elif "open whatsapp" in task:
         webbrowser.open("https://www.whatsapp.com/")
    elif "open irctc" in task:
         webbrowser.open("https://www.irctc.co.in/nget/train-search")
    elif "open bookmyshow" in task:
         webbrowser.open("https://in.bookmyshow.com/") 
    elif "open linkedin" in task:
         webbrowser.open("https://www.linkedin.com/")              
    elif "display time"  in task :
        Dtime = datetime.datetime.now().strftime("%H:%M:%H")
        speak(f"KB Sir the time is {Dtime}")
    elif "open mails" in task :
          webbrowser.open("https://mail.google.com/mail/")
    elif "open musicweb" in task :
        webbrowser.open("https://www.gaana.com")                      
    elif "open stackoverflow" in task :
        webbrowser.open("https://www.stackoverflow.com") 
    elif "open geeksforgeeks" in task :
        webbrowser.open("https://www.geeksforgeeks.com")
    elif "open leetcode" in task :
        webbrowser.open("https://www.leetcode.com")
    elif "take a break" in task : 
        speak("Thanks sir for your free time , have a good day ")
        exit()
    elif "give your intro" in task :
        speak(" I am assistant created by KB sir and company an AI which uses speech recognition designed in Python. Various modules had been used pyttsx3 for giving sound , speech recognition for converting speech to text , os module for executing command opening a file from directory , smtplib for sending mails . I can perform various tasks like sending an e-mail ,opening variuos websites, opening notepad, other application.I can also perform voice to text typing hope you enjoy your time with me  ")  
    elif "group info" in task :
        speak(" Person 1 : Karan Bhanushali , SE-1 , Cmpn roll no 9. Person 2 : Nikhil Joshi , SE-1 , Cmpn roll no 47. Person 3 : Sumit Anantwal , SE-1 , Cmpn roll no 5 . Person 4 : Chetan Edge , SE-1 , Cmpn Roll no 29  ")              
    elif "send email" in task :
        speak(" Enter the message you want to convey ")
        person2content = listen().lower()
        server = smtp.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('youremail@gmail.com','password')
        server.sendmail('karanbhanu799@gmail.com','karanbhanu787@gmail.com',person2content)
        speak(" Successfully parsed your message from freakywebdev@gmail.com " +  " The message is" + person2content) 
        server.close()   
    elif "open important documents"  in task :
          impDoc = "C:\\Users\\Admin\\Desktop\\KB\\Imp Doc"
          os.startfile(impDoc)     
    elif "open android studio folder" in task :
          androidStudio = "C:\\Program Files\\Android"
          os.startfile(androidStudio)
    elif "open notepad" in task :
          notePad = "C:\\Windows\\Notepad.exe"
          os.startfile(notePad)     
    elif  "open eclipse" in task :
          eclipse = "C:\\Users\\Admin\\eclipse\\java-2022-095\\eclipse"
          os.startfile(eclipse)
    elif "open code blocks" in task :
          codeblocks = "C:\\Program Files\\CodeBlocks\\codeblocks.exe"
          os.startfile(codeblocks) 
    elif "open mysql workbench" in task :
          mysql = "C:\\Program Files\\MySQL\MySQL Workbench 8.0 CE\\MySQLWorkbench.exe"
          os.startfile(mysql)      
    elif "open ppt" in task :
          ppt = "C:\\Users\\Admin\\Desktop\\KB\\Imp Doc\\Voice command assistant  based on Artificial Intelligence sem4.pptx"
          os.startfile(ppt) 
    elif "open report" in task :
          report = "C:\\Users\\Admin\\Desktop\\KB\\Imp Doc\\finalreport.docx"
          os.startfile(report)
    elif "open log book" in task :
          logbook = "C:\\Users\\Admin\\Desktop\\KB\\Imp Doc\\logbookfinal.docx"
          os.startfile(logbook)
    elif "type notes" in task : 
          filePath = "C:\\Users\\Admin\\Desktop\\KB\\Imp Doc\\assistant.txt"
          os.startfile(filePath)
          speak("Enter the text to write in notes") 
          takeNote = listen()
          pyautogui.typewrite(takeNote)                   
    else :
        speak(" Repeat the command once again please ")     
        

         
        

         
        


