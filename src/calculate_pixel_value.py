# ==================================================================================================== #
#
# A helper function to calculate whether the pixel is within the set or not
# also returns the number of iteration before escape happened for coloring purposes
#
# ==================================================================================================== #

import cmath

def calculate_pixel_value(x, y, x_min, y_max, pixel_step, max_iterations, escape_threshold):
	# Translate the pixel values to numerical values
	x_value = x_min + (x * pixel_step)
	y_value = y_max - (y * pixel_step)

	# Create the function variables with c as a complex number
	c = complex(x_value, y_value)
	z = 0

	# Begin the loop
	for i in range(max_iterations):
		z = (z ** 2) + c

		# Check for crossing the threshold on every iteration and return data if escaped
		if abs(z) > escape_threshold:
			return False, i

	# If return hasn't been achieved up until now means the umber is within the set
	return True, 0


