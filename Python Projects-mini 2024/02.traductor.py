# Install the required library:
# pip install translate

from translate import Translator

def initialize_translator(from_lang='spanish', to_lang='english'):
    """
    Initialize the translator with the given source and target languages.
    """
    return Translator(from_lang=from_lang, to_lang=to_lang)

def translate_text(translator, text):
    """
    Translate the given text using the provided translator.
    """
    if not text.strip():
        return "Input text is empty. Please enter some text to translate."
    return translator.translate(text)

def translate_from_input():
    """
    Prompt the user to enter text to translate and display the translation.
    """
    from_lang = 'spanish'
    to_lang = 'english'
    translator = initialize_translator(from_lang, to_lang)
    
    txt = input('Que es lo que quieres traducir? ')
    translated_text = translate_text(translator, txt)
    print(f'Texto traducido: {translated_text}')

def main():
    """
    Main function to execute the translation process.
    """
    translate_from_input()

if __name__ == "__main__":
    main()
