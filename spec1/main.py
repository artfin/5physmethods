import matplotlib.pyplot as plt
import scipy as sp
import numpy as np

p_branch = [ 2101.8, 2112.2, 2122.2, 2132.1, 2141.7, 2151.1, 2160.2, 2169.2, 2177.8, 2186.2, 2194.3, 2202.2, 2209.8 ]
q_branch = [ 2080.5, 2069.5, 2058.3, 2046.8, 2035.2, 2023.3, 2011.2, 1999.0, 1986.5, 1973.9, 1961.0, 1948.0, 1934.8 ]
q_branch_reversed = [ _ for _ in reversed(q_branch) ]

p_branch_overtone = [ 4139.2, 4149.0, 4158.5, 4167.4, 4176.0, 4184.0, 4191.6, 4198.8, 4205.3, 4211.4, 4217.1]
q_branch_overtone = [ 4118.0, 4106.8, 4095.1, 4083.0, 4070.5, 4057.5, 4044.1, 4030.3, 4016.0, 4001.4, 3986.2]
q_branch_overtone_reversed = [ _ for _ in reversed(q_branch_overtone)]

m = [ -_ for _ in reversed(range(1, 14))]
m.extend( [_ for _ in range(1, 14)] )

m_overtone = [ -_ for _ in reversed(range(1, len(p_branch_overtone) + 1)) ]
m_overtone.extend( [_ for _ in range(1, len(q_branch_overtone) + 1)] )
print('m_overtone: {0}'.format( m_overtone))

q_branch_reversed.extend( p_branch )
q_branch_overtone_reversed.extend( p_branch_overtone )

fp1, residual1, rank1, sv1, rcond1 = sp.polyfit( m, q_branch_reversed, 2, full = True) 
f1 = sp.poly1d( fp1 )
print('fp1[0]: {0}; fp1[1]: {1}; fp1[2]: {2}'.format( fp1[0], fp1[1], fp1[2] ))

b_prime = 0.5 * (fp1[0] + fp1[1])
b_double_prime = 0.5 * (fp1[1] - fp1[0])
print('b_prime: {0}; b_double_prime: {1}'.format(b_prime, b_double_prime))

x = np.linspace( min(m), max(m), 100 )
lw = 1.5 
#plt.plot( x, f1(x), color = 'b', linewidth = lw ) 
#plt.scatter( m, q_branch_reversed, s = 40, marker = '^', color = 'k' )
#plt.grid( linestyle = ':', alpha = 0.7 )
#plt.show()

fp2, residual2, rank2, sv2, rcond2 = sp.polyfit( m, q_branch_reversed, 4, full = True )
f2 = sp.poly1d( fp2 )
print('fp2[0]: {0}; fp2[1]: {1}; fp2[2]: {2}; fp2[3]: {3}; fp2[4]: {4}'.format( fp2[0], fp2[1], fp2[2], fp2[3], fp2[4] ))

d_prime = - 0.5 * fp2[0] - 0.25 * fp2[1]
d_double_prime = 0.5 * fp2[0] - 0.25 * fp2[1]
b_prime = 0.5 * (fp2[3] + fp2[2] - fp2[0] )
b_double_prime = 0.5 * ( fp2[3] - fp2[2] + fp2[0] )
print('b_prime: {0}; b_double_prime: {1}'.format(b_prime, b_double_prime))
print('d_prime: {0}; d_double_prime: {1}'.format(d_prime, d_double_prime))

d_e = 0.5 * ( 5 * d_prime - 3 * d_double_prime )
print('De: {0}'.format(d_e))
#plt.scatter( m, q_branch_reversed, s = 20, color = 'k'  )
#plt.plot( x, f2(x), color = 'red',  linewidth = 2.0 ) 
#plt.show()

print( 'len(m_overtone): {0}'.format(len(m_overtone)))
print( 'len(q_branch_reversed): {0}'.format( len(q_branch_reversed)) )

x = np.linspace( min(m), max(m), 100 )
fp3, residual3, rank3, sv3, rcond3 = sp.polyfit( m_overtone, q_branch_overtone_reversed, 2, full = True )
f3 = sp.poly1d( fp3 )
print('fp3[0]: {0}; fp3[1]: {1}; fp3[2]: {2}'.format( fp3[0], fp3[1], fp3[2] ))

b_prime = 0.5 * (fp3[0] + fp3[1])
b_double_prime = 0.5 * (fp3[1] - fp3[0])
print('b_prime: {0}; b_double_prime: {1}'.format(b_prime, b_double_prime))

#plt.scatter( m_overtone, q_branch_overtone_reversed, s = 20, color = 'k', marker = '^' )
#plt.plot( x, f3(x), color = 'red', linewidth = lw )
#plt.grid( linestyle = ':', alpha = 0.7 )
#plt.show()

