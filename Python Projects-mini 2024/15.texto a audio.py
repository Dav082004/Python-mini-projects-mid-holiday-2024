from gtts import gTTS

# Open the text file and read its content
try:
    with open('libro.txt', 'r', encoding='utf-8') as file:
        textBook = file.read()
except FileNotFoundError:
    print("Error: The file 'libro.txt' was not found.")
    exit()
except IOError as e:
    print(f"Error reading file: {e}")
    exit()

# Convert the text to speech
try:
    audio = gTTS(text=textBook, lang='es')
    audio.save('audiogenerado.mp3')
    print("Audio file 'audiolibro.mp3' has been created successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
