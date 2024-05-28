import numpy as np
import matplotlib.pyplot as plt
from flagparameters import calculate_flag_parameters
from outline import clean_outline
from outline import sketch_outline

def sun_coordinates(width,sketch=False):

	params = calculate_flag_parameters(width)
	sun_size = params["AB"] / 6
	step_size = (2 * np.pi) / 12
	phase_shift = step_size / 2  # larger circle data points are slightly offset to the smaller circle
	sun_circle_ratio = sun_size * 2/3
	circle_center_width = 1 / 4 * params["AB"]
	circle_center_height = np.sqrt(2) / 4 * params["AB"]

	if sketch == True:
		smaller_circle_angles = np.arange(0, 2 * np.pi, 0.01) + phase_shift

	elif sketch == False:
		smaller_circle_angles = np.arange(0, 2 * np.pi, step_size) + phase_shift

	larger_circle_angles = smaller_circle_angles + phase_shift

	smaller_circle_x = sun_circle_ratio * np.sin(smaller_circle_angles) + circle_center_width
	smaller_circle_y = sun_circle_ratio * np.cos(smaller_circle_angles) + circle_center_height

	larger_circle_x = sun_size * np.sin(larger_circle_angles) + circle_center_width
	larger_circle_y = sun_size * np.cos(larger_circle_angles) + circle_center_height

	return smaller_circle_x, smaller_circle_y, larger_circle_x, larger_circle_y


def sun_clean(width,sketch=False):

	sx, sy, lx, ly =  sun_coordinates(width, sketch=False)

	plt_x = np.array([])
	plt_y = np.array([])
	for i in range(len(sx)):
		  plt_x = np.append(sx[i],plt_x)
		  plt_x = np.append(lx[i],plt_x)
		  plt_y = np.append(sy[i],plt_y)
		  plt_y = np.append(ly[i],plt_y)
	plt_x = np.append(sx[0],plt_x)
	plt_y = np.append(sy[0],plt_y)

	if sketch == False:
		fig = clean_outline(width, color="red",fill=True)
		plt.plot(plt_x, plt_y, color="white", linewidth = 0.1)
		plt.fill(plt_x, plt_y, color="white", linewidth = 0.1)
		return fig

	elif sketch == True:
		plt.plot(plt_x, plt_y, color="k")


def  sun_sketch(width):

	sx, sy, lx, ly =  sun_coordinates(width, sketch=True)

	fig = sketch_outline(width,color="k")
	plt.plot(sx,sy,"k", linestyle=":")
	plt.plot(lx,ly,"k", linestyle=":")
	sun_clean(width, sketch=True)

	return fig
