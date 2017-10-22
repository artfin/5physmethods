#import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

FILENAME = 'main.tex'

def analyze( j_br, br ):
    fp, residual, rank, sv, rcond = sp.polyfit( j_br, br, 2, full = True )
    print('fp[0]: {0}; fp[1]: {1}; fp[2]: {2}'.format( fp[0], fp[1], fp[2] ))
    return fp

def make_tex_header_code( filename ):
    with open( filename, mode = 'w' ) as outputfile:
        outputfile.write(r'\documentclass[14pt]{extarticle}' + "\n" + "\n")
        outputfile.write(r'\usepackage{tabularx}' + "\n" + "\n")
        outputfile.write(r'\begin{document}' + "\n" + "\n")

def make_tex_foot_code( filename ):
    with open( filename, mode = 'a' ) as outputfile:
        outputfile.write(r'\end{document}' + "\n")
        
def generate_table_code( filename, pbr, rbr, jpbr, jrbr ):

    with open( filename, mode = 'a' ) as outputfile:
        outputfile.write(r'\begin{table}' + "\n")
        outputfile.write(r'\centering' + "\n")
        outputfile.write(r'\begin{tabular}{|c|c|c|c|}' + "\n")
        outputfile.write(r'\hline' + "\n") 
        outputfile.write(r'J & $\nu$(P(J) & $\nu$R(J) & m \\' + "\n")
        outputfile.write(r'\hline' + "\n")

        for p, m in zip( pbr, jpbr ):
            outputfile.write(str(-m) + '& ' + str(p) + ' & ' + '& ' + str(m) + r' \\' + "\n" )
        for r, m in zip( rbr, jrbr ):
            outputfile.write(str(m - 1) + '& & ' + str(r) + ' & ' + str(m) + r' \\' + "\n")

        outputfile.write('\hline' + "\n")
        outputfile.write('\end{tabular}' + "\n")
        outputfile.write('\end{table}' + "\n" + "\n")


make_tex_header_code( FILENAME )

p_branch = [ 2998.96, 2988.84, 2978.88, 2968.57, 2958.26, 2947.95, 2937.44, 2926.92, 2916.72, 2906.53, 2895.06, 2885.10 ]
r_branch = [ 3028.67, 3038.42, 3048.09, 3057.63, 3067.18, 3076.57, 3085.86, 3095.16, 3104.34, 3113.38, 3122.43, 3131.33, 3140.16, 3148.89, 3157.56 ]

j_p_branch = [ -_ for _ in range(2, len(p_branch) + 2) ]
j_r_branch = [ _ for _ in range(1, len(r_branch) + 1) ]

p_branch_copy = [_ for _ in p_branch] 
j_p_branch_copy = [_ for _ in j_p_branch]

branches = p_branch
branches.extend( r_branch )

m = j_p_branch
m.extend( j_r_branch )

fp = analyze( m, branches )
f = sp.poly1d( fp )

x = np.linspace( min(m), max(m), 100 )

p_branch = [ _ for _ in reversed(p_branch_copy) ]
j_p_branch = [_ for _ in reversed(j_p_branch_copy) ]

#generate_table_code( FILENAME, p_branch, r_branch, j_p_branch, j_r_branch )

##########################################################################

p_branch = [ 1299.79, 1294.48, 1289.08, 1283.20, 1277.37, 1271.43, 1265.51, 1259.71, 1253.63, 1247.75 ]
r_branch = [ 1311.39, 1316.81, 1322.07, 1327.21, 1332.48, 1337.63, 1342.71, 1347.95, 1353.06 ]

j_p_branch = [ -_ for _ in range(1, len(p_branch) + 1) ]
j_r_branch = [ _ for _ in range(1, len(r_branch) + 1) ]

p_branch_copy = [_ for _ in p_branch] 
j_p_branch_copy = [_ for _ in j_p_branch]

branches = p_branch 
branches.extend( r_branch )

m = j_p_branch 
m.extend( j_r_branch )

fp = analyze(m, branches )
f = sp.poly1d( fp )

x = np.linspace( min(m), max(m), 100 )

p_branch = [ _ for _ in reversed(p_branch_copy) ]
j_p_branch = [_ for _ in reversed(j_p_branch_copy) ]

#generate_table_code( FILENAME, p_branch, r_branch, j_p_branch, j_r_branch )

#make_tex_foot_code( FILENAME )

##########################################################################

#plt.plot( x, f(x), color = 'k', linestyle = 'dashed', linewidth = 2.0 )
#plt.scatter( j_r_branch, r_branch, marker = '^', color = 'k', s = 30 )
#plt.scatter( j_p_branch, p_branch, marker = '^', color = 'k', s = 30 )
#plt.grid( linestyle = ':', alpha = 0.7 )
#plt.show()

