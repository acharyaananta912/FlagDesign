import numpy as np
import matplotlib.pyplot as plt

def make_sun(width, fill_color, line_width):
    """This function creates the Sun of the lower triangle of the Nepali flag.
    All the dimensions are according to the constitution of Nepal.
    Parameters: width of the flag
    Output: figure of the Sun for the flag. """
    
    # Create two circles: one bigger and one smaller
    # In the Nepali flag, the sun has 12 points, hence representing the circle (2*pi) with 12 points
    # Sun has a specific ratio compared to the length of the flag
    sun_size = width / 6  # standard ratio
    step_size = (2 * np.pi) / 12
    phase_shift = step_size / 2  # larger circle data points are slightly offset to the smaller circle
    sun_circle_ratio = sun_size * 2/3
    circle_center_width = 1 / 4 * width
    circle_center_height = np.sqrt(2) / 4 * width

    smaller_circle_angles = np.arange(0, 2 * np.pi, step_size) + phase_shift
    larger_circle_angles = smaller_circle_angles + phase_shift

    smaller_circle_x = sun_circle_ratio * np.sin(smaller_circle_angles) + circle_center_width
    smaller_circle_y = sun_circle_ratio * np.cos(smaller_circle_angles) + circle_center_height

    larger_circle_x = sun_size * np.sin(larger_circle_angles) + circle_center_width
    larger_circle_y = sun_size * np.cos(larger_circle_angles) + circle_center_height

    if fill_color:
      color = "white"
    else:
      color = "red"


    for i in range(len(smaller_circle_angles)):
        plt.plot([smaller_circle_x[i], larger_circle_x[i]], [smaller_circle_y[i], larger_circle_y[i]], color, linewidth = line_width)
        plt.plot([smaller_circle_x[(i+1) % len(smaller_circle_angles)], larger_circle_x[i]], 
                 [smaller_circle_y[(i+1) % len(smaller_circle_angles)], larger_circle_y[i]], color, linewidth = line_width)
