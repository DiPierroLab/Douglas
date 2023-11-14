# script which loads, shows rows, and plots lambda matrices

# Load packages
from numpy import array, loadtxt
from matplotlib.pyplot import plot, show, legend, xlim

# Path to lambdas matrix storage
file = '/Users/douglas/Documents/Features Transfer/store lambdas'

# Load lambdas matrices for different simulations
print('Loading matrices')
#M24 = loadtxt(file+'/Lambdas24.txt', delimiter=',')
#M25 = loadtxt(file+'/Lambdas25.txt', delimiter=',')
#M33 = loadtxt(file+'/Lambdas33.txt', delimiter=',')
M35 = loadtxt(file+'/Lambdas35.txt', delimiter=',')
M36 = loadtxt(file+'/Lambdas36.txt', delimiter=',')
M37 = loadtxt(file+'/Lambdas37.txt', delimiter=',')
M38 = loadtxt(file+'/Lambdas38.txt', delimiter=',')
M39 = loadtxt(file+'/Lambdas39.txt', delimiter=',')
M40 = loadtxt(file+'/Lambdas40.txt', delimiter=',')
print('Matrices loaded')
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
#vec24 = M24[0:2500,0]-M24[0,0]
#vec25 = 5.0*(M25[0:2500,0]-M25[0,1])
#vec33 = 1.4*(M33[0:2500,0]-M33[0,1])
vec35 = 1.4*(M35[0:2500,0]-M35[0,1])
vec36 = 1.4*(M36[0:2500,0]-M36[0,1])
vec37 = 4.0*(M37[0:2500,0]-M37[0,1])
vec38 = 4.0*(M38[0:2500,0]-M38[0,1])
vec39 = 6.0*(M39[0:2500,0]-M39[0,1])
vec40 = 6.0*(M40[0:2500,0]-M40[0,1])


# Plot the lambdas slices. They should overlap.
#plot(d*bead_size_old, vec24,'s', label = '24')
#plot(d*bead_size_new, vec25,'-', label = '25')
#plot(d*bead_size_new, vec33,'--', label = '33')
plot(d*bead_size_new, vec35,'-', label = '35')
plot(d*bead_size_new, vec36,'--', label = '36')
plot(d*bead_size_new, vec37,'-.', label = '37')
plot(d*bead_size_new, vec38,':', label = '38')
plot(d*bead_size_new, vec39,'.', label = '39')
plot(d*bead_size_new, vec40,'o', label = '40')
xlim(0,5e4)
legend()
show()