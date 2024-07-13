import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import pyautogui
import os


r = sr.Recognizer()

engine = pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def handle_command(command):

    command = command.lower()

    if 'press start button' in command:
        engine.say('Start button pressed')
        pyautogui.press('win')
    elif 'open application' in command:
        engine.say('Which application would you like to open?')
        engine.runAndWait()
        application = listen_for_command()
        engine.say(f'Opening {application}')
        engine.runAndWait()
        try:
            app_paths = {
                "notepad": "notepad.exe",
                "calculator": "calc.exe",
                "camera": "camera.exe"  
            }
            if application in app_paths:
                subprocess.Popen(app_paths[application])
            else:
                engine.say(f'{application} not found in predefined applications')
        except Exception as e:
            engine.say(f'Error opening {application}: {str(e)}')
        engine.runAndWait()
    elif 'open youtube' in command:
        engine.say('Opening YouTube')
        webbrowser.open('https://www.youtube.com/')
        engine.runAndWait()
    
    elif 'open channel in youtube' in command:
        engine.say('Opening vogue')
        webbrowser.open('https://www.youtube.com/results?search_query=vogue+beauty+secrets')
        engine.runAndWait()
    elif 'open any video ' in command:
        engine.say('Opening')
        webbrowser.open('https://www.youtube.com/watch?v=oQkQv1ULyzs')
        engine.runAndWait()
    elif 'open spotify' in command:
        engine.say('Opening spotify')
        webbrowser.open('https://open.spotify.com/collection/tracks')
        engine.runAndWait()
    elif 'play song' in command:
        engine.say('Opening')
        webbrowser.open('https://open.spotify.com/track/16kiQQ4BoLHDyj5W2fkfNK?si=b966e90d1d7740a5')
        engine.runAndWait()    
    elif 'open instagram' in command:
        engine.say('Opening Instagram')
        webbrowser.open('https://www.instagram.com/')
        engine.runAndWait()
    elif 'show top movies' in command:
        engine.say('Opening')
        webbrowser.open('https://www.imdb.com/chart/top/')
        engine.runAndWait()
    elif 'show headphones to buy' in command:
        engine.say('showing in amazon')
        webbrowser.open('https://www.amazon.in/s?k=headphones&crid=3KC69TMYGGPVJ&sprefix=h%2Caps%2C211&ref=nb_sb_ss_w_hit-vc-lth_headphones_k5_6_1')
        engine.runAndWait()
    elif 'open pinterest' in command:
        engine.say('Opening pinterest')
        webbrowser.open('https://in.pinterest.com/')
        engine.runAndWait()
    elif 'show my location' in command:
        engine.say('okay showing')
        webbrowser.open('https://www.google.com/maps/@30.8928262,75.8366795,14z?entry=ttu')
        engine.runAndWait()
    elif 'open whizrobo' in command:
        engine.say('Opening Whizrobo Webpage')
        webbrowser.open('https://whizrobo.com/')
        engine.runAndWait()
    elif 'open translater' in command:
        engine.say('okay sure')
        webbrowser.open('https://translate.google.com/?sl=auto&tl=en&op=translate')
        engine.runAndWait()
    elif 'i want to search something through camera' in command:
        engine.say('Opening lens to search')
        webbrowser.open('https://lens.google/#cta-section')

        engine.runAndWait()
    
    elif 'search movie' in command:
        engine.say('What movie would you like to search for?')
        engine.runAndWait()
        movie = listen_for_command()
        engine.say(f'Searching for {movie}')
        webbrowser.open(f'https://www.google.com/search?q={movie}+movie')
        engine.runAndWait()
    elif 'increase volume' in command:
        engine.say('Increasing volume')
        os.system("nircmd.exe changesysvolume 2000")  
        engine.runAndWait()
    elif 'close tabs' in command:
        engine.say('Closing tabs')
        pyautogui.hotkey('ctrl', 'w') 
        engine.runAndWait()
    else:
        engine.say('Sorry, I did not understand that command')
        engine.runAndWait()

def listen_for_command():
    with sr.Microphone() as source:
        print('Listening...')
        engine.say('Listening...')
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio, language='en-US')
            print(f'You said: {command}')
            return command
        except sr.UnknownValueError:
            print('Sorry, I did not understand that')
            engine.say('Sorry, I did not understand that')
            engine.runAndWait()
        except sr.RequestError as e:
            print(f'Error: {e}')
            engine.say(f'Error: {e}')
            engine.runAndWait()
    return ''

if __name__ == '__main__':
    
    while True:
        command = listen_for_command()
        handle_command(command)
        engine.runAndWait()