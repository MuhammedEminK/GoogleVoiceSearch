import speech_recognition as sr
import speech_recognition
from selenium import webdriver
from googlesearch import search
import selenium
import keyboard
import time


while True:
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("...")
        audio = r.listen(source)
        try:
            audio = r.listen(source)
            while True:
                metin = str(r.recognize_google(audio,language = "tr"))
                print(metin)
                print(bool(metin))
                if metin:
                    for j in search(metin, tld="co.in", num=1, stop=1, pause=2,lang="tr"):
                        print(j)
                        driver = webdriver.Chrome()
                        driver.get(j)
                        time.sleep(10)
                        try:
                            print("sekme kapatılmış")
                        except selenium.common.exceptions.WebDriverException:
                            driver.close()                  
                break
        except speech_recognition.UnknownValueError:
            print(".")




