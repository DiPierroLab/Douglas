# script which loads, shows rows, and plots lambda matrices

# Load packages
from numpy import array, loadtxt, exp
from matplotlib.pyplot import plot, show, legend, xlim, xlabel, xlim, ylabel, ylim, xscale, yscale, axvline

# Path to lambdas matrix storage
file = '/Users/douglas/Documents/Features Transfer/store lambdas'

# Load lambdas matrices for different simulations
print('Loading matrices')
M41 = loadtxt(file+'/Lambdas41.txt', delimiter=',')
M49 = loadtxt(file+'/Lambdas49.txt', delimiter=',')
M55 = loadtxt(file+'/Lambdas55.txt', delimiter=',')
M56 = loadtxt(file+'/Lambdas56.txt', delimiter=',')
M57 = loadtxt(file+'/Lambdas57.txt', delimiter=',')
M58 = loadtxt(file+'/Lambdas58.txt', delimiter=',')
M59 = loadtxt(file+'/Lambdas59.txt', delimiter=',')
M60 = loadtxt(file+'/Lambdas60.txt', delimiter=',')
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
vec41 = M41[0:250,0]-M41[0,2499]
vec49 = M49[0:250,0]-M49[0,2499]
vec55 = M55[0:250,0]-M55[0,2499]
vec56 = M56[0:250,0]-M56[0,2499]
vec57 = M57[0:250,0]-M57[0,2499]
vec58 = M58[0:250,0]-M58[0,2499]
vec59 = M59[0:250,0]-M59[0,2499]
vec60 = M60[0:250,0]-M60[0,2499]

# Plot the lambdas slices. They should overlap.
plot(d*bead_size_new, vec41,'-', label='sim 41 ideal chromosome / 6 first  0 first 20 beads')
#plot(d*bead_size_new, vec49,'-', label='sim 49')#: IC/6   AA/2  extrapolation first 70 beads')
plot(d*bead_size_new, vec55,'--', label='sim 55')#: IC/6   AA/2  extrapolation first 70 beads  0 first 40 beads')
plot(d*bead_size_new, vec56,'--', label='sim 56')#: IC/6   AA/2  extrapolation first 70 beads  0 first 40 beads')
plot(d*bead_size_new, vec57,'--', label='sim 57')#: IC/6   AA/2  extrapolation first 70 beads  line first 40 beads')
plot(d*bead_size_new, vec58,'--', label='sim 58')#: IC/6   AA/2  0 first 40 beads line from 40 to 300 beads')
plot(d*bead_size_new, vec59,'--', label='sim 59')#: IC/6   AA/2  line first 40 beads line from 40 to 300 beads')
plot(d*bead_size_new, vec60,'--', label='sim 60')#: IC/6   AA/2  line first 40 beads line from 40 to 600 beads')
#plot(d*250,-exp(-d/420)/12-d/300000, label = 'NuChroM gamma fit')
#axvline(x = 40*bead_size_new, color = 'black', label='genomic distance with correct contact frequency')
xlabel('genomic distance away from the diagonal in base pairs')
#xscale('log')
ylabel('gamma')
#yscale('log')
legend()
#xlim(0,5e4)
#ylim(-.75,.01)
show()