import numpy as np

from artist import MultiPlot, smooth


def plot_ldfs():
    graph = MultiPlot(1, 2, 'loglog', width=r'.45\linewidth',
                      height=r'.6\linewidth')

    graph.set_title(0, 0, "Electrons")
    graph.set_title(0, 1, r"$E$ = \SI{e16}{\electronvolt}")

    for E in range(14, 19):
        e = np.genfromtxt('data/showere%d.t2205' % E)
        x, y = smooth(e[:, 1], e[:, 2], degree=3, logx=True, logy=True)
        graph.plot(0, 0, x, y, mark=None)
        graph.add_pin(0, 0, E)

        if E == 16:
            mu = np.genfromtxt('data/showere%d.t2207' % E)
            x, y = smooth(e[:, 1], e[:, 2], degree=3, logx=True, logy=True)
            graph.plot(0, 1, x, y, mark=None)
            graph.add_pin(0, 1, 'e')
            x, y = smooth(mu[:, 1], mu[:, 2], degree=3, logx=True, logy=True)
            graph.plot(0, 1, x, y, mark=None)
            graph.add_pin(0, 1, '$\mu$')

    graph.set_xlabel("Core distance [\si{\meter}]")
    graph.set_ylabel("Particle density [\si{\per\square\meter}]")

    graph.draw_horizontal_line(0, 0, 1.39, linestyle='gray')
    graph.draw_horizontal_line(0, 0, 2.46, linestyle='gray')
    graph.draw_horizontal_line(0, 1, 1.39, linestyle='gray')
    graph.draw_horizontal_line(0, 1, 2.46, linestyle='gray')

    graph.set_xlimits(6, 2500)
    graph.set_ylimits(1e-6, 1e5)
    graph.set_logyticks(range(-6, 6, 2))

    graph.show_yticklabels(0, 0)
    graph.show_xticklabels_for_all([(0, 0), (0, 1)])

    graph.save("ldf-threshold")
    graph.save_as_pdf("ldf-threshold")


if __name__ == '__main__':
    plot_ldfs()
