import speech_recognition as sr
import pyttsx3
import datetime
import sys
import urllib.request as ur
import json
import notifypy
import pygame.mixer
import time

def waterReminder():
    if (value_m <2 0) and (pasttime == 0 or pasttime == (presentime - datetime.timedelta(hours=0, minutes=1))):
        notification = notifypy.Notify()
        notification.title = "Smart plant"
        notification.message = "Please water your plant"
        notification.icon = './icon.ico'
        notification.send()
        water.play()
        pasttime = datetime.datetime.now()




pasttime = 0
presentime = 0
pygame.mixer.init()
pygame.mixer.music.load('water.mp3')
water = pygame.mixer.Sound('water.mp3')

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def temperature():
    website = ur.urlopen("https://api.thingspeak.com/channels/1340198/feeds.json?results=2")
    response = website.read().decode('utf-8')
    my_data = json.loads(response)
    value = my_data['feeds'][0]['field3']
    return value


def moisture():
    website = ur.urlopen("https://api.thingspeak.com/channels/1340198/feeds.json?results=2")
    response = website.read().decode('utf-8')
    my_data = json.loads(response)
    value = my_data['feeds'][0]['field1']
    return value


def light():
    website = ur.urlopen("https://api.thingspeak.com/channels/1340198/feeds.json?results=2")
    response = website.read().decode('utf-8')
    my_data = json.loads(response)
    value = my_data['feeds'][0]['field2']
    return value


def humidity():
    website = ur.urlopen("https://api.thingspeak.com/channels/1340198/feeds.json?results=2")
    response = website.read().decode('utf-8')
    my_data = json.loads(response)
    value = my_data['feeds'][0]['field4']
    return value


value_t = temperature()
value_h = humidity()
value_l = light()
value_m = moisture()


def engine_talk(text):
    engine.say(text)
    engine.runAndWait()


def usr_commands():
    try:
        with sr.Microphone() as source:
            print("Start speaking!!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def alexa_run():
    command = usr_commands()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        engine_talk('The current time is' + time)
    elif 'temperature' in command:
        engine_talk('the temperature of the plant is' + str(value_t))
    elif 'humidity' in command:
        engine_talk('the humidity of the plant is' + str(value_h))
    elif 'Light' in command:
        engine_talk('the light of the plant is' + str(value_l))
    elif 'health' in command:
        if value_m > 40:
            engine_talk('the plant is healthy')
        elif value_t > 40:
            engine_talk('the plant needs a cooler place')
        elif value_m < 40:
            engine_talk('the plant needs water')
        elif value_m < 40  and  value_t > 40:
            engine_talk('the plant needs water and a cooler place')
        else:
            engine_talk('the plant is healthy')
     elif 'about my plant' in command:
        engine_talk('This is a curry leaf plant')
    elif 'stop' in command:
        sys.exit()
    else:
        engine_talk('i could not hear properly')


while True:
    alexa_run()
    presentime = datetime.datetime.now()
    waterreminder(pasttime)
