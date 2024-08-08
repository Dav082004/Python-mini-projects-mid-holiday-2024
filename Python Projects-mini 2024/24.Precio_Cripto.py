import requests

def get_crypto_price(cryptocurrency):
    """
    Retrieves the price of a specified cryptocurrency in USD.
    """
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={cryptocurrency}&vs_currencies=usd'
    
    try:
        # Send a GET request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the JSON response
        data = response.json()
        
        # Extract the price of the cryptocurrency in USD
        price = data.get(cryptocurrency, {}).get('usd')
        return price
    except requests.RequestException as e:
        print(f'Error al hacer la solicitud: {e}')
        return None

def main():
    cryptocurrency = input('Ingrese el nombre de la criptomoneda: ').lower()
    price = get_crypto_price(cryptocurrency)

    if price is not None:
        print(f'El precio de {cryptocurrency.capitalize()} es ${price}')
    else:
        print('No se pudo obtener el precio.')

if __name__ == '__main__':
    main()
