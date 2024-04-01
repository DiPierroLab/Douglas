import numpy as np
import matplotlib.pyplot as plt
'''
path = '/work/dipierrolab/douglas/final_Hi-C_maps/'

n = 175
phase_diagram = np.zeros((7,7))
for i in range(7):
    for j in range(7):
        matrix = np.loadtxt(path+'Hi-C_directory_'+str(n)+'.txt') # Hi-C map for simulation n.
        cis_contacts = np.sum(np.triu(matrix[0:2500,0:2500])+np.triu(matrix[2500:5000,2500:5000]))
        trans_contacts = np.sum(matrix[0:2500,2500:5000])
        phase_diagram[i,j] = trans_contacts/cis_contacts
        print(round((n-174)*100/49),' percent done')
        n += 1
'''
phase_diagram = np.loadtxt('phase_diagram.txt')

plt.imshow(phase_diagram, origin = 'lower')
plt.xlabel('B')
plt.ylabel('A')
plt.xticks(ticks = range(7), labels = np.linspace(0.5,3.5,7))
plt.yticks(ticks = range(7), labels = [.4,.5,.6,.7,.8,.9,1.0])
plt.title('trans contacts over cis contacts  gamma(d)=A*e^(-d/B)')
plt.colorbar()
plt.savefig('phase_diagram.png')
