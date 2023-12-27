from PIL import Image

input_image = "input.jpg"
output_image = "output.jpg"
size = (200, 200)

image = Image.open(input_image)
image.thumbnail(size)
image.save(output_image)
