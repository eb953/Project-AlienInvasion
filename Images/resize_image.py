from PIL import Image

image = Image.open('/Users/ericbanavong/Project-AlienInvasion/Project-AlienInvasion/Images/IMG_6506.jpeg')

image.thumbnail((50,50))

image.save('image_thumbnail.jpeg')

print(image)
