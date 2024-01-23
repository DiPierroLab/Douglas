path = "/Users/douglas/Documents/DiPierroLab_Douglas/1_make_sequences/"
file = open(path+'chr_chr_TTLTT_small_T.txt',"w")

for i in range(1,6):
    for j in range(70):
        file.write("T\n")
    file.write('N\n')
for j in range(70):
    file.write("T\n")

for i in range(500):
    file.write("L\n")

for i in range(1,6):
    for j in range(70):
        file.write("T\n")
    file.write('N\n')
for j in range(70):
    file.write("T\n")
    
file.close()
