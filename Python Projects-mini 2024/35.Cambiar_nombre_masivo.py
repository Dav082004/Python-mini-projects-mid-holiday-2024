import os

def change_names(directory_path, prefix):
    """
    Renames all files in the specified directory by adding a prefix and a counter to each file name.
    """
    try:
        # List all files in the directory
        files = os.listdir(directory_path)
        for counter, file_name in enumerate(files):
            # Split the file name and extension
            name, extension = os.path.splitext(file_name)
            # Create the new file name
            new_name = f'{prefix}_{counter}{extension}'
            # Rename the file
            os.rename(os.path.join(directory_path, file_name), os.path.join(directory_path, new_name))
            print(f'{file_name} -> {new_name}')
    
    except FileNotFoundError:
        print(f'Error: The directory {directory_path} does not exist.')
    except PermissionError:
        print(f'Error: Permission denied to access {directory_path}.')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    # Define the directory path and prefix
    directory_path = 'C:/Users/Usuario/Desktop/...'  # Adjust the path as needed
    prefix = 'image'
    
    # Call the function to change file names
    change_names(directory_path, prefix)
