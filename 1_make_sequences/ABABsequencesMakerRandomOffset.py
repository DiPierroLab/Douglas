# I make 10 sequences of the form AAA...AAABBB...BBBAAA...AAABBB...BBB with randomly sized regions of the same type.

from random import randrange

path = "/Users/douglas/Documents/DiPierroLab_Douglas/1_make_sequences/"

for n in range(1,11):
    file = open(path+f"chr_ABAB_random_offset_{n}_2500_beads.txt","w")
    
    n1 = randrange(-200,201) # random integer between -100 and 100 inclusive
    n2 = randrange(-200,201) # another random integer between -100 and 100 inclusive
    n3 = randrange(-200,201) # another random integer between -100 and 100 inclusive

    for i in range(1,626+n1):
        file.write(str(i)+" A1\n")

    for j in range(626+n1,1251+n2):
        file.write(str(j)+" B1\n")


    for i in range(1251+n2,1876+n3):
        file.write(str(i)+" A1\n")
        
    for j in range(1876+n3,2501):
        file.write(str(j)+" B1\n")
        
    file.close()
