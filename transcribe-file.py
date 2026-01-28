import speech_recognition as sr
import pyttsx3
import pyaudio

#initialise the recognizer
r = sr.Recognizer()

def record_text():
    #loop incase of errors
    while(1):
        try:
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)
                print("Recognizing...")
                myText = r.recognize_google(audio)
                print(f"Recognized: {myText}")
                return myText
        except sr.RequestError as e:
            print("could not request results {0}".format(e))
        except sr.UnknownValueError:
            print("unknown error occurred")
    return

def transcribe_text(text):
    print(f"Writing to file: {text}")
    with open("output.txt", "a") as f:
        f.write(text + "\n")
    return

while(1):
    text = record_text()
    transcribe_text(text)
    print('wrote text')