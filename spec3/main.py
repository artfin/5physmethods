import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import scipy as sp

def read_file( filename ):
    with open( filename, mode = 'r' ) as inputfile:
        lines = inputfile.readlines()

    freqs = []
    intensities = []

    for line in lines:
        data = line.split()

        freqs.append( float(data[0]) )
        intensities.append( float(data[1]) )

    return freqs, intensities

def find_max( arr ):
    return max( arr )

freqs_0_1, ints_0_1 = read_file( 'HNO3/0_1.txt' )
freqs_0_2, ints_0_2 = read_file( 'HNO3/0_2.txt' )
freqs_0_4, ints_0_4 = read_file( 'HNO3/0_4.txt' )
freqs_0_6, ints_0_6 = read_file( 'HNO3/0_6.txt' )
freqs_0_8, ints_0_8 = read_file( 'HNO3/0_8.txt' )
freqs_2, ints_2 = read_file( 'HNO3/2.txt' )
freqs_4, ints_4 = read_file( 'HNO3/4.txt' )
freqs_6, ints_6 = read_file( 'HNO3/6.txt' )
freqs_8, ints_8 = read_file( 'HNO3/8.txt' )
freqs_10, ints_10 = read_file( 'HNO3/10.txt' )
freqs_12, ints_12 = read_file( 'HNO3/12.txt' )
freqs_14, ints_14 = read_file( 'HNO3/14.txt' )

concentrations = [ 0.1, 0.2, 0.4, 0.6, 0.8 ]
heights = [ find_max(ints_0_1), find_max(ints_0_2), find_max( ints_0_4 ), find_max( ints_0_6), find_max( ints_0_8 ) ]

x = np.linspace( 0.1, 0.9 )
fp, residual, rank, sv, rcond = sp.polyfit( concentrations, heights, 1, full = True )
f = sp.poly1d( fp )

print('fp[0]: {0}; fp[1]: {1}'.format( fp[0], fp[1]) )

heights_high = [ find_max( _ ) for _ in [ints_2, ints_4, ints_6, ints_8, ints_10, ints_12, ints_14] ]
conc_high = [ ( h - fp[1] ) / fp[0] for h in heights_high ]

print('conc_high: {0}'.format(conc_high) )

c_hno3 = [ 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0 ]

kc = [ c_no3**2 / ( hno3 - c_no3 ) for c_no3, hno3 in zip( conc_high, c_hno3 ) ]
print('kc: {0}'.format( kc ))

lg_kc = np.log( kc )

fp2, residual2, rank2, sv2, rcond2 = sp.polyfit( c_hno3, lg_kc, 1, full = True )
f2 = sp.poly1d( fp2 )

x = np.linspace( 1.0, 15.0, 100 )

print('fp2[0]: {0}; fp2[1]: {1}'.format( fp2[0], fp2[1] ))

lw = 2.0
plt.scatter( c_hno3, lg_kc, marker = '^', s = 30 )
plt.plot( x, f2(x), color = 'k', linewidth = lw )
plt.grid( linestyle = ':', alpha = 0.7 ) 
plt.show()

#lw = 2.0
#plt.plot( x, f(x), linewidth = lw, color = 'k' )
#plt.scatter( concentrations, heights, linewidth = lw, marker = '^', s = 30 )
#plt.grid( linestyle = ':', alpha = 0.7 )
#plt.show()

# -------------------------------------------------------------
#patch1 = mpatches.Patch( color = 'r', label = '0.2M' )
#patch2 = mpatches.Patch( color = 'b', label = '0.4M' )
#patch3 = mpatches.Patch( color = 'g', label = '0.6M' )
#patch4 = mpatches.Patch( color = 'y', label = '0.8M' )

#plt.plot( freqs_0_2, ints_0_2, linewidth = lw, color = 'r' )
#plt.plot( freqs_0_4, ints_0_4, linewidth = lw, color = 'b' )
#plt.plot( freqs_0_6, ints_0_6, linewidth = lw, color = 'g' )
#plt.plot( freqs_0_8, ints_0_8, linewidth = lw, color = 'y' )

#plt.plot( freqs_1, ints_1, linewidth = lw )
#plt.plot( freqs_2, ints_2, linewidth = lw )
#plt.plot( freqs_4, ints_4, linewidth = lw )
#plt.plot( freqs_6, ints_6, linewidth = lw )
#plt.plot( freqs_8, ints_8, linewidth = lw )
#plt.plot( freqs_10, ints_10, linewidth = lw )
#plt.plot( freqs_12, ints_12, linewidth = lw )
#plt.plot( freqs_14, ints_14, linewidth = lw )

#plt.xlim( (900.0, 1100.0) )

#plt.grid( linestyle = ':', alpha = 0.7 )
#plt.show()
