import numpy as np

import artist


def plot_abundances():
    solar_abundances = np.loadtxt('solar_abundances.txt')
    Z_solar, N_solar = solar_abundances[:, 0], solar_abundances[:, 1]
    # Abundances per 1e3 Si atoms
    N_solar /= 1e3

    pin_options = dict(location='above', use_arrow=True,
                       style='pin distance=3.5ex')

    gcr_abundances = np.loadtxt('gcr_abundances.txt')
    Z_gcr, N_gcr = gcr_abundances[:, 0], gcr_abundances[:, 1]

    graph = artist.GraphArtist('semilogy', width=r'\linewidth')
    graph.plot(Z_solar, N_solar)
    graph.add_pin('O', x=8, **pin_options)
    graph.add_pin('Si', x=14, **pin_options)
    graph.add_pin('Fe', x=26, **pin_options)

    graph.plot(Z_gcr, N_gcr, mark='*')
    graph.add_pin('Li', x=3, **pin_options)
    graph.add_pin('Be', x=4, **pin_options)
    graph.add_pin('B', x=5, **pin_options)
    graph.add_pin('C', x=6, **pin_options)
    graph.add_pin('Sc', x=21, **pin_options)
    graph.add_pin('Ti', x=22, **pin_options)
    graph.add_pin('V', x=23, **pin_options)
    graph.add_pin('Cr', x=24, location='above', use_arrow=True,
                  style='pin distance=4.5ex')
    graph.add_pin('Mn', x=25, **pin_options)

    graph.set_xlabel("Nuclear Charge (Z)")
    graph.set_ylabel(r"Relative Abundance (Si = \num{e3})")
    graph.set_logyticks(range(-6, 10, 2))
    graph.save('abundances')
    graph.save_as_document('preview')
    graph.save_as_pdf('preview')


if __name__ == '__main__':
    plot_abundances()
