import requests

def shorten_url_isgd(original_url, custom_name):
    """
    Shortens a URL using the is.gd API and optionally provides a custom name for the shortened URL.
    """
    base_url = 'https://is.gd/create.php'

    params = {
        'format': 'json',
        'url': original_url,
        'short': custom_name
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        response_data = response.json()
        
        if 'shorturl' in response_data:
            return response_data['shorturl']
        else:
            print('ERROR: Failed to shorten the URL')
            return None
    except requests.RequestException as e:
        print(f'ERROR: An error occurred - {e}')
        return None

def main():
    original_url = input('Enter the URL to shorten: ')
    custom_name = input('Enter a custom name for the shortened URL (optional): ')
    
    # Shorten the URL
    shortened_url = shorten_url_isgd(original_url, custom_name)
    
    if shortened_url:
        print(f'Original URL: {original_url}')
        print(f'Shortened URL: {shortened_url}')

if __name__ == '__main__':
    main()
