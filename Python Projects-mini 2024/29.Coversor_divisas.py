import requests

API_KEY = ''  # Replace with your API key
URL = ''      # Replace with the URL for the exchange rates API

def get_rates():
    """
    Fetches the currency conversion rates from the API.
    """
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
        return data['conversion_rates']
    except requests.RequestException as e:
        print(f'ERROR: Unable to fetch exchange rates - {e}')
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    """
    Converts an amount from one currency to another using the provided rates.
    """
    if from_currency != 'USD':
        amount = amount / rates[from_currency]
    return amount * rates[to_currency]

def main():
    """
    Main function to handle user input and perform currency conversion.
    """
    rates = get_rates()
    if rates:
        try:
            amount = float(input('Introduce la cantidad que quieres convertir: '))
            from_currency = input('Introduce la divisa desde la cual conviertes: ').upper()
            to_currency = input('Introduce la divisa a la cual quieres convertir: ').upper()
            
            # Check if currencies are valid
            if from_currency not in rates or to_currency not in rates:
                print('ERROR: Moneda no válida')
                return

            result = convert_currency(amount, from_currency, to_currency, rates)
            print(f'{amount:.2f} {from_currency} es igual a {result:.2f} {to_currency}')
        except ValueError:
            print('ERROR: Cantidad no válida')

if __name__ == '__main__':
    main()
