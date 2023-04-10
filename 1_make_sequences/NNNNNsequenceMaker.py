path = "/Users/douglas/Documents/Features Transfer/sequences/store sequences/"
file = open(path+'chr_chr_NNNNN_2500_2500_beads.txt',"w")

for i in range(1,2501):
    file.write("N\n")
    
file.close()
