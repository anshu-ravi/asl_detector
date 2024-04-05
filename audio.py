from gtts import gTTS
import os 
import time 
from playsound import playsound


def speak(text, filename = "text"):
    language = 'en'
    speech = gTTS(text = text, lang = language, slow = False)
    if os.path.exists(f'{filename}.mp3'):
        os.remove(f'{filename}.mp3')
    speech.save(f'{filename}.mp3')
    time.sleep(1)
    playsound(f'{filename}.mp3')
    

def main():
    text = "Hello, I am a text to speech bot"
    speak(text)

if __name__ == "__main__":
    main()