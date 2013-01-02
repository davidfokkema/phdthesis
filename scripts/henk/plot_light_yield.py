import numpy as np
import scipy.optimize

import artist


graph = artist.GraphArtist()
n, sim, data = np.genfromtxt('s98.csv', usecols=(0, 3, 4)).T

f = lambda x, a, b: a * x + b
popt, pcov = scipy.optimize.curve_fit(f, sim, data)

graph.plot(sim, data, linestyle=None)
x = np.linspace(0, 700)
graph.plot(x, f(x, *popt), mark=None)

locations = ['below right'] * len(n)
for i in [7, 15, 12, 2, 4, 3, 1, 0, 13]:
    locations[i] = 'above left'
locations[8] = 'above'
locations[9] = 'below'
locations[16] = 'right'
locations[5] = 'below'
locations = iter(locations)

for i, (i_n, i_sim, i_data) in enumerate(zip(n, sim, data)):
    graph.add_pin_at_xy(i_sim, i_data, '%d' % i_n,
                        location=locations.next(),
                        style='lightgray,pin edge=lightgray')

graph.set_xlabel("Simulation")
graph.set_ylabel("Experiment")
graph.set_xlimits(0, 700)
graph.set_ylimits(max=340)
graph.save('exp-transmission')
