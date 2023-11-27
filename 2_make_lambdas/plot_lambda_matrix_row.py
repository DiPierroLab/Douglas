# script which loads, shows rows, and plots lambda matrices

# Load packages
from numpy import array, loadtxt
from matplotlib.pyplot import plot, show, legend, xlim, xlabel, xlim, ylabel, ylim

# Path to lambdas matrix storage
file = '/Users/douglas/Documents/Features Transfer/store lambdas'

# Load lambdas matrices for different simulations
print('Loading matrices')
#M24 = loadtxt(file+'/Lambdas24.txt', delimiter=',')
#M25 = loadtxt(file+'/Lambdas25.txt', delimiter=',')
#M35 = loadtxt(file+'/Lambdas35.txt', delimiter=',')
#M36 = loadtxt(file+'/Lambdas36.txt', delimiter=',')
#M37 = loadtxt(file+'/Lambdas37.txt', delimiter=',')
#M38 = loadtxt(file+'/Lambdas38.txt', delimiter=',')
M39 = loadtxt(file+'/Lambdas39.txt', delimiter=',')
M45 = loadtxt(file+'/Lambdas45.txt', delimiter=',')
M48 = loadtxt(file+'/Lambdas48.txt', delimiter=',')
M49 = loadtxt(file+'/Lambdas49.txt', delimiter=',')
M50 = loadtxt(file+'/Lambdas50.txt', delimiter=',')
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
#vec35 = 1.4*(M35[0:2500,0]-M35[0,1])
#vec36 = 1.4*(M36[0:2500,0]-M36[0,1])
#vec37 = 4.0*(M37[0:2500,0]-M37[0,1])
#vec38 = 4.0*(M38[0:2500,0]-M38[0,1])
vec39 = 6.0*(M39[0:2500,0]-M39[0,1])
vec45 = 6.0*(M45[0:2500,0]-M45[0,2500])
vec48 = 6.0*(M48[0:2500,0]-M48[0,2500])
vec49 = 6.0*(M49[0:2500,0]-M49[0,2500])
vec50 = 6.0*(M50[0:2500,0]-M50[0,2500])


# Plot the lambdas slices. They should overlap.
#plot(d*bead_size_old, vec24,'s', label = '24')
#plot(d*bead_size_new, vec25,'-', label = '25')
#plot(d*bead_size_new, vec35,'-', label = '35')
#plot(d*bead_size_new, vec36,'--', label = '36')
#plot(d*bead_size_new, vec37,'-.', label = '37')
#plot(d*bead_size_new, vec38,':', label = '38')
plot(d*bead_size_new, vec39,'-', label = '39')
plot(d*bead_size_new, vec45,'--', label = '45')
plot(d*bead_size_new, vec48,'-.', label = '48')
plot(d*bead_size_new, vec49,':', label = '49')
plot(d*bead_size_new, vec50,'-', label = '50')
xlabel('genomic distance away from the diagonal in base pairs')
#xscale('log')
ylabel('gamma')
#yscale('log')
legend()
xlim(0,5e4)
#ylim(-6,1)
show()