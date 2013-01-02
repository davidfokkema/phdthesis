import numpy as np
import scipy.stats

import artist


AREA_PER_DATAPOINT = 4 # cm^2


def plot_efficiency_vs_x(x, y, N):
    eff = N / 36114.

    bins = np.linspace(min(x), max(x), 21)
    low_edges = bins[:-1]
    high_edges = bins[1:]

    #figure()
    #plot(x, 100 * eff, '.')

    e25, e50, e75 = [], [], []
    for low, high in zip(low_edges, high_edges):
        eff_sel = eff.compress((low <= x) & (x < high))
        e25.append(scipy.stats.scoreatpercentile(eff_sel, 25))
        e50.append(scipy.stats.scoreatpercentile(eff_sel, 50))
        e75.append(scipy.stats.scoreatpercentile(eff_sel, 75))
    e25 = np.array(e25)
    e50 = np.array(e50)
    e75 = np.array(e75)

    graph = artist.GraphArtist()
    x = -(low_edges + high_edges) / 2
    graph.shade_region(x, 100 * e25, 100 * e75)
    graph.plot(x, 100 * e50, linestyle=None)
    graph.set_xlimits(0, 100)
    graph.set_xlabel(r"Distance to fishtail [\si{\centi\meter}]")
    graph.set_ylabel(r"Efficiency [\si{\percent}]")
    graph.save('detector-efficiency_vs_x')


def plot_area_vs_efficiency(x, y, N):
    eff = N / 36114.

    bins = np.linspace(0, 1, 1001)
    low_edges = bins[:-1]
    high_edges = bins[1:]

    area = []
    for low, high in zip(low_edges, high_edges):
        eff_sel = eff.compress((low <= eff) & (eff < high))
        area.append(len(eff_sel) * AREA_PER_DATAPOINT)

    #figure()
    #x = (low_edges + high_edges) / 2
    #plot(x, area)

    graph = artist.GraphArtist()
    graph.histogram(area, 100 * bins)
    graph.set_xlimits(0, 5)
    graph.set_ylimits(min=0)
    graph.set_xlabel(r"Efficiency [\si{\percent}]")
    graph.set_ylabel(r"Area [\si{\centi\meter\squared}]")
    graph.save('detector-area_vs_efficiency')


def plot_histogram2d(x, y, N):
    print "Maximum number of photons:", N.max()
    print "Maximum efficiency:", (N / 36114.).max()

    x_edges = np.arange(-100, 0 + 1, 2)
    y_edges = np.arange(-25, 25 + 1, 2)
    H = np.zeros(shape=(len(x_edges) - 1, len(y_edges) - 1))
    for ix, jy, n in zip(x, y, N):
        i = x_edges.searchsorted(ix) - 1
        j = y_edges.searchsorted(jy) - 1
        H[i][j] = n

    graph = artist.GraphArtist()
    graph.histogram2d(H, x_edges, y_edges)
    graph.set_xlimits(-100, 0)
    graph.set_ylimits(-25, 25)
    graph.save_as_document('raw-light-yield')
    graph.save_as_pdf('raw-light-yield')


if __name__ == '__main__':
    data = np.genfromtxt('data/hisparc-fish.dat')
    x, y, eff, N = data.T

    plot_efficiency_vs_x(x, y, N)
    plot_area_vs_efficiency(x, y, N)
    plot_histogram2d(x, y, N)
