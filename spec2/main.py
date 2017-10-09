import matplotlib.pyplot as plt
import scipy as sp
import numpy as np

r_branch = [ 1330.45, 1332.84, 1335.25, 1337.65, 1340.05, 1342.37, 1344.82, 1347.19, 1349.58, 1351.99, 1354.45, 1356.82, 1359.24, 1361.67, 1364.05, 1366.55, 1368.90, 1371.45, 1373.84, 1376.28, 1378.77, 1381.19, 1383.67, 1386.21, 1388.45, 1390.90 ]
m_r_branch = [ _ for _ in range(1, len(r_branch) + 1) ]

p_branch = [ 1325.70, 1323.39, 1321.02, 1318.76, 1316.43, 1314.07, 1311.78, 1309.45, 1307.14, 1304.85, 1302.56, 1300.28, 1297.99, 1295.73, 1293.48, 1291.21, 1288.96, 1286.72, 1284.48, 1282.25, 1280.01, 1277.75, 1275.49, 1273.23, 1270.97, 1268.73, 1266.45, 1264.21, 1261.92 ]
m_p_branch = [ -_ for _ in range(1, len(p_branch) + 1) ]

print(m_p_branch)

branches = p_branch
branches.extend( r_branch )

m = m_p_branch
m.extend( m_r_branch )


fp1, residual1, rank1, sv1, rcond1 = sp.polyfit( m, branches, 2, full = True )
print('fp1[0]: {0}; fp1[1]: {1}; fp1[2]: {2}'.format( fp1[0], fp1[1], fp1[2] ))
f1 = sp.poly1d( fp1 )

x = np.linspace( min(m) - 1, max(m) + 1, 100 )

lw = 2.0
#plt.plot( x, f1(x), color = 'b', linewidth = lw ) 
#plt.scatter( m, branches, s = 40, marker = '^', color = 'k' )
#plt.grid( linestyle = ':', alpha = 0.7 )
#plt.show()

b_prime = 0.5 * ( fp1[0] + fp1[1] )
b_double_prime = 0.5 * ( fp1[1] - fp1[0] )
print("b': {0}; b'': {1}".format( b_prime, b_double_prime )) 

alpha = b_double_prime - b_prime 
print('alpha: {0}'.format(alpha))

be = 0.5 * ( 3 * b_double_prime - b_prime )
print('be: {0}'.format(be))

print('nu0: {0}'.format(fp1[2]))

planck_constant = 6.626070040 * 10**(-34) # j * s
light_speed = 299792458 * 100 # cm/s
inertia_tensor_h = planck_constant / ( 8 * np.pi**2 * light_speed * be ) * 10**(7)
print('inertia_tensor_h: {0}'.format(inertia_tensor_h))

be_d = 0.8479 
print('be_d: {0}'.format(be_d))
inertia_tensor_d = planck_constant / ( 8 * np.pi**2 * light_speed * be_d ) * 10**7
print('inertia_tensor_d: {0}'.format(inertia_tensor_d))

amu = 1.660539040 * 10**(-24)
m_h = 1.00782503233
m_d = 2.01410177812
m_c = 12.0000000

RH = np.sqrt( ( inertia_tensor_d - inertia_tensor_h ) / 2 / ( m_d - m_h ) / amu ) * 10**(-2)
print('RH: {0}'.format(RH))
RC = np.sqrt( inertia_tensor_h / ( 2 * m_c * amu ) - m_h / m_c * ( inertia_tensor_d - inertia_tensor_h ) / 2 / ( m_d - m_h ) / amu ) * 10**(-2)
print('RC: {0}'.format(RC))

rcc = 2 * RC
rch = RH - RC
print('r_cc: {0}'.format(rcc))
print('r_ch: {0}'.format(rch))
