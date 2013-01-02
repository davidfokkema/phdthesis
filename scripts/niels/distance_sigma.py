import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from scipy.optimize import curve_fit
from pylab import *

import artist


def xuniqueCombinations(items, n):
    """Return unique combinations from a list

    Reference: http://code.activestate.com/recipes/190465/

    """
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc

def output_plot(afstand,sigma_dt,error_dt,combi):
    #fig = plt.figure()
    fig = gcf()

    gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
    #ax1 = fig.add_axes(ax)
    ax1 = fig.add_subplot(gs[0])
    ax1.plot(afstand,sigma_dt,'o',c='b')
    #ax1.errorbar(afstand,sigma_dt,yerr=error_dt,fmt='b+')
    ax1.grid(True)
    ax1.set_xlim(0,500)
    ax1.set_ylim(0,500)
    #labels
    ax1.set_xlabel('afstand [m]')
    ax1.set_ylabel('$\sigma$ dt [ns]')
    #textlabels
    #for i,station in enumerate(xuniqueCombinations(stations,2)):
    #    s_text = str(station[0])+'-'+str(station[1])
    #    x_text = int(afstand[i])-40
    #    y_text = int(sigma_dt[i])+1
    #    ax1.text(x_text,y_text,str(s_text),fontsize=8)
    #for i,tkst in enumerate(combi):
    #    x_text = int(afstand[i])-20
    #    y_text = int(sigma_dt[i])+1
    #    ax1.text(x_text,y_text,tkst,fontsize=8)
        
    #fit
    func = lambda x,a,b: a*x+b
    popt, pcov = curve_fit(func, np.array(afstand), np.array(sigma_dt))
    print "a = ",popt[0]
    print "b = ",popt[1]
    x_fit = np.array(range(50,450))
    ax1.plot(x_fit, func(x_fit,*popt), 'r--', linewidth=1)
        
    #plot variances
    ax2 = fig.add_subplot(gs[1])
    ax2.set_xlabel('afstand [m]')
    ax2.set_ylabel('verschil fit [ns]')
    ax2.grid(True)
    ax2.set_xlim(0,500)
    ax2.set_ylim(-10,10)
    
    #textlabels
    for i,x in enumerate(afstand):
        #ax2
        fit_y = func(x,*popt)
        d_fit_y = sigma_dt[i]-fit_y
        print afstand[i],sigma_dt[i],fit_y,d_fit_y
        ax2.plot(x,d_fit_y,'o',c='b')
        x_text = int(afstand[i])-15
        if d_fit_y<0:
            int_y = 2
        else:
            int_y = -4
        y_text = int(d_fit_y)+int_y
        ax2.text(x_text,y_text,combi[i],fontsize=8)
        
        #ax1
        if d_fit_y<0:
            int_x = 10
        else:
            int_x = -45
        x_text = int(afstand[i])+int_x
        y_text = int(sigma_dt[i])-9
        ax1.text(x_text,y_text,combi[i],fontsize=8)
        
        
    fig.savefig('temp.eps')
    fig.show()
    
    graph = artist.GraphArtist()
    graph.plot(afstand, sigma_dt, linestyle=None)
    graph.plot(x_fit, func(x_fit,*popt), mark=None)

    locations = ['below right'] * len(combi)
    locations[1] = 'above left'
    locations[2] = 'above left'
    locations[3] = 'above left'
    locations[9] = 'above left'
    locations = iter(locations)

    for idx, (x, y, text) in enumerate(zip(afstand, sigma_dt, combi)):
        graph.add_pin_at_xy(x, y, '$%s$' % text,
                            location=locations.next(),
                            style='pin distance=1.5ex')

    graph.set_xlabel(r'Distance [\si{\meter}]')
    graph.set_ylabel(r'$\sigma_{\Delta t} [\si{\nano\second}]$')
    graph.set_xlimits(0, 500)
    graph.set_ylimits(0, 500)
    graph.save('sigma-time-vs-distance')
    graph.save_as_pdf('preview')


if __name__ == '__main__':
    stations = [501,502,503,504,505]
    #sigma_dt = [126, 165, 303, 282, 259, 392, 285, 181, 371, 453]
    
    #experimental values
    #sigma_dt = [110,150,284,271,245,363,273,164,356,415]
    #error_dt = [7,1,33,5,39,88,5,3,7,1]
    #afstand = [99.055, 128.918, 262.198, 238.742, 221.901, 359.731, 247.498, 141.597, 327.994, 406.894]
    
    #simulated values
    sigma_dt = [99,126,252,233,219,354,241,136,318,393]
    error_dt = [7,1,33,5,39,88,5,3,7,1]
    afstand = [99.055, 128.918, 262.198, 238.742, 221.901, 359.731, 247.498, 141.597, 327.994, 406.894]
    
    
    combi = ['501-502','501-503','501-504','501-505','502-503','502-504','502-505','503-504','503-505','504-505']

    output_plot(afstand,sigma_dt,error_dt,combi)
    
