from PIL import Image

image = Image.open('Images/Frida2.jpeg')

image.thumbnail((100,100))

image.save('Frida2_thumbnail.jpeg')

print(image)
