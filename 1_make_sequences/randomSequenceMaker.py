path = "/Users/douglas/Documents/Features Transfer/sequences/store sequences/"
file = open(path+"chr_random1_2500_beads.txt","w")

for i in range(1,626):
    file.write(str(i)+" A1\n")
    
for j in range(626,1251):
    file.write(str(j)+" B1\n")
    
for i in range(1251,1876):
    file.write(str(i)+" A1\n")
    
for j in range(1876,2501):
    file.write(str(j)+" B1\n")
    
file.close()
