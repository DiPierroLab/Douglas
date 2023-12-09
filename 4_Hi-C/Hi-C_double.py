import matplotlib.pyplot as plt
import matplotlib as mpl
import sys
sys.path.append('/home/white.do/DiPierroLab_Douglas/4_Hi-C')
from CndbToolsDouglas import cndbTools
import numpy
import datetime
now = datetime.datetime.now()
print("Start Hi-C: ")
print(str(now))

filename = "Hi-C_multi"

def cndb_to_txt_block(string1, string2):# e.g.  r'./traj_0.cndb'
    tool = cndbTools()
    tool.load(string1,string2)
    frameIncrement = 1 # set to 1 if you want all frames
    first = 10000
    last = None # choose None to include all
    xyzs1 = tool.xyz1(frames=[first,last,frameIncrement],beadSelection='all',XYZ=[0,1,2])
    xyzs2 = tool.xyz2(frames=[first,last,frameIncrement],beadSelection='all',XYZ=[0,1,2])
    # rc MiChroM 3.22 NuChroM 1.79 width parameter for the sigmoid f
    # mu MiChroM 1.78 NuChroM 3.43 cutoff parameter for the sigmoid f
    output_matrix = tool.traj2HiC12(xyzs1, xyzs2, mu=3.22, rc=1.78) # Hi-C map in dense matrix form
    return output_matrix

def cndb_to_txt(*argv,filename = "super_file_name"): # e.g.  r'./traj_0.cndb'
    from numpy import zeros, array, savetxt
    from matplotlib.pyplot import matshow, colorbar, savefig
    import matplotlib as mpl
    N_list = []
    block_list = []
    for traj_i in argv:
        block_list_list = []
        for traj_j in argv:
            block = cndb_to_txt_block(traj_i,traj_j)
            block_list_list.append(block)
        N_list.append(block.shape[0])
        block_list.append(block_list_list)
    N_total = 0
    for N in N_list:
        N_total += N
    output_matrix = zeros((N_total,N_total))
    i_counter = 0
    i_index = 0
    for i in N_list:
        j_counter = 0
        j_index = 0
        for j in N_list:
            output_matrix[i_index:i_index+i,j_index:j_index+j] = array(block_list[i_counter][j_counter])
            j_counter += 1
            j_index += j
        i_counter += 1
        i_index += i
    savetxt(filename+".txt",output_matrix)
    matshow(output_matrix, norm = mpl.colors.LogNorm(vmin = .001, vmax = .1),cmap="Reds")
    colorbar()
    savefig(filename+".png")
    return output_matrix

cndb_to_txt(r'./traj_0.cndb',r'./traj_1.cndb',filename=filename)#,r'./traj_2.cndb',r'./traj_3.cndb',r'./traj_4.cndb',r'./traj_5.cndb',filename = filename)

now = datetime.datetime.now()
print("Finish Hi-C: ")
print(str(now))
