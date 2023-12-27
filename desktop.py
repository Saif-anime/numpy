import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("I'm having trouble connecting to the internet.")
        return ""

def main():
    speak("Hello! How can I assist you today?")
    while True:
        command = listen()
        if "hello" in command:
            speak("Hello! How can I assist you today?")
        elif "how are you" in command:
            speak("I'm just a computer program, but thanks for asking!")
        elif "goodbye" in command:
            speak("Goodbye!")
            break
        else:
            speak("I'm not sure how to respond to that.")

if __name__ == "__main__":
    main()
