# ==================================================================================================== #
#
# Main runner function
#
# ==================================================================================================== #

import time
from PIL import Image, ImageDraw
from config import *
from calculate_pixel_value import calculate_pixel_value

def generate_fractal():
	# Calculate the extrapolated values
	width_size = abs(x_max - x_min)
	height_size = abs(y_max - y_min)
	img_height = round((img_width * height_size)/width_size)

	# Important to determine to which numerical values will the pixel objects default to
	pixel_step = width_size/img_width

	# Debug message
	print("Variable calculation completed with the following parameters:")
	print(f"Image Width: {img_width}px")
	print(f"Image Height: {img_height}px")
	print(f"Pixel Step: {pixel_step}")

	# Generate a blank image
	output = Image.new("RGB", (img_width, img_height))
	drawer = ImageDraw.Draw(output)

	# Calculate the data
	for y in range(img_height):
		pixel_row = list()
		for x in range(img_width):
			in_set, escape_count = calculate_pixel_value(x, y, x_min, y_max, pixel_step, max_iterations, escape_threshold)
			if not in_set:
				escape_ratio = escape_count/max_iterations
				color_value = round(255 * escape_ratio)
				pixel_color = (color_value, color_value, color_value)
				drawer.point([x, y], color_value)

	# Determine the image name
	img_name = str(round(time.time()))
	output.save(f"outputs/{img_name}.png")


if __name__ == '__main__':
	generate_fractal()


	