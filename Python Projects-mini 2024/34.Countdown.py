import time

def countdown(minutes):
    """
    Performs a countdown from the given number of minutes to zero.
    Prints the remaining time every second.
    """
    # Convert minutes to total seconds
    total_seconds = int(minutes * 60)  # Convert to integer to handle fractional minutes correctly

    while total_seconds:
        # Calculate minutes and seconds
        mins, secs = divmod(total_seconds, 60)
        # Format time as MM:SS
        time_format = f'{mins:02}:{secs:02}'
        print(time_format, end='\r')  # Overwrite the current line in the console
        time.sleep(1)
        total_seconds -= 1

    print('Time is up!')

if __name__ == '__main__':
    countdown(0.5)  # Example usage: countdown from 0.5 minutes (30 seconds)
