def calculate_reading_time_from_file(file_path):
    """
    Calculates the estimated reading time of the text file based on an average reading speed.
    """
    try:
        # Open the file and read its content
        with open(file_path, 'r', encoding='utf-8') as file:
            text_from_file = file.read()

        # Split the text into words and count them
        words = text_from_file.split()
        average_reading_speed = 200  # Average reading speed in words per minute

        # Calculate the reading time
        reading_time = len(words) / average_reading_speed

        print(f'Estimated reading time: {reading_time:.2f} minutes')
    except FileNotFoundError:
        print(f'Error: The file at {file_path} was not found.')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    file_path = input('Enter the path to the text file: ')
    calculate_reading_time_from_file(file_path)
