import secrets  # Import the secrets module for better randomness

# Define the set of characters for the password
chars = '¡¿?`+^*Ç¨*¨1234567890qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM,.-•· ̣;::_!"·$%&/()='

def generate_password(length):
    """Generate a random password of the given length."""
    if length <= 0:
        raise ValueError("Password length must be greater than 0")
    
    # Generate the password using secrets.choice for cryptographic security
    return ''.join(secrets.choice(chars) for _ in range(length))

try:
    # Get the desired length for the password from the user
    lengthPW = int(input('¿Qué longitud quieres para tu contraseña? '))
    
    # Generate and print the password
    password = generate_password(lengthPW)
    print(f'La contraseña generada es: {password}')

except ValueError as e:
    print(f'Error: {e}')
