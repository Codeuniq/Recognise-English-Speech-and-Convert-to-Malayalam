import speech_recognition as sr
from translate import Translator
from gtts import gTTS
from playsound import playsound

listner=sr.Recognizer()

with sr.Microphone() as source:
    print("Listening....")
    listner.adjust_for_ambient_noise(source)
    voice_recorded=listner.listen(source)
    recognised_text=listner.recognize_google(voice_recorded)
    print(recognised_text)

translator=Translator(from_lang='en',to_lang="ml")

translated_text=translator.translate(recognised_text)

print(translated_text)

mal=gTTS(translated_text,lang="ml")
mal.save("translated_voice.mp3")
playsound("translated_voice.mp3")
