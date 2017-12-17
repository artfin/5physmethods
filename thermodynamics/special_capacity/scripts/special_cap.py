import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.interpolate import UnivariateSpline 
from pprint import pprint

def celcius_to_kelvin( temp ):
    return [ t + 273.15 for t in temp ]

def read_file( filename, n ):
    with open( filename, mode = 'r' ) as inputfile:
        lines = inputfile.readlines()

    lists = [ [] for i in range(n) ] 
    for line in lines:
        data = line.split(',')
        if '#' not in line and len(line.split()) > 0:
            for i, l in zip(range(n), lists):
                l.append( float(data[i]) )

    return lists 

def plot( time, temp, dsc, dsc_corr = [], bounds = [] ):
    if bounds:
        fp, residual, rank, sv, rcond = sp.polyfit( time[bounds[0][0]:bounds[0][1]], dsc[bounds[0][0]:bounds[0][1]], 1, full = True )
        f = sp.poly1d( fp )
        mean_value = fp[0] * 0.5 * (time[bounds[0][1]] + time[bounds[0][0]]) + fp[1] 
        #print('mean_value: {0}'.format(mean_value))

        fp2, residual, rank, sv, rcond = sp.polyfit( time[bounds[1][0]:bounds[1][1]], dsc[bounds[1][0]:bounds[1][1]], 1, full = True )
        f2 = sp.poly1d( fp2 )
        mean_value2 = fp2[0] * 0.5 * (time[bounds[1][1]] + time[bounds[1][0]]) + fp2[1]  
        #print('mean_value2: {0}'.format(mean_value2))

    fig, ax1 = plt.subplots()
    plt.grid( linestyle = ':', alpha = 0.7 )
    
    ax1.scatter( time, temp, color = 'r', s = 3, marker = 'o' )
    ax1.set_xlabel('time(s)')
    ax1.set_ylabel('Temperature, K', color = 'r')
    ax1.tick_params('y', colors = 'r')

    ax2 = ax1.twinx()
    ax2.scatter( time, dsc, color = 'k', s = 3, marker = 'o' )
    if dsc_corr: ax2.scatter( time, dsc_corr, color = 'g', s = 3, marker = 'o' )
    ax2.set_ylabel('DSC signal', color = 'k' )
    ax2.tick_params('y', colors = 'k')


    if bounds:
        x = np.linspace( time[bounds[0][0]], time[bounds[0][1]], 100)
        ax2.plot( x, f(x), color = 'y', lw = 3.0, linestyle = 'dashed')
        x = np.linspace( time[bounds[1][0]], time[bounds[1][1]], 100)
        ax2.plot( x, f2(x), color = 'y', lw = 3.0, linestyle = 'dashed')

        return [ [0.5 * (bounds[0][1] + bounds[0][0]), mean_value], 
                 [0.5 * (bounds[1][1] + bounds[1][0]), mean_value2]
               ]

def remove_drift( time, dsc, mv, mv2 ):
    fp, residual, rank, sv, rcond = sp.polyfit( [mv[0], mv2[0]], [mv[1], mv2[1]], 1, full = True )
    print(fp[0], fp[1])

    dsc_rm_drift = []
    for t, d in zip( time, dsc ):
        drift = fp[0] * t + fp[1]
        dsc_rm_drift.append( d - drift )

    return dsc_rm_drift
    

temp_bline, time_bline, dsc_bline, sensitivity_bline, segment_bline = read_file( '../ExpDat_03881-2_bline_-30-180_10_Ar-20-70_03.04.12.csv', 5 )
temp_sapp, time_sapp, dsc_sapp, sensitivity_sapp, segment_sapp = read_file( '../ExpDat_03882_Sapp-12.69mg-0.25mm_-30-180_10_Ar-20-.csv', 5 )
temp_quartz, time_quartz, dsc_quartz, sensitivity_quartz, segment_quartz = read_file( '../ExpDat_03883_quartz_-30-180_10_Ar-20-70_03.04.12.csv', 5)

temp_bline = celcius_to_kelvin( temp_bline )
temp_sapp = celcius_to_kelvin( temp_sapp )
temp_quartz = celcius_to_kelvin( temp_quartz )

mv, mv2 = plot( time_bline, temp_bline, dsc_bline, bounds = [[700, 1000], [3800, 4090]] )
print(mv)
print(mv2)

dsc_bline_corr = remove_drift( time_bline, dsc_bline, mv, mv2 )

plot( time_bline, temp_bline, dsc_bline, dsc_bline_corr )

#for t, d, d_corr in zip(time_bline, dsc_bline, dsc_bline_corr):
    #print(t, d, d_corr)

plt.show()


