from numpy import zeros, array, savetxt, loadtxt, eye
from matplotlib.pyplot import imshow, show, colorbar, savefig, title

# User inputs
directory_number = input("directory number = ")
print('Available chromatin type sequences:')
print(' AAAA, AABA, ABAB, AABB, ABAB_different_size_1, ABAB_different_size_2, BABA_different_size, random1, random2')
pat_type_sequence = input("paternal chromatin type sequence = ") # AAAA, AABA, ABAB, AABB, ABAB_different_size_1, ABAB_different_size_2, BABA_different_size, random1, random2
mat_type_sequence = input("maternal chromatin type sequence = ")
print('ideal chromosome files available: MiChroM_gammas.txt, gammas_59.txt')
cis_ideal_chromosome_file = input('cis ideal chromosome file name: ')
trans_ideal_chromosome_file = input('trans ideal chromosome file name: ')
pairing_type_sequence_name = input("pairing type sequence = ") # TTTTT, TTLTT, NNNNN, TTNTT, NNLNN, TTL92TT, TTL100TT, TTL50TT
trans_IC_strength = 1.0 #float(input('trans_IC_strength = ')) # This number is multiplied by the trans IC before adding it to Lambda.
loop = input("loop? (True or False)")
link = input("link? (True or False)")
type_to_type_divisor = float(input('type to type divisor = ')) # Number by which to divide the ideal chromosome (or the whole lambdas matrix)

#============Chromatin=Types===============
seqPath = "../1_make_sequences/"#path to the sequences of chromatin type and pairing type
pat_type_sequence_path = seqPath + "chr_"+pat_type_sequence+"_2500_beads.txt"
seq_paternal_string = loadtxt(pat_type_sequence_path,str)#array of strings encoding chromatin types for the paternal sequence of beads
mat_type_sequence_path = seqPath + "chr_"+mat_type_sequence+"_2500_beads.txt"
seq_maternal_string = loadtxt(mat_type_sequence_path,str)#array of strings encoding chromatin types for the maternal sequence of beads
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
        seq_paternal[i] = 1
    if seq_maternal_string[i,1] == "A1":
        seq_maternal[i] = 0
    if seq_maternal_string[i,1] == "B1":
        seq_maternal[i] = 1

# An array of interaction strengths between different types of bead. It's the original from the MiChroM paper.
typeToType = array([[-0.268028,-0.262513], # AA,AB
[-0.262513,-0.342020]]) # BA,BB

typeToType /= type_to_type_divisor # Divide the strength of type-to-type interactions by a user-defined number.

#===============Lengthwise=Compaction===================

# gammas from files
cis_gammas = loadtxt(cis_ideal_chromosome_file)
def cis_gamma(d):
    output = cis_gammas[d]
    return output

trans_gammas = loadtxt(trans_ideal_chromosome_file)
def trans_gamma(d):
    output = trans_gammas[d]
    return output

kb50 = 100 #50kb converted to beads. 50kb is the genomic distance at which loose and tight pairing have the same probability. (1 bead = .5 kb)
loose_pairing_strength = trans_gamma(kb50)

#===========Pairing=Types======================
pairing_type_sequence_path = seqPath + 'chr_chr_'+pairing_type_sequence_name+'_2500_2500_beads.txt'
pairing_types_sequence = loadtxt(pairing_type_sequence_path,str)#array of strings encoding pairing types for corresponding beads on the separate chromosomes.

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
# Make the lambdas matrix from formulas. This method is not the most efficient, but it is arguably more human readable. Since this is definitely not the computational bottleneck, we take liberty.
delta_function = eye(3) # used to toggle which pairing types add to various indices

# cis paternal; i.e. top left
for i in range(N):
    for j in range(N):
        Lambda[i,j] += cis_gamma(abs(i-j))# ideal chromosome
        Lambda[i,j] += typeToType[seq_paternal[i],seq_paternal[j]]# chromatin type

# trans on top right
for i in range(N):
    for j in range(N):
        Lambda[i,j+N] += delta_function[1,pairing_types_matrix[i,j]] * loose_pairing_strength
        Lambda[i,j+N] += delta_function[2,pairing_types_matrix[i,j]] * trans_IC_strength * trans_gamma(abs(i-j))# tight pairing
        Lambda[i,j+N] += typeToType[seq_paternal[i],seq_maternal[j]]# chromatin type

# trans on bottom left
for i in range(N):
    for j in range(N):
        Lambda[i+N,j] += delta_function[1,pairing_types_matrix[i,j]] * loose_pairing_strength
        Lambda[i+N,j] += delta_function[2,pairing_types_matrix[i,j]] * trans_IC_strength * trans_gamma(abs(i-j))# tight pairing
        Lambda[i+N,j] += typeToType[seq_maternal[i],seq_paternal[j]]# chromatin type

# cis maternal; i.e. bottom right
for i in range(N):
    for j in range(N):
        Lambda[i+N,j+N] += cis_gamma(abs(i-j))# ideal chromosome
        Lambda[i+N,j+N] += typeToType[seq_maternal[i],seq_maternal[j]]# chromatin type

# Just in case self interactions are a problem, make them zero
for i in range(2*N):
    Lambda[i,i] = 0.0

#======================================
# Save and display the lambdas matrix.
savePath = "/Users/douglas/Documents/Features Transfer/store lambdas/"

savetxt(savePath + "lambdas"+directory_number + "_0.txt",Lambda[0:N,0:N],delimiter=',')# delimiter of ',' makes output into a csv file
savetxt(savePath + "lambdas"+directory_number + "_1.txt",Lambda[N:N+N,N:N+N],delimiter=',')
savetxt(savePath + "lambdas"+directory_number + ".txt",Lambda,delimiter=',')
imshow(Lambda,vmin=-.45/type_to_type_divisor,vmax =-.26/type_to_type_divisor)
title('simulation '+str(directory_number)+'   AA/'+str(type_to_type_divisor))
colorbar()
savefig(savePath+"lambdas"+directory_number+".png",dpi=300)
show()
