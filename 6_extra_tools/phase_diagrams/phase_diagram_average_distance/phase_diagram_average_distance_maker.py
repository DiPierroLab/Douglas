import numpy as np
import matplotlib.pyplot as plt

path = '/scratch/white.do/Pairing/directory_'

n = 175
phase_diagram = np.zeros((13,13))

# Populate bottom left block of matrix with the order parameter for pairing, which is average distance between corresponding beads
for i in range(7):
    for j in range(7):
        average_distance = np.loadtxt(path+str(n)+'/part_1/average.txt') # Average distance between corresponding beads in simulation n
        phase_diagram[i,j] = average_distance
        print(round((n-174)*100/169),' percent done')
        n += 1
n += 1 # because sim 224 was unrelated

# Populate top left block of matrix with the order parameter for pairing, which is average distance between corresponding beads
for i in range(7,13):
    for j in range(7):
        average_distance = np.loadtxt(path+str(n)+'/part_1/average.txt') # Average distance between corresponding beads in simulation n
        phase_diagram[i,j] = average_distance
        print(round((n-175)*100/169),' percent done')
        n += 1

# Populate bottom right block of matrix with the order parameter for pairing, which is average distance between corresponding beads
for i in range(7):
    for j in range(7,13):
        average_distance = np.loadtxt(path+str(n)+'/part_1/average.txt') # Average distance between corresponding beads in simulation n
        phase_diagram[i,j] = average_distance
        print(round((n-175)*100/169),' percent done')
        n += 1

# Populate top right block of matrix with the order parameter for pairing, which is average distance between corresponding beads
for i in range(7,13):
    for j in range(7,13):
        average_distance = np.loadtxt(path+str(n)+'/part_1/average.txt') # Average distance between corresponding beads in simulation n
        phase_diagram[i,j] = average_distance
        print(round((n-175)*100/169),' percent done')
        n += 1

np.savetxt('phase_diagram_average_distance.txt',phase_diagram)
#phase_diagram = np.loadtxt('phase_diagram_average_distance.txt')

# Plot the phase diagram
fig, ax = plt.subplots()
im = ax.imshow(phase_diagram,origin='lower')

A = [0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5]
B = [0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6]

# We want to show all ticks...
ax.set_xticks(np.arange(len(A)))
ax.set_yticks(np.arange(len(B)))
# ... and label them with the respective list entries
ax.set_xticklabels(A)
ax.set_yticklabels(B)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(B)):
    for j in range(len(A)):
        text = ax.text(j, i, round(phase_diagram[i, j],1),
                       ha="center", va="center", color="w",size='small')

plt.xlabel('B')
plt.ylabel('A')
plt.title('average_distance_between_corresponding_beads_in_trans  gamma(d)=A*e^(-d/B)')
plt.colorbar(im)
plt.savefig('phase_diagram_average_distance.png')
plt.show()
