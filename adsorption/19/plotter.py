import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

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


sigma = 28.88 * 10**(-7) # j / cm**2
vm = 88.74 # cm**3 / mol
UNIGASCONST = 8.314 # j / mol / k
temperature = 293 # K

# desorption curve
a = [ 6.976, 6.928, 6.842, 6.443, 5.519, 4.813, 3.585, 2.737, 1.777, 1.224, 0.769, 0.568, 0.465, 0.398, 0.299, 0.159  ] # mmol / g
pps = [ 0.974, 0.934, 0.896, 0.884, 0.873, 0.866, 0.853, 0.842, 0.827, 0.800, 0.753, 0.710, 0.639, 0.545, 0.317, 0.108 ]

d = [ -4 * sigma * vm / (UNIGASCONST * temperature * np.log( x )) * 10**8 for x in pps ] # in angstrem

vol = [ x * vm / 1000 for x in a ] # cm**3 / g

# -----------------------------------------------
# STRUCTURAL CURVE

#plt.plot( d, vol, color = 'k', linewidth = 1.5 )
#plt.scatter( d, vol, color = 'r', s = 40, marker = 'x' )

#plt.xlabel(r'd, Angstrom')
#plt.ylabel(r'v, cm$^{3}$ / g')

# -----------------------------------------------

dd = [ x - y for x, y in zip(d, d[1:]) ]
vold = [ x - y for x, y in zip(vol, vol[1:]) ]
derivative = [ x / y for x, y in zip(vold, dd) ]

d_aver = [ 0.5 * (x + y) for x, y in zip(d, d[1:]) ]

plt.plot( d_aver[1 : (len(d_aver) - 1)], derivative[1 : (len(derivative) - 1)], color = 'k', linewidth = 1.5 )
plt.scatter( d_aver[1 : (len(d_aver) - 1)], derivative[1 : (len(derivative) - 1)], color = 'r', s = 40, marker = 'x' )

plt.xlabel(r'd, Angstrom')
plt.ylabel(r'$\displaystyle \frac{\Delta V}{\Delta d}$')

m = derivative.index(max(derivative))
plt.axvline( x = d_aver[m], color = 'g', linestyle = 'dashed', linewidth = 1.2 )

print('d_aver[m]: {0}'.format(d_aver[m]))

plt.grid( linestyle = ':', alpha = 0.7 )

plt.show()

