# script which loads, shows rows, and plots lambda matrices

# Load packages
from numpy import array, loadtxt, exp
from matplotlib.pyplot import plot, show, legend, xlim, xlabel, xlim, ylabel, ylim, xscale, yscale, axvline, title

# Path to lambdas matrix storage
file_lambdas = '/Users/douglas/Documents/Features Transfer/store lambdas'

# Load lambdas matrices for different simulations
print('Loading matrices')

#M59 = loadtxt(file_lambdas+'/Lambdas59.txt', delimiter=',')
M75 = loadtxt(file_lambdas+'/Lambdas75.txt', delimiter=',')
M76 = loadtxt(file_lambdas+'/Lambdas76.txt', delimiter=',')
M77 = loadtxt(file_lambdas+'/Lambdas77.txt', delimiter=',')
M78 = loadtxt(file_lambdas+'/Lambdas78.txt', delimiter=',')
M79 = loadtxt(file_lambdas+'/Lambdas79.txt', delimiter=',')
M80 = loadtxt(file_lambdas+'/Lambdas80.txt', delimiter=',')
M81 = loadtxt(file_lambdas+'/Lambdas81.txt', delimiter=',')
M82 = loadtxt(file_lambdas+'/Lambdas82.txt', delimiter=',')
M83 = loadtxt(file_lambdas+'/Lambdas83.txt', delimiter=',')
M84 = loadtxt(file_lambdas+'/Lambdas84.txt', delimiter=',')
M85 = loadtxt(file_lambdas+'/Lambdas85.txt', delimiter=',')
print('Matrices loaded')
print('')

# Number of base pairs per bead before and after we stretched the ideal chromosome
bead_size_new = .500

# 1D array of possible genomic distances in beads
N_bead = 250
d = array(range(N_bead))

# Make arrays for the first column of each lambdas matrix
#     Zero out AA type interactions; this leaves only ideal chromosome interactions
#     If you divided gamma by a number to make the lambdas matrix, then multiply back by it
#vec59 = M59[0:N_bead,0]-M59[0,2499]
vec75cis = M75[0:0+N_bead,0]-M75[0,2499]
vec76cis = M76[0:0+N_bead,0]-M76[0,2499]
vec77cis = M77[0:0+N_bead,0]-M77[0,2499]
vec78cis = M78[0:0+N_bead,0]-M78[0,2499]
vec79cis = M79[0:0+N_bead,0]-M79[0,2499]
vec80cis = M80[0:0+N_bead,0]-M80[0,2499]
vec81cis = M81[0:0+N_bead,0]-M81[0,2499]
vec82cis = M82[0:0+N_bead,0]-M82[0,2499]
vec83cis = M83[0:0+N_bead,0]-M83[0,2499]
vec84cis = M84[0:0+N_bead,0]-M84[0,2499]
vec85cis = M85[0:0+N_bead,0]-M85[0,2499]

vec75trans = M75[2500:2500+N_bead,0]-M75[0,2499]
vec76trans = M76[2500:2500+N_bead,0]-M76[0,2499]
vec77trans = M77[2500:2500+N_bead,0]-M77[0,2499]
vec78trans = M78[2500:2500+N_bead,0]-M78[0,2499]
vec79trans = M79[2500:2500+N_bead,0]-M79[0,2499]
vec80trans = M80[2500:2500+N_bead,0]-M80[0,2499]
vec81trans = M81[2500:2500+N_bead,0]-M81[0,2499]
vec82trans = M82[2500:2500+N_bead,0]-M82[0,2499]
vec83trans = M83[2500:2500+N_bead,0]-M83[0,2499]
vec84trans = M84[2500:2500+N_bead,0]-M84[0,2499]
vec85trans = M85[2500:2500+N_bead,0]-M85[0,2499]

