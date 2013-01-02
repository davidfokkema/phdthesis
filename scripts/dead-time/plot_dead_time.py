import cPickle as pickle
import gzip

from pylab import *

from artist import GraphArtist


def plot_dead_time(dt):
    clf()
    n, bins, patches = hist(dt / 1e3, bins=linspace(0, 100, 51),
                            histtype='step')

    graph = GraphArtist(width=r'.4\linewidth')
    graph.histogram(n, bins)
    graph.set_xlabel(r"Time between triggers [\si{\micro\second}]")
    graph.set_ylabel(r"Number of events")
    graph.set_xlimits(0, 100)
    graph.save("dead_time")

def plot_dead_time_long(dt):
    clf()
    n, bins, patches = hist(dt / 1e6, bins=linspace(0, 1000, 51),
                            histtype='step')

    graph = GraphArtist(width=r'.4\linewidth')
    graph.histogram(n, bins)
    graph.set_xlabel(r"Time between triggers [\si{\milli\second}]")
    graph.set_ylabel(r"Number of events")
    graph.set_xlimits(0, 1000)
    graph.save("dead_time_long")


if __name__ == '__main__':
    if 't' not in globals():
        with gzip.open('ts.dat.gz', 'r') as f:
            t = pickle.load(f)
        dt = t[1:] - t[:-1]
    if 't2' not in globals():
        with gzip.open('ts2.dat.gz', 'r') as f:
            t2 = pickle.load(f)
        dt2 = t2[1:] - t2[:-1]
    plot_dead_time(dt)
    plot_dead_time_long(dt2)
