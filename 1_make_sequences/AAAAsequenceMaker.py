N = 1350 #number of beads in corresponding chromosome

path = "/Users/douglas/Documents/DiPierroLab_Douglas/1_make_sequences/"
file_name = "chr_AAAA_"+str(N)+"_beads"

file = open(path+file_name+".txt","w")

for i in range(1,N+1):#The +1's take care of indexing mismatches.
    file.write(str(i)+" A1\n")
    
file.close()