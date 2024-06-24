import os
from pipes import quote
import re
import sqlite3
import struct
import subprocess
import time
import webbrowser
from playsound import playsound
import eel
import pyaudio
import pyautogui
from engine.command import speak
from engine.config import ASSISTANT_NAME
# Playing assiatnt sound function
import pywhatkit as kit
import pvporcupine
from hugchat import hugchat
from engine.helper import extract_yt_term, remove_words
from pyautogui import *
import wikipedia
from pywikihow import search_wikihow
from engine.command import takecommand


con = sqlite3.connect("jarvis.db")
cursor = con.cursor()   

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

    
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()

    if app_name != "":

        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")

def findContact(query):
    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])

        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0
    
    
def whatsApp(mobile_no, message, flag, name):
    if flag == 'message':
        target_tab = 12
        jarvis_message = "Message sent successfully to " + name

    elif flag == 'call':
        target_tab = 7
        message = ''
        jarvis_message = "Calling to " + name

    elif flag == 'video call':
        target_tab = 6
        message = ''
        jarvis_message = "Starting video call with " + name

    # Remove any leading quotation marks from the message
    message = message.lstrip('"')

    # Encode the message for URL
    encoded_message = quote(message)

    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)

    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(jarvis_message)

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)

def hotword():

    porcupine_1 = None
    porcupine_2 = None
    porcupine_3 = None
    #porcupine_4 = None
    audio_stream = None
    audio=None
    try:
        # Initialize Porcupine with the access key and the path to the keyword files
        porcupine_1 = pvporcupine.create(access_key="o+UhTQPbpyC70LtwZxB9A+fOvA0T4rbd18bu/Nw1RfQTSP1OJqjQ+w==", keyword_paths=["models\\Hey-Titan_en_windows_v3_0_0.ppn"])
        porcupine_2 = pvporcupine.create(access_key="o+UhTQPbpyC70LtwZxB9A+fOvA0T4rbd18bu/Nw1RfQTSP1OJqjQ+w==", keyword_paths=["models\\Wake-Up-Titan_en_windows_v3_0_0.ppn"])
        porcupine_3 = pvporcupine.create(access_key="o+UhTQPbpyC70LtwZxB9A+fOvA0T4rbd18bu/Nw1RfQTSP1OJqjQ+w==", keyword_paths=["models\\Stop-Titan_en_windows_v3_0_0.ppn"])
        #porcupine_4 = pvporcupine.create(access_key="whu87MqFLpyMaXSd1sQVLi5/LRn7K1bh54i5kpqaiEIp1kC7Rxswzw==", keyword_paths=["models\\Stop-Titan_en_windows_v3_0_0.ppn"])
        # Initialize PyAudio for audio input
        audio = pyaudio.PyAudio()
        
        audio_stream = audio.open(
            rate=porcupine_1.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine_1.frame_length
        )

        # Loop for streaming and detecting hotword
        while True:
            pcm = audio_stream.read(porcupine_1.frame_length)
            pcm = struct.unpack_from("h" * porcupine_1.frame_length, pcm)

            # Process the audio data for keyword detection
            keyword_index_1 = porcupine_1.process(pcm)
            keyword_index_2 = porcupine_2.process(pcm)
            keyword_index_3 = porcupine_3.process(pcm)
            # keyword_index_4 = porcupine_4.process(pcm)
            # Check if any keyword is detected
            if keyword_index_1 >= 0:
                print("Hotword detected: Hey Titan")
                # Perform actions for "Wake-up Titan" hotword
                pyautogui.keyDown("win")
                pyautogui.press("j")
                time.sleep(0.5)  # Adjust this delay as needed
                pyautogui.keyUp("win")

            elif keyword_index_2 >= 0:
                print("Hotword detected: Wake Up Titan")
                # Perform actions for "Titan" hotword
                pyautogui.keyDown("win")
                pyautogui.press("j")
                time.sleep(0.5)  # Adjust this delay as needed
                pyautogui.keyUp("win")

            elif keyword_index_3 >= 0:
                print("Hotword detected: Stop Titan")
                # Perform actions for "Hey Titan" hotword
                eel.showhood()
                break  
    except KeyboardInterrupt:
        print("Interrupted by user")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up resources
        if porcupine_1 is not None:
            porcupine_1.delete()
        if porcupine_2 is not None:
            porcupine_2.delete()
        if porcupine_3 is not None:
            porcupine_3.delete()
        if audio_stream is not None:
            audio_stream.close()
        if audio is not None:
            audio.terminate()


