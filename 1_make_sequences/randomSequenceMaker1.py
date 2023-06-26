from random import random

path = "/Users/douglas/Documents/DiPierroLab_Douglas/1_make_sequences/"
file = open(path+"chr_random1_2500_beads.txt","w")

state = True #True when the next locus will be A; false when the next locus will be B.
p = 7/2500 #Probability of transitioning to the opposite state A->B or B->A at a given step.
for i in range(1,2501):
    r = random()
    if r <= p:
        state = not(state)
    if state == True:
        file.write(str(i)+" A1\n")
    else:
        file.write(str(i)+" B1\n")
    
file.close()
