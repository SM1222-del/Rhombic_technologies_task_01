import datetime
import pyttsx3
import speech_recognition as aa
from selenium_web import*
from yt_auto import *
from news import*
import randfacts

listener = aa.Recognizer()
human = pyttsx3.init()

# Set the voice to female and adjust speech properties
voices = human.getProperty('voices')
human.setProperty('voice', voices[1].id)  # Female voice
human.setProperty('rate', 150)  # Speech rate
human.setProperty('volume', 1)  # Volume level (0.0 to 1.0)


# Function to pass the parameters
def talk(text):
    human.say(text)
    human.runAndWait()


talk("Hi there!I'm your voice assistant.How can I assist you!")


def detail():
    pass


def temp():
    pass


talk("Temperature in Lahore is" + str(temp())) + "degree celsius" + "and with" + str(detail())


# Function to get the input
def input_instruction():
    try:
        with aa.Microphone() as source:
            listener.energy_threshold = 10000
            listener.adjust_for_ambient_noise(source, 1.2)
            print("Listening.....")
            audio = listener.listen(source)
            instruction = listener.recognize_google(audio)
            speech = listener.listen(source)
            instruction = instruction.lower()
        if "what" and "about" and "you" in instruction:
            talk("I'm having a good day,thank you what can I do for you!")
            if "sidra" in instruction:
                instruction = instruction.replace('sidra', '')
                print(instruction)
                return instruction
    except aa.UnknownValueError:
        print("Sorry, I did not understand the audio.")
    except aa.RequestError as e:
        print(f"Sorry, I'm having trouble with the speech recognition service. Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return ""


# Function to add functionality of playing any video
def play_sidra():
    while True:
        instruction = input_instruction()
        if instruction == "":
            continue  # If no valid instruction, continue listening
        # print(f"Processed Instruction: {instruction}")
        if "exit" in instruction or "quit" in instruction:
            talk("Goodbye!")
            break

    if "time" in instruction:
        time = datetime.datetime.now().strftime("%I:%M:%p")
        talk(f"Current time is {time}")

    elif "date" in instruction:
        date = datetime.datetime.now().strftime('%d/%m/%Y')
        talk(f"Today's date is {date}")

    elif "today is" in instruction and "day of" in instruction:
        talk("Today is " + datetime.datetime.now().strftime("%A"))

    elif "how are you" in instruction:
        talk("I am fine, how about you?")

    elif "what is your name" in instruction:
        talk("I am Sidra, your assistant. What can I do for you?")

    elif "information" in instruction:
        talk("You need information related to which topic ")

        with aa.Microphone() as source:
            listener.energy_threshold = 10000
            listener.adjust_for_ambient_noise(source, 1.2)
            print("Listening.....")
            audio = listener.listen(source)
            infor = listener.recognize_google(audio)

        talk("Searching {} in wikipedia".format(infor))
        assist=assist.infos()
        assist.get_info(infos)

    elif "play" and "video" in instruction:
        talk("You want to play which video?")
        with aa.Microphone() as source:
            listener.energy_threshold = 10000
            listener.adjust_for_ambient_noise(source, 1.2)
            print("Listening.....")
            audio = listener.listen(source)
            video = listener.recognize_google(audio)
        print("playing {} on youtube".format(video))
        assist=Music()
        assist.play(video)
    elif "news" in instruction:
        news_titles = news()
        for title in news_titles:
            talk(title)
            print(title)
    elif "fact" or "facts" in instruction:
        r_fact = randfacts.getfact()
        print(r_fact)
        talk("did you know that" + r_fact)


play_sidra()
