import requests
from bs4 import BeautifulSoup

def check_word_in_url(url, word):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        if word.lower() in soup.get_text().lower():
            print(f'Se encuentra la palabra "{word}" en la URL: {url}')
        else:
            print(f'La palabra "{word}" no se encuentra en la URL: {url}')
    else:
        print(f'Error: No se puede acceder a la página {url}. Código de estado: {response.status_code}')

def main():
    url = 'https://elcomercio.pe/'
    word = 'para'
    
    for num in range(15, 30):
        check_word_in_url(url, word)

if __name__ == '__main__':
    main()
