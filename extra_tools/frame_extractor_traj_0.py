block_number = 1#block number of the desired structure

from OpenMiChroM.CndbTools import cndbTools
from numpy import savetxt

cndbTools = cndbTools()

traj_0 = cndbTools.load('./traj_0.cndb')

xyz_0 = cndbTools.xyz(frames=[block_number,block_number+1,1], beadSelection='all', XYZ=[0,1,2])

file0 = open('traj_0_block_'+str(block_number)+'.xyz','w')
file0.write('2500\n')
file0.write('maternal chromosome\n')
for i in range(2500):
    file0.write('C '+str(xyz_0[0,i,0])+' '+str(xyz_0[0,i,1])+' '+str(xyz_0[0,i,2])+'\n')
file0.close()

savetxt('traj_0_block_'+str(block_number)+'.txt',xyz_0[0])
