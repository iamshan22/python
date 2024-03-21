import speech_recognition as friday
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = friday.Recognizer()
engine = pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
  engine.say(text)
  engine.runAndWait()
def take_command():
    try:
       with friday.Microphone() as source:
           print('listening...')
           talk('waiting for ur command sir')
           voice = listener.listen(source)
           command =listener.recognize_google(voice)
           command = command.lower()
           if 'friday' in command:
               command = command.replace('friday','')
               talk(command)
    except:
            pass    
    return command
def run_friday():
    command = take_command()
    print(command)
    if 'play' in command:
        song= command.replace('play','')
        talk('playing.' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %P')
            print(time)
            talk('current timeis '+ time)
    elif 'who is' in command:
        person = command.replace ('who is','')
        info = wikipedia.summary(person, 2 )
        print(info)
        talk(info)
    elif 'madara' in command:
        talk('wake up to realtiy')   
    elif 'tell me joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    elif 'good' in command:
        talk('thank you master')
    elif 'what is' in command:
        prompt = command.replace('what is','')
        info = wikipedia.summary(prompt,2)
        print(info)
        talk(info)      
    else :
        talk('please say the command again sir.')  

run_friday()
