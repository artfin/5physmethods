import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import scipy as sp

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


# NaBr

# m/mol kg^-1
c = [ 0.001, 0.002, 0.005, 0.010, 0.020, 0.050, 0.100, 0.200, 0.500, 1.000, 2.000, 5.000 ]
print( 'len(c): {0}'.format( len(c) ))
mean_act = [ 0.965, 0.952, 0.928, 0.903, 0.873, 0.824, 0.783, 0.742, 0.697, 0.687, 0.730, 1.083 ]
print( 'len(mean_act): {0}'.format( len(mean_act)))

eps = 78.3
temperature = 298.15

eps0 = 8.854187817 * 10**(-12) # F / m
boltzmann_constant = 1.38064852 * 10**(-23) # J / k
avogadro = 6.022140857 * 10**(23) # mol-1
electron_charge = 1.6021766208 * 10**(-19) # C

B = electron_charge * np.sqrt( 2.0 * 10**3 * avogadro / ( eps * eps0 * boltzmann_constant * temperature ))
print('B: {0} * 10**9'.format( B * 10**(-9) ))

h = electron_charge**3 / ( 2.3036 * 8 * np.pi * eps * eps0 * boltzmann_constant * temperature ) * np.sqrt( 2 * 10**3 * avogadro / ( eps * eps0 * boltzmann_constant * temperature ) )
print('h: {0}'.format( h ))

end = 11
x = B * np.sqrt( c[:end] )
y = [ -h * np.sqrt( _c ) / np.log10( _mean_act ) for _c, _mean_act in zip( c[:end], mean_act[:end] ) ]

end2 = 6 
fp, residual, rank, sv, rcond = sp.polyfit( x[:end2], y[:end2], 1, full = True )
f = sp.poly1d( fp )

print('residual: {0}'.format( residual ))
print( 'fp[0]: {0}; fp[1]: {1}'.format( fp[0], fp[1] ))
xx = np.linspace( 0, max(x), 100 )

a = fp[0]

x = np.linspace( np.sqrt( min(c) ), np.sqrt( max(c) ), 100 ) 
y1 = [ - h * _c for _c in x ]
y2 = [ - h * _c / ( 1 + a * B * _c ) for _c in x ]

sqrt_c = np.sqrt( c )

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

lw = 2.0

ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.set_xlim( (-0.3, 2.5) )
ax.set_ylim( (-0.3, 0.2) )

label = ax.set_xlabel( r'$\sqrt{C}$', ha='left', va = 'top' )
label = ax.set_ylabel( r'$\lg f_{\pm}^{(N)}$' )

#ax.xaxis.set_label_coords( 2.3, -0.01 )
#ax.yaxis.set_label_coords( -0.01, 2.4 )

patch1 = mpatches.Patch( color = 'g', label = 'I order' )
patch2 = mpatches.Patch( color = 'b', label = 'II order' )

ax.plot( x, y1, color = 'g', linewidth = lw )
ax.plot( x, y2, color = 'b', linewidth = lw )
ax.scatter( sqrt_c, np.log10( mean_act ), s = 30, marker = '^', color = 'k' )
ax.grid( linestyle = ':', alpha = 0.7 )

ax.legend( handles = [patch1, patch2] )

plt.show()

#lw = 2.0
#plt.xlim( (-0.05, 5.0 * 10**9) )
#plt.ylim( (0.8, 5.2) )
#plt.plot( xx, f(xx), linewidth = lw, color = 'k' )
#plt.scatter( x, y, marker = '^', s = 30, color = 'k' )
#plt.grid( linestyle = ':', alpha = 0.7 )
#plt.show()

