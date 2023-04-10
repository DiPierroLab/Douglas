block_number = 1#block number of the desired structure

from OpenMiChroM.CndbTools import cndbTools
from numpy import savetxt

cndbTools = cndbTools()

traj_1 = cndbTools.load('./traj_1.cndb')

xyz_1 = cndbTools.xyz(frames=[block_number,block_number+1,1], beadSelection='all', XYZ=[0,1,2])

file1 = open('traj_1_block_'+str(block_number)+'.xyz','w')
file1.write('2500\n')
file1.write('maternal chromosome\n')
for i in range(2500):
    file1.write('C '+str(xyz_1[0,i,0])+' '+str(xyz_1[0,i,1])+' '+str(xyz_1[0,i,2])+'\n')
file1.close()

savetxt('traj_1_block_'+str(block_number)+'.txt',xyz_1[0])
