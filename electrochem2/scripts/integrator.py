import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

def integrate( f, x0, x1 ):
    return 0.5 * (x1 - x0) * (f(x0) + f(x1))

data = np.loadtxt("kolb1986_figure8.csv", delimiter = ',' )

phi = data[:,0]
C = data[:,1]
spline = interp1d( phi, C, kind = 'cubic' )
xnew = np.linspace( min(phi), max(phi), 100 )

pzc = 0.32 # V

N = 300 
phi_values = []
q_values = []

for i in range( N - 1 ):
    phi_value = phi[0] + (pzc - phi[0]) / (N - 1) * i
    q_value = integrate( spline, phi_value, pzc )
    phi_values.append( phi_value )
    q_values.append( - q_value )

for i in range( N - 1 ):
    phi_value = pzc + (phi[-1] - pzc) / (N - 1) * i
    q_value = integrate( spline, pzc, phi_value )
    phi_values.append( phi_value )
    q_values.append( q_value )

F = 96485.33289 # C * mol^{-1}
R = 8.314 # J * mol^{-1} * K^{-1}
T = 298 # K
A = 5.87 # for H2O, 298 K
c_hclo4 = 0.01

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

plt.title( r'\LARGE Surface charge as a function of potential in 0.01M $HClO_4$' )
plt.xlabel('$U_{SCE}$, V' )
plt.ylabel('q, $\mu$C $\cdot$ cm$^{-2}$')

plt.plot( phi_values, q_values, color = 'k' )
plt.scatter( [pzc], [0.0], color = 'r', s = 40 )
plt.grid( linestyle = ':', alpha = 0.7 )
plt.show()

C2_values = [ F / (R * T) * np.sqrt( 4 * A**2 * c_hclo4  + q**2 ) for q in q_values ]
C_values = spline(phi_values) # values of C based on spline

plt.plot( phi, C, color = 'k', linewidth = 2.0, linestyle = '-' )
plt.plot( phi_values, C2_values, color = 'r', linewidth = 2.0, linestyle = '-' )
plt.grid( linestyle = ':', alpha = 0.7 )
plt.show()

C20_values = [ c * c2 / ( c2 - c ) for c, c2 in zip( C_values, C2_values )]

plt.title(r'\LARGE Double-layer capacity of dense layer as a function of potential in 0.01M $HClO_4$')
plt.xlabel('$U_{SCE}$, V')
plt.ylabel('$C_{H}$, $\mu$F $\cdot$ cm$^{-2}$')
plt.plot( phi_values, C20_values, color = 'k', linewidth = 2.0, linestyle = '-' )
plt.grid( linestyle = ':', alpha = 0.7 )
plt.show()

