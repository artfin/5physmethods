from scipy.optimize import fsolve
import math

c1 = 9.83268
c2 = -0.0380361
c3 = 5.515481
c4 = -0.0291516

def equations( p ):
    b13, b14, b0, z3, z4 = p
    return ( b13 + b0 - 2 * z3 * b13 - c1,
             b13 - b0 - c2,
             b14 + b0 - 2 * z4 * b14 - c3,
             b14 - b0 - c4,
             z3 + z4 - 0.5 )

b13, b14, b0, z3, z4 = fsolve( equations, (5.1996, 5.1687, 5.241, 0.036, 0.464) )

print('b13: {0}'.format(b13))
print('b14: {0}'.format(b14))
print('b0: {0}'.format(b0))
print('dzeta_3: {0}'.format(z3))
print('dzeta_4: {0}'.format(z4))

print equations( (b13, b14, b0, z3, z4) ) 
