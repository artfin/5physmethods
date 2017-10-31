import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import scipy as sp

#mpl.rcParams['text.usetex'] = True
#mpl.rcParams['text.latex.unicode'] = True

#mpl.rcParams['font.family'] = 'serif'
#mpl.rcParams['font.serif'] = 'Times'

#mpl.rcParams['figure.titlesize'] = "xx-large"
#mpl.rcParams['legend.fontsize'] = "large"
#mpl.rcParams['axes.labelsize'] = "x-large"
#mpl.rcParams['axes.titlesize'] = "large"

#mpl.rcParams['xtick.labelsize'] = "large"
#mpl.rcParams['ytick.labelsize'] = "large"


# m = [ 0.050, 0.100, 0.500, 1.000, 2.00, 3.000, 4.000, 6.000, 8.000 ]
#rho = [ 1000.97, 1004.95, 1035.58, 1072.76, 1143.24, 1209.32, 1271.44, 1385.25, 1486.63 ]
#c = [ _m * _rho / 1000.0 for _m, _rho in zip( m, rho )]
c = [ 0.0005, 0.001, 0.002, 0.003, 0.005]
c_sqrt = np.sqrt(c)
# lmb1 = [ 0.5636, 1.088, 4.791, 8.750, 15.18, 19.91, 23.20, 26.32, 26.23 ]

#lmb = [ _l / _c for _c, _l in zip( c, lmb1 ) ]
lmb = [ 126.28, 125.47, 124.36, 123.56, 122.34 ]

lmb_0 = 128.24 #[ 128.28, 128.30, 128.37, 128.47, 128.68 ]

temperature = 298.15

eta = 8.937 * 10**(-4) 
eps = 78.3
eps0 = 8.854187817 * 10**(-12) # F / m
boltzmann_constant = 1.38064852 * 10**(-23) # J / k
avogadro = 6.022140857 * 10**(23) # mol-1
electron_charge = 1.6021766208 * 10**(-19) # C

b_e = avogadro * 2 * electron_charge**3 / ( 12 * np.pi * eta ) * np.sqrt( 2 * 10**3 * avogadro / ( eps * eps0 * boltzmann_constant * temperature ) )
print('be: {0}'.format(b_e))
print('2 * be: {0}'.format( 2 * b_e ))

b_p = electron_charge**3 / ( 12 * np.pi * eps * eps0 * boltzmann_constant * temperature ) * np.sqrt( 2 * 10**3 * avogadro / ( eps * eps0 * boltzmann_constant * temperature )) * 0.5 / ( 1 + np.sqrt(0.5) )
print('bp: {0}'.format(b_p))
print('bp * lambda0: {0}'.format( b_p * lmb_0 ))

B = electron_charge * np.sqrt( 2.0 * 10**3 * avogadro / ( eps * eps0 * boltzmann_constant * temperature ))
print('B: {0} * 10**-9'.format( B * 10**(-9) ))

c_dho_sqrt = np.linspace( min(c_sqrt), max(c_sqrt), 100 )
dho = [lmb_0 * 10**(-4) - ( 2 * b_e + b_p * lmb_0 * 10**(-4) ) * _c for _c in c_dho_sqrt ]

a = 4.7 * 10**(-10)
ofu = [lmb_0 * 10**(-4) - b_p * lmb_0 * 10**(-4) * _c - 2 * b_e * _c / (1 + a * B * _c) for _c in c_dho_sqrt]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

lw = 2.0

#ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
#ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.set_xlim( (0.02, 0.075) )
ax.set_ylim( (0.01215, 0.01265) )

label = ax.set_xlabel( r'$\sqrt{C}$', ha='left', va = 'top' )
label = ax.set_ylabel( r'$\Lambda$' )

patch2 = mpatches.Patch( color = 'b', label = 'Onzager-Fuoss' )
patch1 = mpatches.Patch( color = 'g', label = 'Debye-Huckel-Onzager' )

plt.scatter( c_sqrt, [l * 10**(-4) for l in lmb], marker = '^', s = 40, color = 'k' )
plt.plot(c_dho_sqrt, ofu, color = 'b', linewidth = 2.0 )
plt.plot( c_dho_sqrt, dho, color = 'g', linewidth = 2.0 )
plt.grid(linestyle=':', alpha=0.7)
plt.legend(handles = [patch1, patch2])
plt.show()

right_part = [ 2 * b_e * _c_sqrt / ( lmb_0 * 10**(-4) - _lmb *10**(-4) - b_p * lmb_0 * _c_sqrt * 10**(-4)) for _c_sqrt, _lmb in zip( c_sqrt, lmb)]

fp, residual, rank, sv, rcond = sp.polyfit( c_sqrt, right_part, 1, full = True )
f = sp.poly1d( fp )

print('fp[0]: {0}; fp[1]: {1}'.format(fp[0], fp[1]))

a = fp[0] / B
print('a: {0}'.format(a))

#plt.plot( c_dho_sqrt, f(c_dho_sqrt), color = 'k', linewidth = 2.0)
#plt.scatter( c_sqrt, right_part, marker = '^', s = 30, color = 'k')
#plt.grid(linestyle = ':', alpha = 0.7)
#plt.show()
