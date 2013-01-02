from datetime import datetime

import tables
import numpy as np

from hisparc import publicdb
from artist import GraphArtist


def plot_pulseheight_spectrum(data):
    ph = data.root.s501.events[:]['pulseheights'][:,0]
    ph = ph * .57
    n, bins = np.histogram(ph, bins=np.arange(0, 600, 10 * .57))

    graph = GraphArtist('semilogy')
    graph.histogram(n, bins)
    graph.add_pin(r'\SI{1}{\mip}', location='above', x=122.5,
                  use_arrow=True)
    graph.set_xlabel(r"Pulseheight [\si{\milli\volt}]")
    graph.set_ylabel("Count")
    graph.draw_vertical_line(30, linestyle='gray')
    graph.draw_vertical_line(70, linestyle='gray')
    graph.add_pin_at_xy(30, 1e4, r'\SI{30}{\milli\volt}',
                        location='right', style='pin distance=4.5ex')
    graph.add_pin_at_xy(70, 2e4, r'\SI{70}{\milli\volt}',
                        location='right')
    graph.set_xlimits(0, 600)

    graph.save('pulseheight-spectrum-trigger-levels')


if __name__ == '__main__':
    try:
        data
    except NameError:
        try:
            data = tables.openFile('data.h5', 'r')
        except IOError:
            data = tables.openFile('data.h5', 'a')
            publicdb.download_data(data, '/s501', 501, datetime(2011, 10, 1),
                                   datetime(2011, 10, 2))

    plot_pulseheight_spectrum(data)
