# cp this .py file into the directory of the trajectory you want a frame from.
frame = 1998608 # the number of the frame before the crash

from OpenMiChroM.CndbTools import cndbTools
from numpy import savetxt

cndbTools = cndbTools()

traj_0 = cndbTools.load('traj_0.cndb')

print(traj_0) # Print the information of the cndb trajectory.

chr_0_xyz = cndbTools.xyz(frames=[frame,frame+1,1], beadSelection='all', XYZ=[0,1,2])

savetxt("traj_0_frame_"+str(frame)+'.txt',chr_0_xyz[0])#the [0] comes from the fact that the xyz array's single entry is an array of dimension 2.
