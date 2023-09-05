path = "/Users/douglas/Documents/DiPierroLab_Douglas/1_make_sequences/"
file = open(path+"chr_AABA_2500_beads.txt","w")

for i in range(1,626):
    file.write(str(i)+" A1\n")

for j in range(626,1251):
    file.write(str(j)+" A1\n")

for i in range(1251,1876):
    file.write(str(i)+" B1\n")

for j in range(1876,2501):
    file.write(str(j)+" A1\n")

file.close()