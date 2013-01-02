import numpy as np

import artist


def plot_transport_time():
    counts = np.genfromtxt('data/time15.dat', skip_header=1)
    bins = np.linspace(1, 8, 71)

    approx_x = [2.5507,   2.5507,   3.4953,   3.4953,   6.4630, 6.4630]
    approx_y = [0,      380.96,   380.96,   186.68,   186.68,   0]
    
    graph = artist.GraphArtist()
    graph.histogram(counts, bins, linestyle='gray')
    graph.plot(approx_x, approx_y, mark=None, linestyle='black')
    graph.set_xlabel(r"Transport time [\si{\nano\second}]")
    graph.set_ylabel("Counts")
    graph.set_xlimits(1, 8)
    graph.set_ylimits(min=0)
    graph.save('transport_time')


if __name__ == '__main__':
    plot_transport_time()
