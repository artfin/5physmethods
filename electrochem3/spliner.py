import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline 
import numpy as np

mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.unicode'] = True

mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = 'Times'

mpl.rcParams['figure.titlesize'] = "xx-large"
mpl.rcParams['legend.fontsize'] = "large"
mpl.rcParams['axes.labelsize'] = "x-large"
mpl.rcParams['axes.titlesize'] = "large"

mpl.rcParams['xtick.labelsize'] = 15 
mpl.rcParams['ytick.labelsize'] = 15 

# celcius
temperatures = [ 0.0, 0.1, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0 ]
temperatures = [ t + 273.15 for t in temperatures ]

epsilon = [ 87.740, 87.700, 85.763, 83.832, 81.946, 80.103, 78.304, 76.546, 74.828, 73.151, 71.512, 69.910, 68.345, 66.815, 65.319, 63.857, 62.427, 61.027, 59.659, 58.319, 57.007 ]

spl = UnivariateSpline( temperatures, epsilon )

#der = spl.derivative()
#eps_der = [ der(298.0), der(360.0) ]
#print('derivative 298K: {0}'.format(eps_der[0]))
#print('derivative 360K: {0}'.format(eps_der[1]))

#xs = np.linspace( temperatures[0], temperatures[-1], 100 )
#plt.title(r'\LARGE Temperature dependence of dielectric constant of water')
#plt.xlabel(r'Temperature, K')
#plt.ylabel(r'$\varepsilon$')
#plt.scatter( temperatures, epsilon, color = 'k', marker = '^', s = 20  )
#plt.plot( xs, spl(xs), 'k', lw = 2 )
#plt.grid( linestyle = ':', alpha = 0.7 )
#plt.show()

temperature = [ 298.0, 360.0 ]
delta_g = 157.0 # kJ/mol
Na = 6.022140857 * 10**(23)
e_charge = 1.6021766208 * 10**(-19)
eps0 = 8.854187817 *10**(-12)

epsilon = [ spl(298.0), spl(360.0)] # 298K, 360K
print('epsilon(298K): {0}'.format(epsilon[0]))
print('epsilon(360K): {0}'.format(epsilon[1]))

radii =  1.0/delta_g * Na * e_charge**2 / (8 * np.pi * eps0) * (1.0 - 1.0/epsilon[0]) * 10**(-3)
print('radii: {0}'.format(radii))

delta_g = -Na * e_charge**2 / (8 * np.pi * eps0 * radii) * (1.0 - 1.0/epsilon[1])
print('delta_g(360K): {0}'.format(delta_g))


