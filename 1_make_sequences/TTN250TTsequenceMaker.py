# Make a sequence of TTTTTTLLLLTTTTTTT where the middle 100 lines are "L"
path = "/Users/douglas/Documents/DiPierroLab_Douglas/1_make_sequences/"
file = open(path+'chr_chr_TTN250TT_2500_2500_beads.txt',"w")

for i in range(1,1126):
    file.write("T\n")

for i in range(1126,1376):
    file.write("N\n")

for i in range(1376,2501):
    file.write("T\n")
    
file.close()
