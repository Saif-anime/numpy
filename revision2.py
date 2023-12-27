from datetime import datetime
import pyttsx3

#def greet():
current_time = datetime.now().time()

if current_time < datetime.strptime('12:00:00', '%H:%M:%S').time():
    greet = "Good morning"
    #return "Good morning"
elif current_time < datetime.strptime('16:00:00', '%H:%M:%S').time(): 
    greet = "Good afternoon"
    #return "Good afternoon"
elif current_time < datetime.strptime('20:00:00', '%H:%M:%S').time():
    greet = "Good evening"
    #return "Good evening"       
else:
    greet = "Good night"
    #return "Good night"
    
print(f"{greet}! The current time is {current_time.strftime('%H:%M:%S')}.")         


def speak(text):
    mohini = pyttsx3.init()
    mohini.say(text)
    mohini.runAndWait()
    
speak(f"{greet}! The current time is {current_time.strftime('%H:%M:%S')}.")    
# print(greet)
