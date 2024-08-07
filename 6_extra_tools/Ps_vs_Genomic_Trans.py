from hicTools import *

path = '/work/dipierrolab/douglas/final_Hi-C_maps/' # path to Hi-C map .txt storage
path2 = '/home/white.do/DiPierroLab_Douglas/1_make_sequences/' # path to AB type sequence storage
path3 = '/work/dipierrolab/douglas/PvsGenomic/' # path in which to store final P vs d txt files

typesPlist = [f'ABAB_random_offset_{i}' for i in range(1,11)]
typesMlist = [f'ABAB_random_offset_{i}' for i in range(1,11)]

i = 0 #keeps track of which sequence name to use
for directory_number in range(379,389): # Make directory numbers consistent with the sequence name lists above. Otherwise the output is faulty.
    filename = "Hi-C_directory_"+str(directory_number)+".txt"

    typesP = typesPlist[i]
    typesM = typesMlist[i]
    i += 1

    block12(path+filename, "/scratch/white.do/Pairing/Hi-C_directory"+str(directory_number)+"_block")

    PvsGenomic("/scratch/white.do/Pairing/Hi-C_directory"+str(directory_number)+"_block.txt", outputFileName = path3+'transPvsGenomic_directory_'+str(directory_number))
    PAAvsGenomic("/scratch/white.do/Pairing/Hi-C_directory"+str(directory_number)+"_block.txt",path2+"chr_"+typesM+"_2500_beads.txt",path2+"chr_"+typesM+"_2500_beads.txt", outputFileName = path3+'transPAAvsGenomic_directory_'+str(directory_number))
    PBBvsGenomic("/scratch/white.do/Pairing/Hi-C_directory"+str(directory_number)+"_block.txt",path2+"chr_"+typesM+"_2500_beads.txt",path2+"chr_"+typesM+"_2500_beads.txt", outputFileName = path3+'transPBBvsGenomic_directory_'+str(directory_number))
    PABvsGenomic("/scratch/white.do/Pairing/Hi-C_directory"+str(directory_number)+"_block.txt",path2+"chr_"+typesM+"_2500_beads.txt",path2+"chr_"+typesM+"_2500_beads.txt", outputFileName = path3+'transPABvsGenomic_directory_'+str(directory_number))
