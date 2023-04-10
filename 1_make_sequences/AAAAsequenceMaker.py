N = 2500 #number of beads in corresponding chromosome

path = "/Users/douglas/Documents/Features Transfer/sequences/store sequences/"
file_name = "chr_AAAA_"+str(N)+"_beads"

file = open(path+file_name+".txt","w")

for i in range(1,N+1):#The +1's take care of indexing mismatches.
    file.write(str(i)+" A1\n")
    
file.close()