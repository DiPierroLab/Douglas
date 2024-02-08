# script which loads, shows rows, and plots lambda matrices

# Load packages
from numpy import array, loadtxt, exp
from matplotlib.pyplot import plot, show, legend, xlim, xlabel, xlim, ylabel, ylim, xscale, yscale, axvline

# Path to lambdas matrix storage
file = '/Users/douglas/Documents/Features Transfer/store lambdas'

# Load lambdas matrices for different simulations
print('Loading matrices')

M2 = loadtxt(file+'/Lambdas2.txt', delimiter=',')
M59 = loadtxt(file+'/Lambdas59.txt', delimiter=',')
print('Matrices loaded')
print('')

# Number of base pairs per bead before and after we stretched the ideal chromosome
bead_size_new = .500

# 1D array of possible genomic distances in beads
d = array(range(250))

# Make arrays for the first column of each lambdas matrix
#     Zero out AA type interactions; this leaves only ideal chromosome interactions
#     If you divided gamma by a number to make the lambdas matrix, then multiply back by it
vec2 = M2[0:250,0]-M2[0,2499]
vec59 = M59[0:250,0]-M59[0,2499]
vec78 = loadtxt('/Users/douglas/Documents/DiPierroLab_Douglas/2_make_lambdas/gammas_78.txt', delimiter=',')
vec78 = vec78[0:250]

# Plot the lambdas slices. They should overlap.
plot(d*bead_size_new, vec2,':', label='sim 2')
plot(d*bead_size_new, vec59,'o', label='sim 59')#: IC/6   AA/2  line first 40 beads line from 40 to 600 beads')
plot(d*bead_size_new, vec78,'-', label='sim 78')
#plot(d*250,-exp(-d/420)/12-d/300000, label = 'NuChroM gamma fit')
#axvline(x = 40*bead_size_new, color = 'black', label='genomic distance with correct contact frequency')
xlabel('genomic distance from diagonal in kb')
#xscale('log')
ylabel('gamma')
#yscale('log')
legend()
#xlim(0,5e4)
#ylim(-.75,.01)
show()