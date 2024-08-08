# Install the required libraries:
# pip install SpeechRecognition pyttsx3 pyaudio

import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def talk():
    """
    Capture audio from the microphone and convert it to text using Google's speech recognition service.
    """
    mic = sr.Microphone()
    
    # Adjust the recognizer settings for better performance
    recognizer.pause_threshold = 0.5  # Reduce the pause threshold for faster response
    recognizer.energy_threshold = 300  # Set a fixed energy threshold
    recognizer.dynamic_energy_threshold = False  # Disable dynamic energy threshold adjustment

    with mic as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        # Recognize speech using Google
        text = recognizer.recognize_google(audio, language='es-ES')
        print(f'You said: {text}')
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def search_amazon():
    """
    Prompts the user for a search query and opens Amazon with the search results.
    """
    engine.say('What do you want to buy on Amazon?')
    engine.runAndWait()
    query = talk()
    if query:
        webbrowser.open(f'https://www.amazon.es/s?k={query}')

def search_google():
    """
    Prompts the user for a search query and opens Google with the search results.
    """
    engine.say('What do you want to search on Google?')
    engine.runAndWait()
    query = talk()
    if query:
        webbrowser.open(f'https://www.google.com/search?q={query}')

def play_youtube():
    """
    Prompts the user for a search query and opens YouTube with the search results.
    """
    engine.say('What do you want to watch on YouTube?')
    engine.runAndWait()
    query = talk()
    if query:
        webbrowser.open(f'https://www.youtube.com/results?search_query={query}')

# Main logic
try:
    user_command = talk()
    if 'amazon' in user_command:
        search_amazon()
    elif 'google' in user_command:
        search_google()
    elif 'youtube' in user_command:
        play_youtube()
    else:
        print("Command not recognized.")
except AttributeError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
