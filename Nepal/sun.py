import numpy as np
import matplotlib.pyplot as plt

def make_sun(width_of_flag):

  """This function creates the Sun of the lower triangle of the Nepali flag.
  All the dimensions are according to the constitution of Nepal.
  Parameters: width of the flag
  Output: figure of the Sun for the flag. """
  # creates two circles one bigger and one smaller
  # In Nepali flag, the sun has 12 points, hence representing the circle (2*pi) with 12 points
  # Sun has specific ratio compared to the length of the flag
  sun_size = width_of_flag/2 # standard ratio
  step_size = (2*np.pi)/12
  phase_shift = step_size/2 # larger circle data points are slightly offset to the smaller circle
  sun_circle_ratio = sun_size * 1.5
  smaller_circle_angles = np.arange(0, 2*np.pi, step_size) + phase_shift
  larger_circle_angles  = smaller_circle_angles + phase_shift

  smaller_circle_x = sun_size * np.sin(smaller_circle_angles)
  smaller_circle_y = sun_size * np.cos(smaller_circle_angles)

  larger_circle_x = sun_circle_ratio * np.sin(larger_circle_angles)
  larger_circle_y = sun_circle_ratio * np.cos(larger_circle_angles)

  plt.figure(figsize=(sun_size, sun_size))
  plt.grid("on")
  for i in range(len(smaller_circle_angles)):
    plt.plot([smaller_circle_x[i], larger_circle_x[i]], [smaller_circle_y[i], larger_circle_y[i]], 'k-')
    if i == len(x)-1:
          plt.plot([smaller_circle_x[0], larger_circle_x[i]], [smaller_circle_y[0], larger_circle_y[i]], 'k-')
          break
    plt.plot([smaller_circle_x[i+1], larger_circle_x[i]], [smaller_circle_y[i+1], larger_circle_y[i]], 'k-')
    plt.savefig("sun.png")
