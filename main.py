# ==================================================================================================== #
#
# Main runner function
#
# ==================================================================================================== #

import time
from PIL import Image, ImageDraw
import lib.config as config
from src.calculate_pixel_value import calculate_pixel_value
from src.determine_pixel_color import determine_color
from src.calculate_from_center import calculate_from_center

def generate_fractal():
	# Recalculate starting variables if custom_area is set to true
	if config.custom_area:
		x_max, x_min, y_max, y_min = calculate_from_center(config.center_x, config.center_y, config.spread)
	else:
		x_max = config.x_max
		x_min = config.x_min
		y_max = config.y_max
		y_min = config.y_min

	# Calculate the extrapolated values
	width_size = abs(x_max - x_min)
	height_size = abs(y_max - y_min)
	img_height = round((config.img_width * height_size)/width_size)

	# Important to determine to which numerical values will the pixel objects default to
	pixel_step = width_size/config.img_width

	# Debug message
	print("Variable calculation completed with the following parameters:")
	print(f"Image Width: {config.img_width}px")
	print(f"Image Height: {img_height}px")
	print(f"Pixel Step: {pixel_step}")

	# Generate a blank image
	output = Image.new("RGB", (config.img_width, img_height))
	drawer = ImageDraw.Draw(output)

	# Calculate the data
	for y in range(img_height):
		pixel_row = list()
		for x in range(config.img_width):
			in_set, escape_count = calculate_pixel_value(x, y, x_min, y_max, pixel_step, config.max_iterations, config.escape_threshold)
			if not in_set:
				color_value = determine_color(escape_count, config.max_iterations, config.selected_pallete)
				drawer.point([x, y], color_value)

	# Determine the image name
	img_name = str(round(time.time()))
	output.save(f"outputs/{img_name}.png")

	print(f"Generated render with file name of {img_name}.png in the outputs/ directiory")


if __name__ == '__main__':
	generate_fractal()


	