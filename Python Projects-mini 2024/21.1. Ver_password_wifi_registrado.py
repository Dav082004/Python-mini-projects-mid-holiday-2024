import subprocess

# Ask the user to input the Wi-Fi profile name
perfil_red = input('Introduce el nombre del perfil de red WIFI: ')

try:
    # Run the netsh command to show the Wi-Fi profile details
    resultados = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', perfil_red, 'key=clear'],
                                         shell=True).decode('utf-8', errors='backslashreplace')

    # Check if the key content is in the results
    if 'Contenido de la clave' in resultados:
        # Iterate over each line in the results
        for line in resultados.split('\n'):
            # Find the line that contains the key content
            if 'Contenido de la clave' in line:
                # Extract the password from the line
                password = line.split(':')[1].strip()
                print(f'La contraseña de la red {perfil_red} es: {password}')
                break
    else:
        print(f'No se pudo encontrar la contraseña para la red {perfil_red}')

except subprocess.CalledProcessError:
    # Handle errors in running the subprocess command
    print(f'No se pudo obtener la información del perfil {perfil_red}')
