import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Lestening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data=recognizer.recognize_google(audio)
            return(data)
            print(data)

        except sr.UnknownValueError:
            print("Not Understand")


# sptext()


def speechtx(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    #voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice',voices[1].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',100)
    engine.say(x)
    engine.runAndWait()

#speechtx("I Miss You Ajay")

if __name__ == '__main__':
    
    #if "hey swaathi" in sptext().lower():
        
        #data1 = speechtx()


        while True:
                data1=sptext().lower()
                if "your name" in data1:
                    name = " my name is swaathi"
                    speechtx(name)

                elif "old are you" in data1:
                    age = " i am 28 years old"
                    speechtx(age)
                
                elif "time now" in data1:
                    time = datetime.datetime.now().strftime("%I%M%p")
                    speechtx(time)

                elif "youtube" in data1:
                    print = "opening.."
                    speechtx(print)
                    webbrowser.open("https://www.youtube.com/")

                elif "joke" in data1:
                    joke = pyjokes.get_joke(language="en", category="chuck")
                    speechtx(joke)

                elif "play music" in data1:
                    music ="palying music"
                    speechtx(music)
                    # add ="link"
                    # listsong=os.listdir(add)
                    # os.startfile(os.path.join(add,listsong[0]))

                elif "exit" in data1:
                    wish = "Thank you"
                    speechtx(wish)
                    break

                time.sleep(5)

    #else:
       # print("thanks")
    



        
