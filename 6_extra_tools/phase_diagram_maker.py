import numpy as np
import matplotlib.pyplot as plt

path = '/work/dipierrolab/douglas/final_Hi-C_maps/'
'''
n = 175
phase_diagram = np.zeros((13,13))

# Populate bottom left block of matrix with the order parameter trans_contacts/cis_contacts
for i in range(7):
    for j in range(7):
        matrix = np.loadtxt(path+'Hi-C_directory_'+str(n)+'.txt') # Hi-C map for simulation n.
        cis_contacts = np.sum(np.triu(matrix[0:2500,0:2500])+np.triu(matrix[2500:5000,2500:5000]))
        trans_contacts = np.sum(matrix[0:2500,2500:5000])
        phase_diagram[i,j] = trans_contacts/cis_contacts
        print(round((n-174)*100/182),' percent done')
        n += 1
n += 1 # because sim 224 was unrelated

# Populate top left block of matrix with the order parameter trans_contacts/cis_contacts
for i in range(7,13):
    for j in range(7):
        matrix = np.loadtxt(path+'Hi-C_directory_'+str(n)+'.txt') # Hi-C map for simulation n.
        cis_contacts = np.sum(np.triu(matrix[0:2500,0:2500])+np.triu(matrix[2500:5000,2500:5000]))
        trans_contacts = np.sum(matrix[0:2500,2500:5000])
        phase_diagram[i,j] = trans_contacts/cis_contacts
        print(round((n-175)*100/182),' percent done')
        n += 1

# Populate bottom right block of matrix with the order parameter trans_contacts/cis_contacts
for i in range(7):
    for j in range(7,13):
        matrix = np.loadtxt(path+'Hi-C_directory_'+str(n)+'.txt') # Hi-C map for simulation n.
        cis_contacts = np.sum(np.triu(matrix[0:2500,0:2500])+np.triu(matrix[2500:5000,2500:5000]))
        trans_contacts = np.sum(matrix[0:2500,2500:5000])
        phase_diagram[i,j] = trans_contacts/cis_contacts
        print(round((n-175)*100/182),' percent done')
        n += 1

# Populate top right block of matrix with the order parameter trans_contacts/cis_contacts
for i in range(7,13):
    for j in range(7,13):
        matrix = np.loadtxt(path+'Hi-C_directory_'+str(n)+'.txt') # Hi-C map for simulation n.
        cis_contacts = np.sum(np.triu(matrix[0:2500,0:2500])+np.triu(matrix[2500:5000,2500:5000]))
        trans_contacts = np.sum(matrix[0:2500,2500:5000])
        phase_diagram[i,j] = trans_contacts/cis_contacts
        print(round((n-175)*100/182),' percent done')
        n += 1

np.savetxt('phase_diagram.txt',phase_diagram)
'''
phase_diagram = np.loadtxt('phase_diagram.txt')

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

ax.set_title("phase_diagram of local A (in tons/year)")
plt.xlabel('B')
plt.ylabel('A')
plt.title('trans contacts over cis contacts  gamma(d)=A*e^(-d/B)')
plt.colorbar(im)
plt.savefig('phase_diagram.png')
plt.show()
