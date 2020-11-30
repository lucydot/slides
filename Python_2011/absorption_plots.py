
import numpy
import pandas
import matplotlib.pyplot

data = pandas.read_csv("./data/UVVis-01-cleaned.csv")

ave_absorption = data.mean(axis=0)
ave_plot = matplotlib.pyplot.plot(min_absorption)
matplotlib.pyplot.xlabel("wavelength")
matplotlib.pyplot.ylabel("min. absorption")
matplotlib.pyplot.savefig("./min_absorption_plot.png")


