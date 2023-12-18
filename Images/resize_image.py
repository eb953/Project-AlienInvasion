from PIL import Image

image = Image.open('/Users/ericbanavong/Project-AlienInvasion/Project-AlienInvasion/Images/Frida1.jpeg')

image.thumbnail((50,50))

image.save('Frida1_thumbnail.jpeg')

print(image)
