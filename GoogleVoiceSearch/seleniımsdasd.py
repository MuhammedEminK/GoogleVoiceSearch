
from selenium import webdriver
import time
import threading
driver = webdriver.Chrome()
driver.get("https://stackoverflow.com/questions/25394329/python-voice-recognition-library-always-listen")

driver.close()
