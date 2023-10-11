# Make a sequence of TTTTTTLLLLTTTTTTT where the middle 100 lines are "L"
path = "/Users/douglas/Documents/DiPierroLab_Douglas/1_make_sequences/"
file = open(path+'chr_chr_TTL100TT_2500_2500_beads.txt',"w")

for i in range(1,1201):
    file.write("T\n")

for i in range(1201,1301):
    file.write("L\n")

for i in range(1301,2501):
    file.write("T\n")
    
file.close()
