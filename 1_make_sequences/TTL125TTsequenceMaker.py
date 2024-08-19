# Make a sequence of TTTTTTLLLLTTTTTTT where the middle 100 lines are "L"
path = "/Users/douglas/Documents/DiPierroLab_Douglas/1_make_sequences/"
file = open(path+'chr_chr_TTL125TT_2500_2500_beads.txt',"w")

for i in range(1,1189):
    file.write("T\n")

for i in range(1189,1314):
    file.write("L\n")

for i in range(1314,2501):
    file.write("T\n")
    
file.close()
