from PIL import Image

image = Image.open('Images/IMG_6719.jpeg')

image.thumbnail((75,75))

image.save('E2_thumbnail.jpeg')

print(image)
