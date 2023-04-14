from numpy import zeros, array, savetxt, loadtxt, eye
from math import log
from matplotlib.pyplot import imshow, show, colorbar, savefig, title

# User inputs
directory_number = input("directory number = ")
pat_type_sequence = input("paternal type sequence = ")# AAAA, AABA, ABAB, or AABB
mat_type_sequence = input("maternal type sequence = ")
pairing_type_sequence_name = input("pairing type sequence = ")# TTTTT, TTLTT, NNNNN, TTNTT, NNLNN
trans_IC_strength = 1.0 #float(input('trans_IC_strength = ')) # This number is multiplied by the trans IC before adding it to Lambda.
loop = input("loop? (True or False)")
link = input("link? (True or False)")

#============Chromatin=Types===============
seqPath = "/Users/douglas/Documents/Features Transfer/store sequences/"#path to the sequences of chromatin type and pairing type
seq_paternal_string = loadtxt(seqPath + "chr_"+pat_type_sequence+"_2500_beads.txt",str)#array of strings encoding chromatin types for the paternal sequence of beads
seq_maternal_string = loadtxt(seqPath + "chr_"+mat_type_sequence+"_2500_beads.txt",str)#array of strings encoding chromatin types for the maternal sequence of beads
if seq_paternal_string.shape[0] == seq_maternal_string.shape[0]:
    N = seq_paternal_string.shape[0]

print("N = ", N)

# Change the chromatin types to numbers so that I can reference the typeToType table. After redefining, calling index i of e.g. seq_paternal will return its type T(i) as an integer.
seq_paternal = zeros(N, int)
seq_maternal = zeros(N, int)
for i in range(N):
    if seq_paternal_string[i,1] == "A1":
        seq_paternal[i] = 0
    if seq_paternal_string[i,1] == "B1":
        seq_paternal[i] = 2
    if seq_maternal_string[i,1] == "A1":
        seq_maternal[i] = 0
    if seq_maternal_string[i,1] == "B1":
        seq_maternal[i] = 2

# An array of interaction strengths between different types of bead.
typeToType = array([[-0.268028,-0.274604,-0.262513,-0.258880,-0.266760,-0.266760,-0.225646], #A1 = 0
                    [-0.274604,-0.299261,-0.286952,-0.281154,-0.301320,-0.301320,-0.245080], #A2 = 1
                    [-0.262513,-0.286952,-0.342020,-0.321726,-0.336630,-0.336630,-0.209919], #B1 = 2
                    [-0.258880,-0.281154,-0.321726,-0.330443,-0.329350,-0.329350,-0.282536], #B2 = 3
                    [-0.266760,-0.301320,-0.336630,-0.329350,-0.341230,-0.341230,-0.349490], #B3 = 4
                    [-0.266760,-0.301320,-0.336630,-0.329350,-0.341230,-0.341230,-0.349490], #B4 = 5
                    [-0.225646,-0.245080,-0.209919,-0.282536,-0.349490,-0.349490,-0.255994]])#NA = 6

#===============Lengthwise=Compaction===================
# cis ideal chromosome; this causes chromatin to have its characteristic power law decay.
def gamma_cis(d): # \gamma(d) = \frac{\gamma_1}{\log{(d)}} +\frac{\gamma_2}{d} +\frac{\gamma_3}{d^2}
    gamma1 = -0.030
    gamma2 = -0.351
    gamma3 = -3.727
    if d == 0:
        return 0.0 # Nearby beads "shouldn't" affect each other in this way. This doesn't really matter because OpenMM's CustomNonbondedForce doesn't add self-interaction forces between beads.
    elif d == 1:
        return 0.0
    else:
        return gamma1/log(d)+gamma2/d+gamma3/d**2

#===========Pairing=Types======================
pairing_types_sequence = loadtxt(seqPath + 'chr_chr_'+pairing_type_sequence_name+'_2500_2500_beads.txt',str)#array of strings encoding pairing types for corresponding beads on the separate chromosomes.

pairing_types_matrix = zeros([N,N],int)# Will be made into a matrix of pairing types between loci. M[i,j] = 0 if locus i and locus j don't pair, 1 if they pair loosely, and 2 if they pair tightly.pairing_types_path = '/Users/douglas/Documents/Features Transfer/pairing type matrices/store pairing type matrices/'
i = 0
Tmin = 0
Lmin = 0