# Plot the lambdas slices. They should overlap.
'''
#plot(d*bead_size_new, vec59, label='sim 59 (cis)')
plot(d*bead_size_new, vec75, label='sim 75')
plot(d*bead_size_new, vec76, label='sim 76')
plot(d*bead_size_new, vec77, label='sim 77')
plot(d*bead_size_new, vec78, label='sim 78')
plot(d*bead_size_new, vec79, label='sim 79')
plot(d*bead_size_new, vec80, label='sim 80')
plot(d*bead_size_new, vec81, label='sim 81')
plot(d*bead_size_new, vec82, label='sim 82')
plot(d*bead_size_new, vec83, label='sim 83')
plot(d*bead_size_new, vec84, label='sim 84')
plot(d*bead_size_new, vec85, label='sim 85')
'''
plot(d*bead_size_new, vec75cis, label='sim 75')
title('75')
xlabel('genomic distance from diagonal in kb')
ylabel('cis gamma')
show()
plot(d*bead_size_new, vec76cis, label='sim 76')
title('76')
xlabel('genomic distance from diagonal in kb')
ylabel('cis gamma')
show()
plot(d*bead_size_new, vec77cis, label='sim 77')
title('77')
xlabel('genomic distance from diagonal in kb')
ylabel('cis gamma')
show()
plot(d*bead_size_new, vec78cis, label='sim 78')
title('78')
xlabel('genomic distance from diagonal in kb')
ylabel('cis gamma')
show()
plot(d*bead_size_new, vec79cis, label='sim 79')
title('79')
xlabel('genomic distance from diagonal in kb')
ylabel('cis gamma')
show()
plot(d*bead_size_new, vec80cis, label='sim 80')
title('80')
xlabel('genomic distance from diagonal in kb')
ylabel('cis gamma')
show()
plot(d*bead_size_new, vec81cis, label='sim 81')
title('81')
xlabel('genomic distance from diagonal in kb')
ylabel('cis gamma')
show()
plot(d*bead_size_new, vec82cis, label='sim 82')
title('82')
xlabel('genomic distance from diagonal in kb')
ylabel('cis gamma')
show()
plot(d*bead_size_new, vec83cis, label='sim 83')
title('83')
xlabel('genomic distance from diagonal in kb')
ylabel('cis gamma')
show()
plot(d*bead_size_new, vec84cis, label='sim 84')
title('84')
xlabel('genomic distance from diagonal in kb')
ylabel('cis gamma')
show()
plot(d*bead_size_new, vec85cis, label='sim 85')
title('85')
xlabel('genomic distance from diagonal in kb')
ylabel('cis gamma')
show()

plot(d*bead_size_new, vec75trans, label='sim 75')
title('75')
xlabel('genomic distance from diagonal in kb')
ylabel('trans gamma')
show()
plot(d*bead_size_new, vec76trans, label='sim 76')
title('76')
xlabel('genomic distance from diagonal in kb')
ylabel('trans gamma')
show()
plot(d*bead_size_new, vec77trans, label='sim 77')
title('77')
xlabel('genomic distance from diagonal in kb')
ylabel('trans gamma')
show()
plot(d*bead_size_new, vec78trans, label='sim 78')
title('78')
xlabel('genomic distance from diagonal in kb')
ylabel('trans gamma')
show()
plot(d*bead_size_new, vec79trans, label='sim 79')
title('79')
xlabel('genomic distance from diagonal in kb')
ylabel('trans gamma')
show()
plot(d*bead_size_new, vec80trans, label='sim 80')
title('80')
xlabel('genomic distance from diagonal in kb')
ylabel('trans gamma')
show()
plot(d*bead_size_new, vec81trans, label='sim 81')
title('81')
xlabel('genomic distance from diagonal in kb')
ylabel('trans gamma')
show()
plot(d*bead_size_new, vec82trans, label='sim 82')
title('82')
xlabel('genomic distance from diagonal in kb')
ylabel('trans gamma')
show()
plot(d*bead_size_new, vec83trans, label='sim 83')
title('83')
xlabel('genomic distance from diagonal in kb')
ylabel('trans gamma')
show()
plot(d*bead_size_new, vec84trans, label='sim 84')
title('84')
xlabel('genomic distance from diagonal in kb')
ylabel('trans gamma')
show()
plot(d*bead_size_new, vec85trans, label='sim 85')
title('85')
xlabel('genomic distance from diagonal in kb')
ylabel('trans gamma')
show()

#plot(d*120,-exp(-d/420)/12-d/300000, label = 'NuChroM gamma fit')
#axvline(x = 40*bead_size_new, color = 'black', label='genomic distance with correct contact frequency')
xlabel('genomic distance from diagonal in kb')
#xscale('log')
ylabel('gamma')
#yscale('log')
legend(loc="upper left", bbox_to_anchor=(1,1))
#xlim(0,5e4)
#ylim(-.75,.01)
show()