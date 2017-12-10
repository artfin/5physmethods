import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate 

mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.unicode'] = True

mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = 'Times'

mpl.rcParams['figure.titlesize'] = "xx-large"
mpl.rcParams['legend.fontsize'] = "large"
mpl.rcParams['axes.labelsize'] = "x-large"
mpl.rcParams['axes.titlesize'] = "large"

mpl.rcParams['xtick.labelsize'] = "large"
mpl.rcParams['ytick.labelsize'] = "large"

data = np.loadtxt("kolb1986_figure8.csv", delimiter=',')

x = data[:,0]
y = data[:,1]
spline = interpolate.splrep(x, y)
xnew = np.linspace(min(x), max(x), 100)
ynew = interpolate.splev(xnew, spline, der=0)

plt.title( r'\LARGE Double-layer capacity as a function of potential for Au(111)-(1x23) in 0.01M $HClO_4$' )

plt.xlabel(r'$U_{SCE}, V' )
plt.ylabel(r'C, $\mu$F $\cdot$ cm${-2}$' )

plt.plot(xnew, ynew, color = 'k', linewidth = 2.0, linestyle = 'solid')
plt.grid( linestyle = ':', alpha = 0.7 )
 
plt.show()

