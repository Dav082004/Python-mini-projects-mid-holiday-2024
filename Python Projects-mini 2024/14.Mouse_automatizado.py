import pyautogui as botMouse
import webbrowser
import time
import keyboard  # pip install keyboard

def main():
    # Open the specified URL in the default web browser
    webbrowser.open('https://www.youtube.com/@YouTube')
    
    print('Script iniciado. Presiona "q" para detenerlo.')
    
    try:
        while True:
            # Define the coordinates to move to
            x = 671
            y = 517

            # Move the mouse to the specified coordinates
            botMouse.moveTo(x, y, duration=0.5)
            # Wait for a few seconds
            time.sleep(4)
            # Click at the current position
            botMouse.click()
            
            # Check for a key press to stop the loop
            if keyboard.is_pressed('q'):  # Press 'q' to quit the loop
                print('Stopping the script.')
                break
    except KeyboardInterrupt:
        print('Script interrupted by user.')

if __name__ == '__main__':
    main()
