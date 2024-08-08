import mysql.connector  # Corrected import statement

def insert_user(name, age):
    """
    Inserts a new user record into the 'usuarios' table.
    """
    try:
        # Establish the connection to the database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bbdd_prueba'
        )
        
        cursor = connection.cursor()
        
        # Define the new user data and SQL query
        new_user = (name, age)
        query = 'INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)'
        
        # Execute the query and commit the changes
        cursor.execute(query, new_user)
        connection.commit()
        
        print('Record was successfully inserted')
        
    except mysql.connector.Error as err:
        print(f'Error: {err}')
        
    finally:
        # Close the database connection
        cursor.close()
        connection.close()

if __name__ == '__main__':
    # Example usage
    insert_user('Juan', 30)
