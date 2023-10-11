path = "/Users/douglas/Documents/DiPierroLab_Douglas/1_make_sequences/"
file = open(path+'chr_chr_TTLTT_2500_2500_beads.txt',"w")

for i in range(1,1001):
    file.write("T\n")

for i in range(1001,1501):
    file.write("L\n")

for i in range(1501,2501):
    file.write("T\n")
    
file.close()
