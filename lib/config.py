# ==================================================================================================== #
#
# Configuration based on which the script will run
#
# ==================================================================================================== #

# Define left and right min and max values of the coordinate system -- these are the default values
x_max = 0.5
x_min = -2
y_max = 1
y_min = -1

# For centering on specific coordinates -- this will work only if custom_area is set to true
custom_area = False
center_x = -0.75
center_y = 0.16
spread = 0.005

# Define the image width (height will be calculated accordingly)
img_width = 1366

# Define the maximum number of iterations before the state of the pixel is fixed
max_iterations = 70

# Define the radius that will serve as escape threshold
escape_threshold = 2

# Pallete to be used - can be None for render in red channel only or catpuccin
selected_pallete = None
