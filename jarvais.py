import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initialize recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

# Function to make Friday speak
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice command
def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('Listening...')
            talk('Waiting for your command, sir.')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'friday' in command:
                command = command.replace('friday', '').strip()
                print(f"Command: {command}")
            else:
                talk("Please say the keyword 'Friday' to activate.")
                return ""
    except sr.UnknownValueError:
        talk("Sorry, I didn't catch that. Can you repeat?")
    except sr.RequestError:
        talk("Sorry, my speech service is down.")
    except Exception as e:
        print(f"Error: {e}")
        talk("An error occurred. Please try again.")
    return command

# Function to execute commands
def run_friday():
    while True:
        command = take_command()
        if not command:
            continue

        if 'play' in command:
            song = command.replace('play', '').strip()
            talk(f'Playing {song}')
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f'The current time is {time}')
        elif 'who is' in command:
            person = command.replace('who is', '').strip()
            info = wikipedia.summary(person, sentences=3)
            talk(info)
        elif 'madara' in command:
            talk('Wake up to reality!')
        elif ' joke' in command:
            joke = pyjokes.get_joke()
            talk(joke)
            print(joke)
        elif 'what is' in command:
            query = command.replace('what is', '').strip()
            info = wikipedia.summary(query, sentences=3)
            talk(info)
        elif 'good' in command:
            talk('Thank you, master!')
        elif 'exit' in command or 'stop' in command:
            talk('Goodbye, sir!')
            break
        else:
            talk('I did not understand that. Can you repeat?')

# Run the assistant
run_friday()