# script which loads, shows rows, and plots lambda matrices

# Load packages
from numpy import array, loadtxt, exp
from matplotlib.pyplot import plot, show, legend, xlim, xlabel, xlim, ylabel, ylim, xscale, yscale, axvline

# Path to lambdas matrix storage
file = '/Users/douglas/Documents/Features Transfer/store lambdas'

# Load lambdas matrices for different simulations
print('Loading matrices')
M49 = loadtxt(file+'/Lambdas49.txt', delimiter=',')
M50 = loadtxt(file+'/Lambdas50.txt', delimiter=',')
M55 = loadtxt(file+'/Lambdas55.txt', delimiter=',')
M56 = loadtxt(file+'/Lambdas56.txt', delimiter=',')
print('Matrices loaded')
print('')

# Number of base pairs per bead before and after we stretched the ideal chromosome
bead_size_old = 5000
bead_size_new = 500

# 1D array of possible genomic distances in beads
d = array(range(250))
print(d)

# Make arrays for the first column of each lambdas matrix
#     Zero out AA type interactions; this leaves only ideal chromosome interactions
#     If you divided gamma by a number to make the lambdas matrix, then multiply back by it
vec49 = 6.0*(M49[0:250,0]-M49[0,2499])
vec50 = 6.0*(M50[0:250,0]-M50[0,2499])
vec55 = 6.0*(M55[0:250,0]-M55[0,2499])
vec56 = 6.0*(M56[0:250,0]-M56[0,2499])


# Plot the lambdas slices. They should overlap.
plot(d*bead_size_new, vec49,'-', label='IC/6   AA/2  extrapolation first 70 beads')
#plot(d*bead_size_new, vec50,'--', label='IC/6   AA/2  extrapolation first 100 beads')
#plot(d*bead_size_new, vec55,':', label='IC/6   AA/2  new')
plot(d*bead_size_new, vec56,':', label='IC/6   AA/2  extrapolation first 70 beads  0 first 40 beads')
plot(d*250,-exp(-d/420)/12-d/300000, label = 'NuChroM gamma fit')
axvline(x = 40*bead_size_new, color = 'black', label='genomic distance with correct contact frequency')
#xlabel('genomic distance away from the diagonal in base pairs')
#xscale('log')
ylabel('gamma')
#yscale('log')
legend()
#xlim(0,5e4)
#ylim(-.75,.01)
show()