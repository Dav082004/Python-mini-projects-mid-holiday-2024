import qrcode

def generate_qr_code(data, file_name='QRCode.png', box_size=10, border=4, fill_color="black", back_color="white"):
    """
    Generate a QR code image and save it to a file.
    
    Parameters:
    - data: The data to encode in the QR code.
    - file_name: The name of the file to save the QR code image (default is 'QRCode.png').
    - box_size: The size of each box in the QR code grid (default is 10).
    - border: The thickness of the border (default is 4).
    - fill_color: The color of the QR code (default is "black").
    - back_color: The background color of the QR code (default is "white").
    """
    try:
        # Create a QR code object
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=border
        )
        
        # Add data to the QR code
        qr.add_data(data)
        qr.make(fit=True)
        
        # Create the QR code image
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        
        # Save the image to a file
        img.save(file_name)
        print(f"QR code saved as '{file_name}'")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    url = input('Introducir la URL que quiere crear un QR: ')
    output_file = 'QRprueba.png'
    generate_qr_code(data=url, file_name=output_file)
