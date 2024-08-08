import cv2
from pyzbar.pyzbar import decode

def read_qr_code(image_path):
    # Read the image from the given path
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Decode the QR codes in the grayscale image
    decoded_objects = decode(gray_image)
    
    # Check if any QR codes are found
    if decoded_objects:
        # Iterate over the decoded objects
        for obj in decoded_objects:
            # Extract and decode the data from the QR code
            data = obj.data.decode('utf-8')
            print(f'Datos del código QR: {data}')
    else:
        print('No se encontraron códigos QR en la imagen')

# Specify the path to the image file
image_path = 'qr_prueba.png'

# Call the function to read the QR code
read_qr_code(image_path)
