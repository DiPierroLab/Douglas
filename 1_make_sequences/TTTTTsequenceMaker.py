path = "/Users/douglas/Documents/DiPierroLab_Douglas/1_make_sequences/"
file = open(path+'chr_chr_TTTTT_2500_2500_beads.txt',"w")

for i in range(1,2501):
    file.write("T\n")
    
file.close()
