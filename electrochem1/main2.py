import matplotlib.pyplot as plt
import numpy as np

c = [ 0.050, 0.100, 0.500, 1.000, 2.00, 3.000, 4.000, 6.000, 8.000 ]
c_sqrt = np.sqrt(c)
lmb1 = [ 0.5636, 1.088, 4.791, 8.750, 15.18, 19.91, 23.20, 26.32, 26.23 ]

lmb = [ _l / _c / 1000.0 for _c, _l in zip( c, lmb1 ) ]


l_0 = 128.18 * 10**(-4)

c_dho = np.linspace( min(c), max(c), 100 )
c_dho_sqrt = np.sqrt( c_dho )
dho = [l_0 - ( 60.4 * 10**(-4) + 0.23 * l_0 ) * np.sqrt(_c) for _c in zip(  c_dho ) ]

plt.scatter( c_sqrt, lmb, marker = '^', s = 30, color = 'k' )
plt.plot( c_dho_sqrt, dho, color = 'k' )
plt.show()
