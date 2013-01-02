import numpy as np

import artist


def plot_atmospheric_abundances():
    graph = artist.GraphArtist('semilogy', width=r'.67\linewidth',
                               height=r'\linewidth')

    X, I = get_smoothed_data_from_file('proton.csv')
    X = list(X) + [1013]
    I = list(I) + [0.000045]
    graph.plot(X, I, mark=None, linestyle='smooth')
    graph.add_pin('p', location='right')

    X, I = get_smoothed_data_from_file('electron.csv')
    X = list(X) + [1013]
    I = list(I) + [0.00225]
    graph.plot(X, I, mark=None, linestyle='smooth')
    graph.add_pin('e', location='right')

    X, I = get_smoothed_data_from_file('muon.csv')
    X = list(X) + [1013]
    I = list(I) + [0.0082]
    graph.plot(X, I, mark=None, linestyle='smooth')
    graph.add_pin(r'$\mu$', location='right')

    graph.draw_vertical_line(1013, linestyle='gray')
    graph.add_pin_at_xy(1013, 2e-1, 'sea level', location='left')
    graph.set_xlabel(r"Atmospheric depth [\si{\gram\per\centi\meter\squared}]")
    graph.set_ylabel(r"Vertical intensity "
        "[\si{\per\centi\meter\squared\per\second\per\steradian}]")
    graph.set_xlimits(min=0)
    graph.set_ylimits(1e-5, 1)

    graph.save('atmospheric_abundances')
    graph.save_as_pdf('preview')


def get_smoothed_data_from_file(filename):
    data = np.genfromtxt(filename, delimiter=',', names=['X', 'I'])
    data.sort(order='X')
    X, I = artist.smooth(data['X'], data['I'], degree=2, logy=True)
    return X, I


if __name__ == '__main__':
    plot_atmospheric_abundances()
