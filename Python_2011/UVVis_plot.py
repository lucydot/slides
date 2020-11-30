import numpy
import pandas
import matplotlib.pyplot

data = pandas.read_csv("./data/UVVis-01-cleaned.csv")

ave_absorption = data.mean(axis=0)
max_absorption = data.max(axis=0)
min_absorption = data.min(axis=0)


fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.set_xlabel('wavelength')
axes1.plot(ave_absorption)

axes2.set_ylabel('max')
axes2.set_xlabel('wavelength')
axes2.plot(max_absorption)

axes3.set_ylabel('min')
axes3.set_xlabel('wavelength')
axes3.plot(min_absorption)

fig.tight_layout()

matplotlib.pyplot.savefig('./group_plot.png')

matplotlib.pyplot.show()