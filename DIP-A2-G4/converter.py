from PIL import Image, ImageOps

# creating an og_image object
og_image = Image.open("./B2DBy.jpg")

# applying grayscale method
gray_image = ImageOps.grayscale(og_image)
gray_image.save('B2DBy.jpg')