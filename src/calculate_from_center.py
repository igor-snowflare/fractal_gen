# ==================================================================================================== #
#
# Helper function that calculates variables based on center and spread values
#
# ==================================================================================================== #

def calculate_from_center(center_x, center_y, spread):
	x_max = center_x + spread
	x_min = center_x - spread
	y_max = center_y + spread
	y_min = center_y - spread

	return x_max, x_min, y_max, y_min