def GoogleSearch(query):
    query = query.replace("Titan","")
    query = query.replace("what is","")
    query = query.replace("how to","")
    query = query.replace("what is","")
    query = query.replace(" ","")
    query = query.replace("what do you mean by","")

    writeab = str(query)

    oooooo = open('E:\\titan1\\titan\\Data.txt','a')
    oooooo.write(writeab)
    oooooo.close()

    Query = str(query)

    kit.search(Query)
    kit.search(query)
    result = wikipedia.summary(query,1)
    speak(result)
    if 'how to' in Query:

        max_result = 1

        how_to_func = search_wikihow(query=Query,max_results=max_result)

        assert len(how_to_func) == 1

        how_to_func[0].print()

        speak(how_to_func[0].summary)

    else:

        search = wikipedia.summary(Query,2)

        speak(f": According To Your Search : {search}")
    
def YouTube(query):
    query = str(query)
    if 'search' in query:
        search_term = query.split('search', 1)[1].strip()
        search_url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.open(search_url)

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)

def WikipediaSearch(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("titan","")
        results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia..")
        print(results)
        speak(results)  

def calculator(expression):
    try:
        expression = expression.replace('x', '*').replace('X', '*')
        result = eval(expression)  # Evaluate the expression
        speak(f"The result is {result}")
    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, I couldn't evaluate the expression.")

#GPT BOT      
def chatBot(query, require_more_info=False):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)

    # Append "need more information" to the user input if required
    if require_more_info:
        user_input += " need more information"

    # Get the response from the chatbot
    response = chatbot.chat(user_input)
    
    # Convert the response to a string
    response_str = str(response)
    
    # Limit the response to 20 words
    response_words = response_str.split()[:20]
    truncated_response = ' '.join(response_words)
    
    # Print and speak the truncated response
    print(truncated_response)
    speak(truncated_response)
    
    # Ask if more information is needed
    if len(response_words) < 20:
        return truncated_response  # Return the truncated response if it's already short
    else:
        while True:
            user_response = input("Need more information? (yes/no): ").lower()
            if user_response == "yes" or user_response == "no":
                break  # Exit the loop if a valid response is provided
            else:
                print("Invalid response. Please enter 'yes' or 'no'.")
        
        if user_response == "yes":
            return chatBot(query, require_more_info=True)  # Recursively call chatBot with require_more_info=True
        else:
            return truncated_response  # Return the truncated response if the user doesn't need more information



#SCHEDULE TASK
def scheduleTask():
    tasks = []

    eel.DisplayMessage('Do you want to clear old tasks? (Please say YES or NO)')
    speak("Do you want to clear old tasks? (Please speak YES or NO)")
    query = takecommand().lower()

    if "yes" in query:
        with open("tasks.txt", "w") as file:
            file.write("")
        eel.DisplayMessage('Old tasks cleared.')
        speak("Old tasks cleared.")
    else:
        eel.DisplayMessage('Keeping old tasks.')
        speak("Keeping old tasks.")

    eel.DisplayMessage('How many tasks do you want to schedule?')
    speak("How many tasks do you want to schedule?")
    no_tasks = int(takecommand())
    
    for i in range(no_tasks):
        eel.DisplayMessage(f'Enter task {i+1}:')
        speak(f'Enter task {i+1}:')
        task = takecommand().strip()
        tasks.append(task)

    with open("tasks.txt", "w") as file:
        for i, task in enumerate(tasks):
            file.write(f"{i+1}. {task}\n")

from googletrans import Translator

def translate_text(text, dest_lang='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=dest_lang)
    return translated_text.text

#MAIL FEATURE
# Constants for SMTP configuration
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sqlite3

import eel

from engine.command import speak


smtp_server = 'smtp.gmail.com'
smtp_port = 587


def send_email(subject, message, recipient_name):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('jarvis.db')
        cursor = conn.cursor()

        # Query the database to fetch the email address associated with the provided name
        cursor.execute("SELECT email FROM gmail WHERE LOWER(name)=?", (recipient_name,))
        recipient_email = cursor.fetchone()

        if recipient_email:
            recipient_email = recipient_email[0]  # Extract the email address from the tuple

            # Email configuration
            sender_email = 's.s.dhanushsiva0101@gmail.com'  # Your email address
            sender_password = 'lvyg ikup mpyk bmfr'      # Your email password

            # Create a MIMEMultipart object to represent the email message
            email = MIMEMultipart()
            email['From'] = sender_email
            email['To'] = recipient_email
            email['Subject'] = subject

            # Attach the email body
            email.attach(MIMEText(message, 'plain'))

            # Establish a connection with the SMTP server
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  # Start TLS encryption
                server.login(sender_email, sender_password)  # Login to the email server
                server.sendmail(sender_email, recipient_email, email.as_string())  # Send the email

            print("Email sent successfully!")
            eel.DisplayMessage('Email sent succeessfully!')
            speak("Email sent succeessfully!")
        else:
            print("Recipient not found in contacts.")

        # Close the database connection after use
        conn.close()

    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Please check your email credentials.")
    except smtplib.SMTPException as e:
        print(f"An error occurred while sending the email: {str(e)}")