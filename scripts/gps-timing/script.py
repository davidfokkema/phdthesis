import datetime
import tables
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats.distributions import norm

from hisparc import publicdb
from hisparc.analysis import coincidences as search_coincidences

from artist import GraphArtist


def download_data(data):
    for station in 501, 502:
        publicdb.download_data(data, '/s%d' % station, station,
                               datetime.datetime(2011, 10, 23, 13),
                               datetime.datetime(2011, 10, 24, 13))

def main(data):
    coincidences, timestamps = search_coincidences.search_coincidences(data, ['/s501', '/s502'])

    histogram_time_differences(coincidences, timestamps)

def histogram_time_differences(coincidences, timestamps):
    dt = []
    for coinc in coincidences:
        a, b = timestamps[coinc[0]], timestamps[coinc[1]]
        if a[1] > b[1]:
            print swap
            a, b = b, a
        t501 = int(a[0])
        t502 = int(b[0])
        dt.append(t502 - t501 - 435)

    dt = np.array(dt)
    n, bins = np.histogram(dt, bins=np.arange(-50.5, 50.5))
    x = (bins[:-1] + bins[1:]) / 2
    y = n

    f = lambda x, a, b, c: a * norm.pdf(x, b, c)
    popt, pcov = curve_fit(f, x, y)
    x = np.linspace(-50, 50, 1000)

    print "loc: %.2f, width: %.2f" % (popt[1], popt[2])
    print np.std(dt)

    graph = GraphArtist()
    graph.histogram(n, bins)
    graph.plot(x, f(x, *popt), mark=None, linestyle='gray')
    graph.set_xlimits(5, 30)
    graph.set_ylimits(min=0)
    graph.set_xlabel(r"Time difference [\si{\nano\second}]")
    graph.set_ylabel("Count")
    graph.save('gps-time-distr')
        

if __name__ == '__main__':
    try:
        data
    except NameError:
        try:
            data = tables.openFile('data.h5', 'r')
        except IOError:
            data = tables.openFile('data.h5', 'w')
            download_data(data)

    main(data)
