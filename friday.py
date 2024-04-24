import datetime
import json
import webbrowser
from datetime import date
import pyjokes
import pyttsx3
import speech_recognition as sr
import wikipedia
import pywhatkit
import subprocess
import ctypes
import wolframalpha
import jsonobj
import json


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'friday' in command:
                command = command.replace('friday', '')
                print(command)
            if 'hey friday' in command:
                command = command.replace('hey friday', '')
                print(command)
    except:
        pass
    return command


def run_friday():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print('Current time is ' + time)

    elif "weather" in command:
        api_key = "Api key"
        base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
        talk(" City name ")
        print("City name : ")
        city_name = takeCommand()
        complete_url = base_url + "appid =" + api_key + "&q =" + city_name
        response = requests.get(complete_url)
        x = response.json()

        if x["code"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            print(" Temperature (in kelvin unit) = " + str(
                current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                current_pressure) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(
                weather_description))

        else:
            talk(" City Not Found ")

    elif 'news' in command:

        try:
            json_obj = urlopen(
                '''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
            data = json.load(json_obj)
            i = 1

            talk('here are some top news from the times of india')
            print('''=============== TIMES OF INDIA ============''' + '\n')

            for item in data['articles']:
                print(str(i) + '. ' + item['title'] + '\n')
                print(item['description'] + '\n')
                talk(str(i) + '. ' + item['title'] + '\n')
                i += 1
        except Exception as e:

            print(str(e))

    elif 'define' in command:
        person = command.replace('define', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'what is mean by' in command:
        person = command.replace('what is mean by', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'good morning' in command:
        talk("Good morning sir,have a pleasant day")
        print("Good morning sir,have a pleasant day")
    elif 'good afternoon' in command:
        talk("Good afternoon sir")
        print("Good afternoon sir")
    elif 'good night' in command:
        talk('good night sir')
        print('good night sir')
    elif 'date' in command:
        talk(date.today())
    elif 'created you' in command:
        talk('i am a self made AI')
        print('i am a self made AI')

    elif "restart" in command:
        talk("restarting windows")
        subprocess.call(["shutdown", "/r"])

    elif 'lock window' in command:
        talk("locking the device")
        ctypes.windll.user32.LockWorkStation()

    elif 'hai' in command:
        talk('hi sir')
        print("hi sir")
    elif 'hi' in command:
        talk('hi sir')
        print('hi sir')
    elif 'hay' in command:
        talk('hi,how can i help u')
        print('hi,how can i help u')
    elif 'hey' in command:
        talk('hi,how can i help u')
        print('hi,how can i help u')

    elif 'hi' in command:
        talk('hi sir')
        print('hi sir')
    elif 'hello' in command:
        talk('hello sir')
        print('hello sir')
    elif 'your name' in command:
        talk('am friday')
        print('am friday')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())

    elif 'open youtube'in command:
        talk("Here you go, the Youtube is opening\n")
        webbrowser.open("youtube.com")

    elif 'open google'in command:
        talk("Opening Google\n")
        webbrowser.open("google.com")

    else:
        talk('As i am in initial stage of development,i have not get thought by it')

while True:
    run_friday()
