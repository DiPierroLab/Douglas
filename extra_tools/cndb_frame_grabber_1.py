# cp this .py file into the directory of the trajectory you want a frame from.
frame = 1998608 # the number of the frame before the crash

from OpenMiChroM.CndbTools import cndbTools
from numpy import savetxt

cndbTools = cndbTools()

traj_1 = cndbTools.load('traj_1.cndb')

print(traj_1) # Print the information of the cndb trajectory.

chr_1_xyz = cndbTools.xyz(frames=[frame,frame+1,1], beadSelection='all', XYZ=[0,1,2])

savetxt("traj_1_frame_"+str(frame)+'.txt',chr_1_xyz[0])#the [0] comes from the fact that the xyz array's single entry is an array of dimension 2.
