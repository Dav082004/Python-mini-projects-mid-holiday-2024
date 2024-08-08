import os
from concurrent.futures import ThreadPoolExecutor

def search_files(file_name, initial_path):
    """
    Searches for a file in the specified directory and its subdirectories.
    """
    def search_in_directory(path):
        """
        Searches for the file in a given directory.
        """
        print(f'Searching in directory: {path}')
        
        for concurrent_path, _, files in os.walk(path):
            if file_name in files:
                return os.path.join(concurrent_path, file_name)
        return None
    
    # Use ThreadPoolExecutor to perform the search in parallel
    with ThreadPoolExecutor() as executor:
        # Submit the search task to the executor
        result = list(executor.map(search_in_directory, [initial_path]))
    
    # Filter out any None results
    results = [res for res in result if res is not None]

    # Return the first result if any, otherwise return None
    return results[0] if results else None

# Define the file name to search and the initial directory path
file_name_to_search = 'ejemplo.txt'
initial_path_to_search = '/home/user/Desktop'  # Update this path to your target directory

# Perform the search
found_path = search_files(file_name_to_search, initial_path_to_search)

# Print the result of the search
if found_path:
    print(f'El archivo {file_name_to_search} se ha encontrado en la ruta {found_path}')
else:
    print(f'El archivo {file_name_to_search} no se encontró en el sistema')
