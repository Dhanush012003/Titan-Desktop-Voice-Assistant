import os
import pyautogui
import pyttsx3
import speech_recognition as sr
import eel
import time
import re
from keyboard import press
import keyboard
import pyautogui
import speech_recognition as sr
from engine.keyboard import volumedown,volumeup
import sys



def speak(text):
    text= str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening....')
        eel.DisplayMessage('Listening....')
        r.pause_threshold = 0.5  # Shorter pause threshold for quicker response
        r.adjust_for_ambient_noise(source, duration=0.5)  # Shorter duration for adjusting to ambient noise quickly

        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=6)
        except sr.WaitTimeoutError:
            print("No audio received. Going to eel.ShowHood()")
            eel.ShowHood()
            return ""

    try:
        print('Recognizing')
        eel.DisplayMessage('Recognizing....')
        query = r.recognize_google(audio, language='en-in', show_all=False)  # Use more accurate recognition model
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)

    except Exception as e:
        print("Error:", str(e))
        return ""
    
    return query.lower()

@eel.expose
def allCommands(message=1):
        
        if message == 1:
            query = takecommand()
            print(query)
            eel.senderText(query)
        else:
            query = message
            eel.senderText(query)

        try:
            if "open" in query:
                from engine.features import openCommand
                openCommand(query)

            elif "youtube" in query:
                if "search" in query:
                    query = query.replace("Titan", "")
                    query = query.replace("youtube", "")
                    from engine.features import YouTube
                    YouTube(query)
                else:
                    from engine.features import PlayYoutube
                    PlayYoutube(query)
            elif 'wikipedia' in query:
                from engine.features import WikipediaSearch
                WikipediaSearch(query)
            
            elif 'google search' in query or 'search' in query or 'how to' in query:
                from engine.features import GoogleSearch
                GoogleSearch(query)

            elif "send message" in query or "phone call" in query or "video call" in query:
                from engine.features import findContact, whatsApp
                flag = ""
                contact_no, name = findContact(query)
                if contact_no != 0:

                    if "send message" in query or "message" in query:
                        flag = 'message'
                        speak("what message to send")
                        query = takecommand()
                    elif "phone call" in query:
                        flag = 'call'
                    else:
                        flag = 'video call'
                        
                    whatsApp(contact_no, query, flag, name)

            elif "mute" in query:
                pyautogui.press("m")
                speak("video muted")

            elif "volume up" in query:
                speak("Turning volume up,")
                volumeup()

            elif "volume down" in query:
                speak("Turning volume down,")
                volumedown()
                
            elif 'minimize' in query or 'minimise' in query:
                pyautogui.moveTo(1786,7)
                pyautogui.leftClick()
        
            elif 'maximize' in query or ' maximise' in query:
                pyautogui.moveTo(1822,5)
                pyautogui.leftClick()
            elif 'cut' in query or 'slice' in query:
                pyautogui.moveTo(1893,3)
                pyautogui.leftClick()
                
            elif "shutdown the system" in query or "turn off the system" in query:
                speak("Are You sure you want to shutdown")
                shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                os.system("shutdown /s /t 1")

            elif "screenshot" in query:
                     im = pyautogui.screenshot()
                     file_path = "E:\\titan\\Screenshots\\ss.jpg"
                     im.save(file_path)
            elif "take a photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(3)
                    speak("SMILE")
                    pyautogui.press("enter")

            elif 'pause' in query:
                press('space bar')

            elif 'resume' in query or 'play' in query:
                press('space bar')

            elif 'full screen' in query:
                press('f')

            elif 'movie screen' in query:
                press('t')

            elif 'forward' in query:
                press('l')

            elif 'backward' in query:
                press('j')

            elif 'speed increase' in query:
                keyboard.press_and_release('SHIFT + .')

            elif 'slow motion' in query:
                keyboard.press_and_release('SHIFT + ,')

            elif 'previous' in query:
                keyboard.press_and_release('SHIFT + p')

            elif 'next' in query:
                keyboard.press_and_release('SHIFT + n')

            elif 'unmute' in query:
                press('m')
            elif 'calculate' in query or 'calculator' in query:
                from engine.features import calculator
                expression = re.search(r'calculate (.+)', query).group(1)
                calculator(expression)

            elif 'new tab' in query:
                pyautogui.hotkey('ctrl', 't')
                time.sleep(1)
            elif 'close tab' in query:
                pyautogui.hotkey('ctrl', 'w')
                time.sleep(1) 
            elif 'new window' in query:
                pyautogui.hotkey('ctrl', 'n')
                time.sleep(1)  

            elif 'history' in query:
                pyautogui.hotkey('ctrl', 'h')
                time.sleep(1)

            elif 'download' in query:
                keyboard.press_and_release('ctrl + j')

            elif 'bookmark' in query:
                pyautogui.hotkey('ctrl', 'shift', 'o')
                time.sleep(1)

            elif 'incognito' in query or 'private tab' in query:
                pyautogui.hotkey('ctrl', 'shift', 'n')
                time.sleep(1)

            elif 'switch tab' in query:
                def switch_tab(tab_number):
                    pyautogui.hotkey('ctrl', str(tab_number))
                # Open a new tab (e.g., Ctrl + T)
                switch_tab(1)  # Switch to the first tab
                time.sleep(1)

            elif 'email' in query or 'gmail' in query or 'send a gmail' in query:
                from engine.features import send_email
                speak("To whom should I send the email?")
                to_email = takecommand().lower()
                eel.DisplayMessage(to_email)
                speak("What message should I send?")
                message = takecommand().lower()
                subject = "Test Email"
                send_email(subject, message, to_email)

            elif 'translate' in query or 'translation' in query:
                    from engine.features import translate_text
                    speak("Can you say what i need to translate")
                    original_text = takecommand().title()
                    translated_text = translate_text(original_text, dest_lang='en')
                    speak(translated_text)
                    
            elif "go to home" in query or "home" in query:
                    eel.ShowHood()

            elif "go to sleep" in query or "exit" in query or 'sign off' in query or 'bye bye' in query:
                        from engine.Chatbot import ChatterBot
                        reply = ChatterBot(query)
                        speak(reply)
                        sys.exit()  # Close the entire program
            elif "hi" in query or "hello" in query or"hey" in query or "hay" in query or "hello there" in query:
                        from engine.Chatbot import ChatterBot
                        reply = ChatterBot(query)
                        speak(reply)
            elif 'thanks' in query or 'thanks titan' in query or 'good' in query or'nice' in query:
                        from engine.Chatbot import ChatterBot
                        reply = ChatterBot(query)
                        speak(reply)   
            else:
                from engine.features import chatBot
                chatBot(query)
        except:
            print("error")

        eel.ShowHood()