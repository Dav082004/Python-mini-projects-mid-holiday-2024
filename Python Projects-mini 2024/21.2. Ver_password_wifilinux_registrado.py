import subprocess

# Ask the user to input the Wi-Fi profile name
perfil_red = input('Introduce el nombre del perfil de red WIFI: ')

try:
    # Run nmcli to get the connection information
    resultados = subprocess.check_output(['nmcli', '-s', '-g', '802-11-wireless-security.psk', 'connection', 'show', perfil_red],
                                         shell=False).decode('utf-8').strip()

    # Check if results are obtained
    if resultados:
        print(f'La contraseña de la red {perfil_red} es: {resultados}')
    else:
        print(f'No se pudo encontrar la contraseña para la red {perfil_red}')

except subprocess.CalledProcessError:
    # Handle errors in running the subprocess command
    print(f'No se pudo obtener la información del perfil {perfil_red}')
