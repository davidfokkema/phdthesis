import numpy as np

from artist import GraphArtist, smooth


def plot_ldfs():
    plot_lateral_df()
    plot_longitudinal_df()

def plot_lateral_df():
    gamma = np.genfromtxt('data/showere15-proton.t2001', usecols=(1, 2))
    e = np.genfromtxt('data/showere15-proton.t2205', usecols=(1, 2))
    mu = np.genfromtxt('data/showere15-proton.t2207', usecols=(1, 2))

    graph = GraphArtist(axis='loglog', width=r'.5\linewidth')
    x, y = smooth(gamma[:, 0], gamma[:, 1], degree=3, logx=True, logy=True)
    graph.plot(x, y, mark=None, linestyle='smooth')
    graph.add_pin(r'$\gamma$')
    x, y = smooth(e[:, 0], e[:, 1], degree=3, logx=True, logy=True)
    graph.plot(x, y, mark=None, linestyle='smooth')
    graph.add_pin('e')
    x, y = smooth(mu[:, 0], mu[:, 1], degree=3, logx=True, logy=True)
    graph.plot(x, y, mark=None, linestyle='smooth')
    graph.add_pin(r'$\mu$')

    graph.set_xlabel(r"Core distance [\si{\meter}]")
    graph.set_ylabel(r"Particle density [\si{\per\square\meter}]")
    graph.set_logyticks(range(-6, 3, 2))
    graph.save('ch1-lateral')
    graph.save_as_pdf('ch1-lateral')

def plot_longitudinal_df():
    gamma = np.genfromtxt('data/showere15-proton.t1001', usecols=(1, 2))
    e = np.genfromtxt('data/showere15-proton.t1205', usecols=(1, 2))
    mu = np.genfromtxt('data/showere15-proton.t1207', usecols=(1, 2))

    graph = GraphArtist(axis='semilogy', width=r'.5\linewidth')
    graph.plot(gamma[:, 0], gamma[:, 1], mark=None, linestyle='smooth')
    graph.add_pin(r'$\gamma$', location='right')
    graph.plot(e[:, 0], e[:, 1], mark=None, linestyle='smooth')
    graph.add_pin('e', location='right')
    graph.plot(mu[:, 0], mu[:, 1], mark=None, linestyle='smooth')
    graph.add_pin(r'$\mu$', location='right')

    graph.set_xlabel("Atmospheric depth [\si{\gram\per\centi\meter\squared}]")
    graph.set_ylabel("Number of particles")
    graph.save('ch1-longitudinal')
    graph.save_as_pdf('ch1-longitudinal')


if __name__ == '__main__':
    plot_ldfs()
