from hicTools import *

path = '/work/dipierrolab/douglas/final_Hi-C_maps/' # path to Hi-C map .txt storage
path2 = '/home/white.do/DiPierroLab_Douglas/1_make_sequences/' # path to AB type sequence storage

typesPlist = ['AAAA','AAAA','AAAA','AAAA','ABAB','ABAB','random1','random2'] # list of sequence names to help reference the correct AB type sequence files
typesMlist = ['AAAA','AAAA','BABA','BABA','ABAB','ABAB','random1','random2']

i = 0 #keeps track of which sequence name to use
for directory_number in {1,2,8,9,10,11,12,13}: # Make directory numbers consistent with the sequence name lists above. Otherwise the output is faulty.
    filename = "Hi-C_directory_"+str(directory_number)+".txt"

    typesP = typesPlist[i]
    typesM = typesMlist[i]
    i += 1

    block22(path+filename, "Hi-C_directory"+str(directory_number)+"_block")

    PvsGenomic("Hi-C_directory"+str(directory_number)+"_block.txt", outputFileName = 'PvsGenomic_directory_'+str(directory_number))
    PAAvsGenomic("Hi-C_directory"+str(directory_number)+"_block.txt",path2+"chr_"+typesM+"_2500_beads.txt",path2+"chr_"+typesM+"_2500_beads.txt", outputFileName = 'PAAvsGenomic_directory_'+str(directory_number))
    PBBvsGenomic("Hi-C_directory"+str(directory_number)+"_block.txt",path2+"chr_"+typesM+"_2500_beads.txt",path2+"chr_"+typesM+"_2500_beads.txt", outputFileName = 'PBBvsGenomic_directory_'+str(directory_number))
    PABvsGenomic("Hi-C_directory"+str(directory_number)+"_block.txt",path2+"chr_"+typesM+"_2500_beads.txt",path2+"chr_"+typesM+"_2500_beads.txt", outputFileName = 'PABvsGenomic_directory_'+str(directory_number))