# translate a 1D sequence of pairing types into 2D pairing type matrix
while i < N:
    if pairing_types_sequence[i] == 'T':
        stillT = True
        stillL = False
        stillN = False
    elif pairing_types_sequence[i] == 'L':
        stillT = False
        stillL = True
        stillN = False
    elif pairing_types_sequence[i] == 'N':
        stillT = False
        stillL = False
        stillN = True
    if stillT: # Keep making the block of 2's bigger.
        pairing_types_matrix[Tmin:i+1,Tmin:i+1] = 2
        Lmin = i+1
        Nmin = i+1
    if stillL: # Keep making the block of 1's bigger.
        pairing_types_matrix[Lmin:i+1,Lmin:i+1] = 1
        Tmin = i+1
        Nmin = i+1
    if stillN: # Keep making the block of 0's bigger by not changing the entrees.
        Lmin = i+1
        Tmin = i+1
    i += 1
imshow(pairing_types_matrix)
title("Pairing Types")
show()

print('')
print("Making matrix")

loose_pairing_strength =  -.32 + 0.268028 #added to  -0.268028, the AA interaction strength, this will end up as -.32, which I used in my original simulations.

# trans ideal chromosome; this is the model for tight pairing
def gamma_trans(d):# This is the same as gamma_cis except when d==0 or d==1.
    gamma1 = -0.030
    gamma2 = -0.351
    gamma3 = -3.727
    if d == 0:
        return -1.150530851226669#-1.6# I smoothed out the trans IC
    elif d == 1:
        return -1.150530851226669#-1.5# I smoothed out the trans IC
    else:
        return gamma1/log(d)+gamma2/d+gamma3/d**2

#==================Looping====================
loop_strength = -0.8264462879099161 * 2.0 #The first number -0.8264462879099161 is called the star wars number for historical reasons. 
M = 3 # loop size in beads

#=============================================
#=============================================
Lambda = zeros([N+N,N+N])

# Add loops and links without using delta functions
#square loop
if loop == "True":
    for i in range(250,251+M):
        for j in range(750,751+M):
            Lambda[i,j] += loop_strength

#square link
if link == "True":
    for i in range(1250,1251+M):
        for j in range(750,751+M):
            Lambda[N+i,j] += loop_strength
            Lambda[j,N+i] += loop_strength # the matrix needs to be symmetric otherwise Ailun's and my chromosome dynamics module will complain

#=======================================
# Make the lambdas matrix from formulas.
delta_function = eye(3) # used to toggle which pairing types add to various indices

# cis paternal; i.e. top left
for i in range(N):
    for j in range(N):
        Lambda[i,j] += gamma_cis(abs(i-j))# ideal chromosome
        Lambda[i,j] += typeToType[seq_paternal[i],seq_paternal[j]]# chromatin type

# trans on top right
for i in range(N):
    for j in range(N):
        Lambda[i,j+N] += delta_function[1,pairing_types_matrix[i,j]] * loose_pairing_strength
        Lambda[i,j+N] += delta_function[2,pairing_types_matrix[i,j]] * trans_IC_strength * gamma_trans(abs(i-j))# tight pairing
        Lambda[i,j+N] += typeToType[seq_paternal[i],seq_maternal[j]]# chromatin type


# trans on bottom left
for i in range(N):
    for j in range(N):
        Lambda[i+N,j] += delta_function[1,pairing_types_matrix[i,j]] * loose_pairing_strength
        Lambda[i+N,j] += delta_function[2,pairing_types_matrix[i,j]] * trans_IC_strength * gamma_trans(abs(i-j))# tight pairing
        Lambda[i+N,j] += typeToType[seq_maternal[i],seq_paternal[j]]# chromatin type

# cis maternal; i.e. bottom right
for i in range(N):
    for j in range(N):
        Lambda[i+N,j+N] += gamma_cis(abs(i-j))# ideal chromosome
        Lambda[i+N,j+N] += typeToType[seq_maternal[i],seq_maternal[j]]# chromatin type

#======================================
# Save and display the lambdas matrix.
savePath = "/Users/douglas/Documents/Features Transfer/store lambdas/"

savetxt(savePath + "lambdas"+directory_number + "_0.txt",Lambda[0:N,0:N],delimiter=',')# delimiter of ',' makes output into a csv file
savetxt(savePath + "lambdas"+directory_number + "_1.txt",Lambda[N:N+N,N:N+N],delimiter=',')
savetxt(savePath + "lambdas"+directory_number + ".txt",Lambda,delimiter=',')

imshow(Lambda,vmin=-.45,vmax =-.26)
title('directory_'+str(directory_number))
colorbar()
savefig(savePath+"lambdas"+directory_number+".png",dpi=300)
show()