# ==================================================================================================== #
#
# Function for determining pixel color for stylizing the image
#
# ==================================================================================================== #

from palletes import palletes_out

def determine_color(escape_count, max_iterations, pallete=None):
	escape_ratio = escape_count/max_iterations

	# With no pallete provided, a default render in red will be generated
	if pallete == None:
		color_value = round(255 * escape_ratio)
		pixel_color = (color_value, 0, 0)
		return pixel_color

	# Otherwise we need to chose and modify provided colors
	else:
		target_pallete = palletes_out[pallete]
		target_index = min(round(len(target_pallete) * escape_ratio), len(target_pallete) - 1)
		red, green, blue = target_pallete[target_index]

		pixel_color = (
			round(red * escape_ratio),
			round(blue * escape_ratio),
			round(green * escape_ratio),
			)

		return pixel_color
