import datetime

import tables
from pylab import *

from hisparc import publicdb
import hisparc.analysis.traces

import artist


def download_data(data):
    publicdb.download_data(data, '/s501', 501,
                           datetime.datetime(2012, 8, 15),
                           datetime.datetime(2012, 8, 16), get_blobs=True)


def main(data):
    global sel, phs, ids, trace

    events = data.root.s501.events
    blobs = data.root.s501.blobs

    phs = events.col('pulseheights')
    ids = events.col('event_id')

    sel = ids.compress(phs[:, 0] >= 400)

    event_id = sel[0]
    traces = events[event_id - 1]['traces']
    trace = hisparc.analysis.traces.get_traces(blobs, [traces[0]])[0]

    clf()
    b = arange(len(trace)).compress(trace < 20 * -.57)[0]
    a = b - 1
    plot(arange(0, b), trace[:b], 'b')
    plot(arange(b, len(trace)), trace[b:], 'b')
    plot([a, b], [trace[a], trace[b]], 'g')

    threshold = 20 * -.57
    # y = dydx * x + c
    dydx = (trace[b] - trace[a]) / (b - a)
    c = trace[a] - dydx * a
    x = (threshold - c) / dydx
    axhline(threshold)
    axvline(x)
    axvline(b)

    print 2.5 * x

    graph = artist.MultiPlot(1, 2, width=r'.45\linewidth')

    graph.plot(0, 0, 2.5 * arange(len(trace)), trace, mark=None)
    graph.draw_horizontal_line(0, 0, threshold, linestyle='gray')

    graph.plot(0, 1, 2.5 * arange(0, b), trace[:b])
    graph.plot(0, 1, 2.5 * arange(b, len(trace)), trace[b:])
    graph.plot(0, 1, [2.5 * a, 2.5 * b], [trace[a], trace[b]],
               linestyle='dashed', mark=None)
    graph.draw_horizontal_line(0, 1, threshold, linestyle='gray')
    graph.draw_vertical_line(0, 1, 2.5 * x, linestyle='dashed')
    graph.draw_vertical_line(0, 1, 2.5 * b, linestyle='dashdotted')

    zoom = 28, 52
    graph.draw_vertical_line(0, 0, zoom[0], linestyle='dotted')
    graph.draw_vertical_line(0, 0, zoom[1], linestyle='dotted')
    graph.set_xlimits_for(0, 1, *zoom)
    graph.set_ylimits(-250, 20)

    graph.set_xlabel(r"Time [\si{\nano\second}]")
    graph.set_ylabel(r"Signal [\si{\milli\volt}]")
    graph.show_xticklabels_for_all([(0, 0), (0, 1)])
    graph.set_xticklabels_position(0, 1, 'right')
    graph.show_yticklabels(0, 0)
    graph.save('timing-methods')
    graph.save_as_pdf('preview')


if __name__ == '__main__':
    if 'data' not in globals():
        data = tables.openFile('data.h5', 'a')
    if '/s501' not in data:
        download_data(data)

    main(data)
