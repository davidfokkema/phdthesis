import numpy as np

from artist import GraphArtist


def main():
    leap = np.genfromtxt('leap-prot.dat', delimiter=',', usecols=(0, 1))
    leap_energy = leap[:, 0] * 1e6
    leap_flux = leap[:, 1] * 1e3 * 2

    akeno_new_lo = np.genfromtxt('akeno-new-lo', usecols=(0, 1),
                                 names=['E', 'F'])
    akeno_new_lo.sort()
    akeno_new_lo['F'] /= (akeno_new_lo['E'] / 1e9) ** 2.75
    
    flys_eye = np.genfromtxt('fe-new', usecols=(0, 1))
    flys_eye_energy = flys_eye[:, 0]
    flys_eye_flux = (flys_eye[:, 1] / (flys_eye_energy / 1e9) ** 2.75)

    yakutsk = np.genfromtxt('yakustk', usecols=(1, 0))
    yakutsk_energy = yakutsk[:, 0]
    yakutsk_flux = (yakutsk[:, 1] / (yakutsk_energy / 1e9) ** 2.75)

    proton = np.genfromtxt('proton', usecols=(1, 0))
    proton_energy = proton[:, 0]
    proton_flux = (proton[:, 1] / (proton_energy / 1e9) ** 2.75)

    haverah = np.genfromtxt('haverah', usecols=(1, 0))
    haverah.sort(axis=0)
    haverah_energy = haverah[:, 0]
    haverah_flux = (haverah[:, 1] / (haverah_energy / 1e9) ** 2.75)

    clf()
    #loglog(leap_energy, leap_flux)
    loglog(akeno_energy, akeno_flux)
    loglog(akeno_new_lo['E'], akeno_new_lo['F'])
    #loglog(flys_eye_energy, flys_eye_flux)
    #loglog(yakutsk_energy, yakutsk_flux)
    #loglog(proton_energy, proton_flux)
    #loglog(haverah_energy, haverah_flux)

    #x = logspace(11, 20)
    #plot(x, x ** -2.75 / 1e-29)


if __name__ == '__main__':
    main()
