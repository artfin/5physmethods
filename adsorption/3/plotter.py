# -*- coding: utf-8 -*-8

import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy as sp
import numpy as np
import matplotlib.patches as mpatches

mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.unicode'] = True

mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = 'Times'

mpl.rcParams['figure.titlesize'] = 'xx-large'
mpl.rcParams['legend.fontsize'] = 'large'
mpl.rcParams['axes.labelsize'] = 'x-large'
mpl.rcParams['axes.titlesize'] = 'large'

mpl.rcParams['xtick.labelsize'] = 'large'
mpl.rcParams['ytick.labelsize'] = 'large'

omega = 21.5 # Angstrem**2

a = [32.675, 57.384, 61.763, 68.738, 71.235] 
pps = [0.0189, 0.1211, 0.1543, 0.2204, 0.2454]

lin = [x / (1 - x) / y * 1000 for x, y in zip(pps, a)]

x = np.linspace( 0.0, 0.3, 100 )

fp, residuals, rank, sv, rcond = sp.polyfit( pps, lin, 1, full = True )
f = sp.poly1d( fp )

am = 1 / (fp[0] + fp[1])
print("am: {0}".format( am ))

AVOGADRO = 6.022e23
s = am * AVOGADRO * omega * 1e-20 * 1e-3
print("surface area: {0}".format(s))

#print("Parameters: %s" % fp )
#print("f: %s" % f )

#plt.scatter( pps, lin, color = 'k', s = 40, marker = 'd' ) 
#plt.plot( x, f( x ), color = 'r' )

#plt.xlim((-0.02, 0.32 )) 
#plt.ylim(( 0.0, 0.006 ))

#plt.xlabel(r'$p / p_s$')
#plt.ylabel(r'$\frac{ p / p_s }{ a ( 1 - p / p_s) }$')

plt.grid( linestyle = ':', alpha = 0.7 )

plt.xlabel(r'$p / p_s$')
plt.ylabel(r'a, mcmol / g')

plt.scatter( pps, a, color = 'k', s = 40, marker = 'd' )
plt.scatter( 0.115, am * 1000, s = 40, marker = 'x', color = 'r')   
plt.show()

