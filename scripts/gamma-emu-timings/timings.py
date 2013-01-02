import tables
import numpy as np

import artist


LOW = 123
HIGH = 246


if __name__ == '__main__':
    try:
        data
    except NameError:
        data = tables.openFile('jamboree-timing.h5')

    d = data.root.timings.read()

    bins = np.arange(-51.25, 52.5, 2.5)

    gammas_dist = d.compress((d[:,1] < LOW) & (d[:,2] < LOW) &
                             (abs(d[:,0]) < 100), axis=0)[:,0]
    gammas, bins = np.histogram(gammas_dist, bins)

    emus_dist = d.compress((d[:,1] > HIGH) & (d[:,2] > HIGH) &
                           (abs(d[:,0]) < 100), axis=0)[:,0]
    emus, bins   = np.histogram(emus_dist, bins)

    gamma_emu, bins = np.histogram(d.compress((d[:,1] < LOW) & (d[:,2] > HIGH),
                                   axis=0)[:,0], bins)
    emu_gamma, bins = np.histogram(d.compress((d[:,1] > HIGH) & (d[:,2] < LOW),
                                   axis=0)[:,0], bins)

    print "gammas: < %f mV, mu = %f, sigma = %f" % (LOW * .57,
                                                    np.mean(gammas_dist),
                                                    np.std(gammas_dist))
    print "e/mu's: > %f mV, mu = %f, sigma = %f" % (HIGH * .57,
                                                    np.mean(emus_dist),
                                                    np.std(emus_dist))

    graph = artist.MultiPlot(2, 2, width=r'.45\linewidth')
    graph.histogram(0, 0, gammas, bins)
    graph.histogram(0, 1, emu_gamma, bins)
    graph.histogram(1, 0, gamma_emu, bins)
    graph.histogram(1, 1, emus, bins)
    graph.set_label(0, 0, r'$\gamma - \gamma$')
    graph.set_label(0, 1, r'$\mathrm{e}/\mu - \gamma$')
    graph.set_label(1, 0, r'$\gamma - \mathrm{e}/\mu$')
    graph.set_label(1, 1, r'$\mathrm{e}/\mu - \mathrm{e}/\mu$')

    graph.set_xlabel(r"$t_1 - t_2$ [\si{\nano\second}]")
    graph.show_xticklabels_for_all([(1, 0), (0, 1)])
    graph.set_ylimits_for_all(None, min=0)
    graph.set_yticks_for_all(None, None)

    graph.save('gamma-emu-time-differences')
