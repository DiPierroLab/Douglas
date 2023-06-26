path = "/Users/douglas/Documents/DiPierroLab_Douglas/1_make_sequences/"
file = open(path+"chr_AABB_2500_beads.txt","w")

for i in range(1,1251):
    file.write(str(i)+" A1\n")
    
for i in range(1251,2501):
    file.write(str(i)+" B1\n")
    
file.close()