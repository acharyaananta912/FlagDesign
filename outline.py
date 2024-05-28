import matplotlib.pyplot as plt
from flagparameters import calculate_flag_parameters

def clean_outline(width,color="red", fill=True):

	params = calculate_flag_parameters(width)

	plot_x = [params["B"][0], params["A"][0], params["C"][0], params["G"][0], params["E"][0], params["B"][0]]
	plot_y = [params["B"][1], params["A"][1], params["C"][1], params["G"][1], params["E"][1], params["B"][1]]

	fig, ax = plt.subplots()

	plt.plot(plot_x, plot_y, color=color)
	if fill == True:
		plt.fill(plot_x, plot_y, color=color)
	
	plt.gca().set_aspect('equal', adjustable='box')
	plt.axis("off")

	return fig

def sketch_outline(width,color="k"):

	params = calculate_flag_parameters(width)

	fig = clean_outline(width,color="k",fill=False)
	plt.plot([params["B"][0],params["D"][0]],[params["B"][1],params["D"][1]],color=color,linestyle=":")
	plt.plot([params["F"][0],params["G"][0]],[params["F"][1],params["G"][1]],color=color,linestyle=":")

	plt.gca().set_aspect('equal', adjustable='box')
	plt.axis("off")

	return fig
