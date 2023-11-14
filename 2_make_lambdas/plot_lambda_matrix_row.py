# script which loads, shows rows, and plots lambda matrices

# Load packages
from numpy import array, loadtxt
from matplotlib.pyplot import plot, show, legend, xlim

# Path to lambdas matrix storage
file = '/Users/douglas/Documents/Features Transfer/store lambdas'

# Load lambdas matrices for different simulations
print('loading M24')
M24 = loadtxt(file+'/Lambdas24.txt', delimiter=',')
print('loading M25')
M25 = loadtxt(file+'/Lambdas25.txt', delimiter=',')
print('loading M33')
M33 = loadtxt(file+'/Lambdas33.txt', delimiter=',')
print('loading M35')
M35 = loadtxt(file+'/Lambdas35.txt', delimiter=',')
print('loading M36')
M36 = loadtxt(file+'/Lambdas36.txt', delimiter=',')
print('')

# Number of base pairs per bead before and after we stretched the ideal chromosome
bead_size_old = 5000
bead_size_new = 500

# 1D array of possible genomic distances in beads
d = array(range(2500))
print(d)

# Make arrays for the first column of each lambdas matrix
#     Zero out AA type interactions; this leaves only ideal chromosome interactions
#     If you divided gamma by a number to make the lambdas matrix, then multiply back by it
vec24 = M24[0:2500,0]-M24[0,0]
vec25 = 5.0*(M25[0:2500,0]-M25[0,0])
#vec33 = 1.4*(M33[0:2500,0]-M33[0,1]) # M33[0,0]=0
vec35 = 1.4*(M35[0:2500,0]-M35[0,1]) # M34[0,0]=0
vec36 = 1.4*(M36[0:2500,0]-M36[0,1]) # M35[0,0]=0


# Plot the lambdas slices. They should overlap.
plot(d*bead_size_old, vec24,'s', label = '24')
plot(d*bead_size_new, vec25,'-', label = '25')
#plot(d*bead_size_new, vec33,'--', label = '33')
plot(d*bead_size_new, vec35,'.', label = '35')
plot(d*bead_size_new, vec36,'x', label = '36')
xlim(0,5e4)
legend()
show()