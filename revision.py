from datetime import datetime
import pyttsx3

def greet():
    current_time = datetime.now().time()
    # print(current_time)

    if current_time < datetime.strptime("12:00:00", "%H:%M:%S").time():
        print("Good morning!")
        return "Good Morning"
    elif current_time < datetime.strptime("16:00:00", "%H:%M:%S").time():
        print("Good afternoon!")
        return "Good Afternoon"
    elif current_time < datetime.strptime("20:00:00", "%H:%M:%S").time():
        print("Good evening!")
        return "Good Evening"
    else:
        print("Good night!")
        return "Good Night"

def speak(text):
    mohini = pyttsx3.init()
    mohini.say(text)
    mohini.runAndWait()


speak(greet())

