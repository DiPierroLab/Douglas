path = "/Users/douglas/Documents/DiPierroLab_Douglas/1_make_sequences/"
file = open(path+"chr_AABAA_2500_beads.txt","w")

for i in range(1,1001):
    file.write(str(i)+" A1\n")
    
for j in range(1001,1501):
    file.write(str(j)+" B1\n")
    
for i in range(1501,2501):
    file.write(str(i)+" A1\n")
    
file.close()
