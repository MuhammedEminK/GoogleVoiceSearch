
import speech_recognition as sr
from googlesearch import search
import os
import webbrowser


closeL = ["kapan", "kapat", "close", "kapatabilirsin"]
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        word = r.recognize_google(audio,language = "tr",show_all=True)
        print(word)
        if word:
            word = word["alternative"][0]['transcript']
            print(word)
            close = [i for i in closeL if i == word]
            print(close," close")
            if close:
                    os.system("taskkill/im msedge.exe")
            else:
                for i in search(word, tld="co.in", num=1, stop=1):
                    x = webbrowser.open_new(i)

            