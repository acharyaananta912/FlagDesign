import matplotlib.pyplot as plt
from outline import clean_outline
from outline import sketch_outline
from sun import sun_clean
from sun import sun_sketch

global width
width = 10

fig1 = sun_clean(width)
plt.savefig("flagoutline.pdf")

fig2 = sun_sketch(width)
plt.savefig("flagoutline_sketch.pdf")

