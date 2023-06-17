path = "/Users/douglas/Documents/DiPierroLab_Douglas/1_make_sequences/"
file = open(path+"chr_BABA_different_size_2500_beads.txt","w")

for i in range(1,616):# range(1,626) makes blocks the same size
    file.write(str(i)+" B1\n")

for j in range(616,1231):# range(626,1251) makes blocks the same size
    file.write(str(j)+" A1\n")

for i in range(1231,1856):# range(1251,1876) makes blocks the same size
    file.write(str(i)+" B1\n")

for j in range(1856,2501):# range(1876,2501) makes blocks the same size
    file.write(str(j)+" A1\n")
    
file.close()
