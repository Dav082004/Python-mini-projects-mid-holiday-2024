import random

# Initialize game variables
vida = 100
puntuacion = 0
armadura = 50

def jugar_juego():
    """Main game loop."""
    while vida > 0:
        print('\nTe encuentras en un pasillo del castillo.')
        mostrar_estado()
        opcion = input('¿Qué deseas hacer?\n1. Entrar en una habitación\n2. Seguir explorando\n3. Consultar tu estado\n4. Salir del juego\nElige una opción (1/2/3/4): ')

        if opcion == '1':
            explorar_habitacion()
        elif opcion == '2':
            evento_aleatorio()
        elif opcion == '3':
            mostrar_estado()
        elif opcion == '4':
            print('Decidiste salir del juego.')
            break
        else:
            print('Opción no válida. Por favor, elige una opción correcta.')

        if vida <= 0:
            print('\nPerdiste.')
            mostrar_estado()
        elif puntuacion >= 100:
            print('¡Felicidades! Has ganado el juego.')
            mostrar_estado()
            break
        elif armadura <= 0:
            print('\nArmadura dañada, perdiste.')
            mostrar_estado()
            break

def mostrar_estado():
    """Display the current status of the player."""
    print(f'Vida: {vida}')
    print(f'Puntuación: {puntuacion}')
    print(f'Armadura: {armadura}\n')

def explorar_habitacion():
    """Explore the room and handle encounters."""
    global vida
    enemigo_presente = random.choice([True, False])

    if enemigo_presente:
        print('Enemigo encontrado en la habitación.')
        hablar_con_profesor()
    else:
        print('La habitación está vacía. Sigues explorando.')

def hablar_con_profesor():
    """Interact with a professor and solve a math problem."""
    global vida, puntuacion
    print('Te encuentras con un profesor de matemáticas en la habitación.')
    print('Te hace una pregunta matemática.')

    respuesta_correcta = False

    while not respuesta_correcta and vida > 0:
        multiplicador = random.randint(1, 10)
        multiplicando = random.randint(1, 10)
        respuesta_esperada = multiplicador * multiplicando

        respuesta = input(f'¿Cuánto es {multiplicador} x {multiplicando}?: ')

        if respuesta.isdigit() and int(respuesta) == respuesta_esperada:
            print('¡Respuesta correcta!')
            puntuacion += 20
            respuesta_correcta = True
        else:
            print('Respuesta incorrecta, pierdes 10 de vida. El profesor te da otra oportunidad.')
            vida -= 10

def evento_aleatorio():
    """Handle random events that occur during exploration."""
    global vida, puntuacion, armadura

    evento = random.choice(['Encontraste un cofre con tesoros',
                            'Te caiste y perdiste algo de vida',
                            'Encontraste un atajo'])

    if evento == 'Encontraste un cofre con tesoros':
        print('Encontraste un cofre con tesoros. Obtuviste 20 puntos.')
        puntuacion += 20
    elif evento == 'Te caiste y perdiste algo de vida':
        print('Te caiste y pierdes 10 de vida y armadura.')
        vida -= 10
        armadura -= 10
    elif evento == 'Encontraste un atajo':
        print('Encontraste un atajo que te lleva a la habitación del jefe final.')
        jugar_piedra_papel_tijeras()

def jugar_piedra_papel_tijeras():
    """Play rock-paper-scissors with the final boss."""
    global puntuacion
    print('\nLlegaste a la habitación del jefe final.')
    print('El jefe final te desafía a un juego de piedra, papel o tijeras.')

    opciones = ['piedra', 'papel', 'tijeras']
    
    while True:
        eleccion_jugador = input('Elige tu jugada (piedra/papel/tijeras): '.lower())
        eleccion_jefe = random.choice(opciones)

        print(f'El jefe eligió {eleccion_jefe}.')

        if eleccion_jugador == eleccion_jefe:
            print('Es un empate, intenta de nuevo.')
        elif (eleccion_jugador == 'piedra' and eleccion_jefe == 'tijeras') or \
             (eleccion_jugador == 'papel' and eleccion_jefe == 'piedra') or \
             (eleccion_jugador == 'tijeras' and eleccion_jefe == 'papel'):
            print('Ganaste, derrotaste al jefe final.')
            puntuacion += 100
            print('Pasaste el juego.')
            break
        else:
            print('Perdiste contra el jefe final.')
            print('Regresas al principio.')
            reiniciar_juego()
            break

def reiniciar_juego():
    """Reset game variables to restart the game."""
    global vida, puntuacion, armadura
    vida = 100
    puntuacion = 0
    armadura = 50

# Start the game
jugar_juego()
