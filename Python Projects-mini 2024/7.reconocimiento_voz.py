import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the microphone
mic = sr.Microphone()

try:
    # Use the microphone as the source for input
    with mic as source:
        print("Listening...")
        # Adjust for ambient noise and record audio
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    # Recognize speech using Google Web Speech API
    text = recognizer.recognize_google(audio, language='es')
    
    # Print the recognized text
    print(f'Has dicho: {text}')
    
except sr.UnknownValueError:
    # Handle cases where the speech is unintelligible
    print("Google Speech Recognition could not understand the audio.")
except sr.RequestError as e:
    # Handle cases where there is an issue with the API request
    print(f"Could not request results from Google Speech Recognition service; {e}")
