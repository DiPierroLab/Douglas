# Make a sequence of TTTTTTLLLLTTTTTTT where the middle 100 lines are "L"
path = "/Users/douglas/Documents/DiPierroLab_Douglas/1_make_sequences/"
file = open(path+'chr_chr_TTL92TT_2500_2500_beads.txt',"w")

for i in range(1,1205):
    file.write("T\n")

for i in range(1205,1297):
    file.write("L\n")

for i in range(1297,2501):
    file.write("T\n")
    
file.close()
