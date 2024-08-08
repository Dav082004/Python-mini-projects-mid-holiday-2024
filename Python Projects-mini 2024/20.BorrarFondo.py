from rembg import remove
from PIL import Image

# Open the image file
image = Image.open('imagenFondo.png')

# Remove the background from the image
image_no_bg = remove(image)

# Save the image with the background removed
image_no_bg.save('imagensinfondo.png')

# Print confirmation message
print('Fondo eliminado')