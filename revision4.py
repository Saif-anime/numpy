import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
a = pyttsx3.init()

def speak(text):
    a.say(text)
    a.runAndWait()
    
    

    
def listen(source):
    with sr.Microphone() as source:
        print("listening...")
        audio = recognizer.listen(source)
        
    try:
        command = recognizer.recognize_google(audio)
        print("you said:", command)
        return command.lower()
    except sr.UnknownValueError:
        
        print("sorry, I didn't catch that.")
        return"" 
    except sr.RequestError:
        print("I'm having trouble connecting to the internet.")
        return""
    
def main():
    speak("hello! How can I assist you today?")
    while True:
        command = listen('hello')
        if "hello" in command:
            speak("hello! How can I assist you today?")
        elif "how are you" in command:
            speak("I'm just a computer programme, but thanks for asking!")
        elif "goodbye" in command:
            speak("Goodbye!")
            break
        else:
            speak("I'm not sure how to respond to that.")
            
main()
