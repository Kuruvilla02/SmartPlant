import speech_recognition as sr
import pyttsx3
import datetime
import sys
import urllib.request as ur
import json

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def temperature():
    # website = ur.urlopen("https://api.thingspeak.com/channels/1340198/feeds.json?results=2")
    # response = website.read().decode('utf-8')
    # my_data = json.loads(response)
    # # print(my_data['feeds'][0]['field1'])
    # value = my_data['feeds'][0]['field3']
    #return value
    return 10


def moisture():
    # website = ur.urlopen("https://api.thingspeak.com/channels/1340198/feeds.json?results=2")
    # response = website.read().decode('utf-8')
    # my_data = json.loads(response)
    # # print(my_data['feeds'][0]['field1'])
    # value = my_data['feeds'][0]['field1']
    #return value
    return 20


def light():
    # website = ur.urlopen("https://api.thingspeak.com/channels/1340198/feeds.json?results=2")
    # response = website.read().decode('utf-8')
    # my_data = json.loads(response)
    # # print(my_data['feeds'][0]['field1'])
    # value = my_data['feeds'][0]['field2']
    # return value
    return 30


def humidity():
    # website = ur.urlopen("https://api.thingspeak.com/channels/1340198/feeds.json?results=2")
    # response = website.read().decode('utf-8')
    # my_data = json.loads(response)
    # # print(my_data['feeds'][0]['field1'])
    # value = my_data['feeds'][0]['field4']
    # return value
    return 10.9


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
        else:
            engine_talk('the plant needs water')
    elif 'stop' in command:
        sys.exit()
    else:
        engine_talk('i could not hear properly')


while True:
    alexa_run()
