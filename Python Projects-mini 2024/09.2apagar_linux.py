import os

def main():
    # Ask the user if they want to shut down the computer
    shutdown = input('Do you want to shut down the computer? (yes/no): ').strip().lower()
    
    # Check the user's response
    if shutdown in ['yes', 'si']:
        try:
            # Execute the shutdown command
            os.system('shutdown now')
        except Exception as e:
            print(f"An error occurred while trying to shut down the computer: {e}")
    elif shutdown in ['no', 'nope']:
        print("Shutdown canceled.")
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()

#sudo python3 script_name.py
