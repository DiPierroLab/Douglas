import numpy 
import matplotlib.pyplot as plt
import matplotlib as mpl

path = "/work/dipierrolab/douglas/final_Hi-C_maps/"
for i in {85}:
    HiC_Matrices = []
    number_of_matrices = 0
    for j in range(1,9):#part
        number_of_matrices += 1
        print("loading Hi-C_directory_"+str(i)+"_part_"+str(j)+".txt")
        HiC_Matrices.append(numpy.loadtxt("//scratch//white.do//Pairing//directory_"+str(i)+"//part_"+str(j)+"//Hi-C_multi.txt"))
    HiC_Total = sum(HiC_Matrices)/number_of_matrices
    numpy.savetxt(path+"Hi-C_directory_"+str(i)+".txt",HiC_Total)
    plt.matshow(HiC_Total, norm=mpl.colors.LogNorm(vmin=0.00003, vmax=1.0),cmap="Reds")
    plt.title('simulation_'+str(i))
    plt.colorbar()
    plt.savefig(path+"Hi-C_directory_"+str(i)+".png")
