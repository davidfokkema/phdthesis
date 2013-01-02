from matplotlib.pyplot import figure, show
from matplotlib.patches import Ellipse
from matplotlib.patches import Circle
import numpy as np

#----read csv table ------------------------
import string
import csv

'''
    read table from csv file standard excel export. In Dutch format the decimal separator is a comma.
    The value separator is then a semi colon. Soemtimes called semicolon separated value- files (SSV format)
    I cannot find a proper option in the reader method.
'''
qq=[]
pf = list(csv.reader(open('../LOI/s98.csv', "r"), delimiter=';',dialect='excel'))

print  pf[0]   #header strings
print pf[1]
for i in range(1,len(pf)):   #skip first row, header
    qq.append([float(string.replace(x,',','.')) for x in pf[i]]) # if x.isdigit()]

#sys.exit('ho even')
#----plot-------------------
fig = figure()

ax = fig.add_subplot(111, aspect='equal')

def plotsmile(x,y, xerr, yerr, str):
    '''  
        Function to plot datapoins in circles
        Errorbars optional
    '''
    cir = Circle((x,y), 15, facecolor='green', alpha=0.5)
    ax.add_artist(cir)
    ax.annotate(str,
                xy = (x, y),      # datacoord=textcoord
                xycoords = 'data',
#                arrowprops=dict(facecolor='black', shrink=0.05),
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=12,
                clip_on=True, # clip to the axes bounding box
     )
    if (xerr > 0) or (yerr > 0):
        ax.errorbar(x, y, xerr=xerr, yerr=yerr)
        
ax.set_xlim(0, 700)
ax.set_ylim(0, 350)
ax.set_xlabel('simulation')
ax.set_ylabel('data')

    
for i in range(len(qq)): 
    plotsmile (zip(*qq)[3][i],zip(*qq)[4][i], 0, 0, str(int(zip(*qq)[0][i])))

linfit = polyfit(zip(*qq)[3],zip(*qq)[4],1)    
text(30, 30, 'a= ' + str(linfit[0]) + '      b= '+str(linfit[1]))


if False: #----ook nog 3d:------
    from mpl_toolkits.mplot3d.axes3d import Axes3D
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib import cm
    from mpl_toolkits.mplot3d.axes3d import get_test_data

    # Twice as wide as it is tall.
    #fig = plt.figure(figsize=plt.figaspect(0.5))

#---- First subplot
    ab = fig.add_subplot(1, 2, 2, projection='3d')
    X = zip(*qq)[1]
    Y = zip(*qq)[2]
    #X, Y = np.meshgrid(X, Y)
    #R = np.sqrt(X**2 + Y**2)
    #Z = np.sin(R)
    Z = zip(*qq)[3]
    ab.scatter3D(X, Y, Z, 'r', marker='o')
    ab.set_xlim3d(-25,25)
    ab.set_ylim3d(-100,0)
    ab.set_zlim3d(0,700)


show()