fp4, residual4, rank4, sv4, rcond4 = sp.polyfit( m_overtone, q_branch_overtone_reversed, 4, full = True )
f4 = sp.poly1d( fp4 )

print('fp4[0]: {0}; fp4[1]: {1}; fp4[2]: {2}; fp4[3]: {3}; fp4[4]: {4}'.format( fp4[0], fp4[1], fp4[2], fp4[3], fp4[4] ))

d_prime = - 0.5 * fp4[0] - 0.25 * fp4[1]
d_double_prime = 0.5 * fp4[0] - 0.25 * fp4[1]
b_prime = 0.5 * (fp4[3] + fp4[2] - fp4[0] )
b_double_prime = 0.5 * ( fp4[3] - fp4[2] + fp4[0] )
print('b_prime: {0}; b_double_prime: {1}'.format(b_prime, b_double_prime))
print('d_prime: {0}; d_double_prime: {1}'.format(d_prime, d_double_prime))

light_speed = 299792458.0 * 100.0 # cm/s
boltzmann = 1.38064852 * 10**(-23)
planck = 6.62607004 * 10**(-34) # J / s
protium_mass = 1.00782503223
chlorine_mass =  34.968852682
deuterium_mass = 2.01410177812
mu = (chlorine_mass * deuterium_mass) / (chlorine_mass + deuterium_mass) * 10**(-3) # mass in kg/mol
avogadro = 6.022140857 * 10**(23)
be_1 = 5.448794
re_1 = 1 / np.sqrt( 8 * be_1 * np.pi**2 * light_speed * mu / avogadro / planck )
print('re_1: {0}'.format(re_1))

omega_e1 = 2144.96
omegax_e1 = 26.85
omega_e2 = 2145.01
omegax_e2 = 26.87

de1 = omega_e1**2 / ( 4 * omegax_e1 )
beta1 = 0.2435576 * ( mu * 10**3 * omegax_e1 )**0.5

de2 = omega_e2**2 / ( 4 * omegax_e2 )
beta2 = 0.2435576 * ( mu * 10**3 * omegax_e2 )**0.5

re1 = 1.278
re2 = 1.275

x = np.linspace( 0.5, 5.0, 100 )
morse1 = de1 * ( 1 - np.exp( - beta1 * (x - re1)))**2 / 8065.0
morse2 = de2 * ( 1 - np.exp( - beta2 * (x - re2)))**2 / 8065.0

#plt.xlim((0.4, 5.0))
#plt.ylim((0.0, 7.0))

#plt.ylabel(r'U, eV')
#plt.xlabel(r'r, A')

#plt.plot( x, morse2, linewidth = lw * 1.3, color = 'b', linestyle = '-')
#plt.grid( linestyle = ':', alpha = 0.7 )
#plt.show()


j = [ _ for _ in reversed(range(1, 14))]
#j.extend( [_ for _ in range(1, 14)] )

bv = 5.391
temperature = 300
_population = [ (2 * _j + 1) * np.exp( - bv * light_speed * planck * _j * (_j + 1) / ( boltzmann * temperature)) for _j in j]
population = [ _ / max(_population) for _ in _population]

spec_j = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
spec_pop = [0.2138, 0.2888, 0.3138, 0.3333, 0.325, 0.297, 0.2666]
spec_pop = [ _ / max(spec_pop) for _ in spec_pop]

#plt.scatter( j, population, marker = 'o', color = 'b', s = 30 )
#plt.scatter( spec_j, spec_pop, marker = 'o', color = 'r', s = 30 )
#plt.grid( linestyle = ':', alpha = 0.7)
#plt.show()

mu_hcl = protium_mass * chlorine_mass / ( protium_mass + chlorine_mass ) * 10**(-3)
rho = np.sqrt( mu_hcl / mu )
print('rho: {0}'.format(rho))

omega_e_hcl = omega_e1 * rho**(-1)
be_hcl = be_1 * rho**(-2)
omegax_e_hcl = omegax_e1 * rho**(-2)

b_prime_hcl = b_prime * rho**(-2)
b_double_prime_hcl = b_double_prime * rho**(-2)

nu01_hcl = 2091.26 * rho**(-1)

nu_hcl = [ nu01_hcl + (b_prime_hcl + b_double_prime_hcl) * _m + (b_prime_hcl - b_double_prime_hcl) * _m**2 - 29.72 for _m in m]

print('omega_e_hcl: {0}'.format(omega_e_hcl))
print('be_hcl: {0}'.format(be_hcl))
print('omegax_e_hcl: {0}'.format(omegax_e_hcl))

print('b_prime_hcl: {0}; b_double_prime_hcl: {1}'.format(b_prime_hcl, b_double_prime_hcl))

print('nu01_hcl: {0}'.format(nu01_hcl))

for _m, _nu in zip(m, nu_hcl):
	print('m: {0}; nu: {1}'.format(_m, _nu))

