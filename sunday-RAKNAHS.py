import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)  # Adjusting for background noise
            talk('Welcome to Shan')
            talk('What would you like to do today, sir?')
            print('Listening...')
            voice = listener.listen(source, timeout=5)  # Adding timeout for recognition
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'friday' in command:
                command = command.replace('friday', '')
                talk(command)
    except sr.RequestError:
        talk("Sorry, I couldn't reach Google's servers. Please try again later.")
        return ''
    except sr.UnknownValueError:
        talk("Sorry, I did not understand. Could you repeat?")
        return ''
    except Exception as e:
        talk("Something went wrong. Try again.")
        print(f"Error: {e}")
        return ''

    return command


def run_friday():
    command = take_command()
    if command:
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('Playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')  # Correcting %P to %p
            talk('Current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 2)
            talk(info)
        elif 'cute' in command:
            talk('Manasa is cute tokki')
        elif 'tell me joke' in command:
            joke = pyjokes.get_joke()
            talk(joke)
        elif 'good' in command:
            talk('No, Jashu is the most stupid in the whole world')
        else:
            talk('Please say the command again, sir.')
    else:
        talk("Sorry, I didn't catch that.")


run_friday()
