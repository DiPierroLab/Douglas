import numpy as np
import matplotlib.pyplot as plt

path = '/work/dipierrolab/douglas/final_Hi-C_maps/'

n = 175
phase_diagram = np.zeros((13,13))
'''
# Populate bottom left block of matrix with the order parameter trans_contacts/cis_contacts
for i in range(7):
    for j in range(7):
        matrix = np.loadtxt(path+'Hi-C_directory_'+str(n)+'.txt') # Hi-C map for simulation n.
        cis_contacts = np.sum(np.triu(matrix[0:2500,0:2500])+np.triu(matrix[2500:5000,2500:5000]))
        trans_contacts = np.sum(matrix[0:2500,2500:5000])
        phase_diagram[i,j] = trans_contacts/cis_contacts
        print(round((n-174)*100/133),' percent done')
        n += 1
n += 1 # because sim 224 was unrelated

# Populate top left block of matrix with the order parameter trans_contacts/cis_contacts
for i in range(7,13):
    for j in range(7):
        matrix = np.loadtxt(path+'Hi-C_directory_'+str(n)+'.txt') # Hi-C map for simulation n.
        cis_contacts = np.sum(np.triu(matrix[0:2500,0:2500])+np.triu(matrix[2500:5000,2500:5000]))
        trans_contacts = np.sum(matrix[0:2500,2500:5000])
        phase_diagram[i,j] = trans_contacts/cis_contacts
        print(round((n-175)*100/133),' percent done')
        n += 1

# Populate bottom right block of matrix with the order parameter trans_contacts/cis_contacts
for i in range(7):
    for j in range(7,13):
        matrix = np.loadtxt(path+'Hi-C_directory_'+str(n)+'.txt') # Hi-C map for simulation n.
        cis_contacts = np.sum(np.triu(matrix[0:2500,0:2500])+np.triu(matrix[2500:5000,2500:5000]))
        trans_contacts = np.sum(matrix[0:2500,2500:5000])
        phase_diagram[i,j] = trans_contacts/cis_contacts
        print(round((n-175)*100/133),' percent done')
        n += 1
'''
#np.savetxt('phase_diagram.txt',phase_diagram)
phase_diagram = np.loadtxt('phase_diagram.txt')

plt.imshow(phase_diagram, origin = 'lower')
plt.xlabel('B')
plt.ylabel('A')
plt.xticks(ticks = range(13), labels = np.linspace(0.5,6.5,13))
plt.yticks(ticks = range(13), labels = [0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6])
plt.title('trans contacts over cis contacts  gamma(d)=A*e^(-d/B)')
plt.colorbar()
plt.savefig('phase_diagram.png')
