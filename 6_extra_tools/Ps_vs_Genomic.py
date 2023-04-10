from hicTools import *

path = "/work/dipierrolab/secret/final_Hi-C_maps/"
path2 = "/work/dipierrolab/secret/lambdas/"
directory_number = 69
filename = "Hi-C_directory_"+str(directory_number)+".txt"
typesP = "AAAA"
typesM = "ABAB"

block22(path+filename, "Hi-C_directory"+str(directory_number)+"_block")

PvsGenomic("Hi-C_directory"+str(directory_number)+"_block.txt")
PAAvsGenomic("Hi-C_directory"+str(directory_number)+"_block.txt",path2+"chr_"+typesM+"_2500_beads.txt",path2+"chr_"+typesM+"_2500_beads.txt")
PBBvsGenomic("Hi-C_directory"+str(directory_number)+"_block.txt",path2+"chr_"+typesM+"_2500_beads.txt",path2+"chr_"+typesM+"_2500_beads.txt")
PABvsGenomic("Hi-C_directory"+str(directory_number)+"_block.txt",path2+"chr_"+typesM+"_2500_beads.txt",path2+"chr_"+typesM+"_2500_beads.txt")
