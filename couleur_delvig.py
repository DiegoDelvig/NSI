# Diego Delvig 1G7

from PIL import Image
from random import randint

width = 1000
height = 1000

im = Image.new('RGB', (width, height), (255, 255, 255))

couleurs = [
	(49, 203, 100),
	(53, 12, 87),
	(1, 90, 109),
	(77, 12, 2),
	(245, 201, 92),
	(43, 19, 26)
]

pixel_num = 0
while pixel_num < 100_000:

	coor = (randint(0, width - 1), randint(0, height - 1))
	current_pixel = im.getpixel(coor)

	if current_pixel == (255, 255, 255):
		im.putpixel(coor, couleurs[randint(0, len(couleurs) - 1)])
		pixel_num += 1

im.show()
