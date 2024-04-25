from numpy import zeros, array, savetxt, loadtxt, eye
from matplotlib.pyplot import imshow, show, colorbar, savefig, title
import argparse

# User inputs

parser = argparse.ArgumentParser()

parser.add_argument('directory_number',metavar='dir', type=str, help='identifying number for simulation')
parser.add_argument('pat_type_sequence',metavar='pat', type=str, help='paternal AB chromatin type sequence identifyer e.g., AAAA, ABAB')
parser.add_argument('mat_type_sequence',metavar='mat', type=str, help='maternal AB chromatin type sequence identifyer e.g., AAAA, ABAB')
parser.add_argument('cis_ideal_chromosome_file',metavar='cis_gamma', type=str, help='path to cndb trajectory of first molecule')
parser.add_argument('trans_ideal_chromosome_file',metavar='trans_gamma', type=str, help='path to cndb trajectory of second molecule')
parser.add_argument('pairing_type_sequence_name',metavar='pt', type=str, help='')
parser.add_argument('loop_strength',metavar='lst',type=float,help='interaction energy between bead pairs in the same loop or link')
parser.add_argument('loop_size',metavar='lsz',type=int,help='side length of a square region to which to add loop energies')
parser.add_argument('loop',metavar='cis_gamma', type=str, help='path to cndb trajectory of first molecule')
parser.add_argument('link',metavar='trans_gamma', type=str, help='path to cndb trajectory of second molecule')
parser.add_argument('type_to_type_divisor',metavar='tt_div', type=float, help='')

args = parser.parse_args()

directory_number = args.directory_number # file name for cndb trajectory of first molecule
pat_type_sequence = args.pat_type_sequence
mat_type_sequence = args.mat_type_sequence
cis_ideal_chromosome_file = args.cis_ideal_chromosome_file
trans_ideal_chromosome_file = args.trans_ideal_chromosome_file
pairing_type_sequence_name = args.pairing_type_sequence_name
loop_strength = args.loop_strength # loop_strength = -0.8264462879099161 * 2.0
M = args.loop_size # loop size in beads
loop = args.loop
link = args.link
type_to_type_divisor = args.type_to_type_divisor

# Paths
gammas_path = 'gamma_files/' # on local machine
#gammas_path = '/home/white.do/DiPierroLab_Douglas/2_make_lambdas/gamma_files/' # on discovery cluster

#path to the sequences of chromatin type and pairing type
seqPath = "/Users/douglas/Documents/DiPierroLab_Douglas/1_make_sequences/"# on local machine
#seqPath = "/home/white.do/DiPierroLab_Douglas/1_make_sequences/"# on discovery cluster

savePath = "/Users/douglas/Documents/Features_Transfer/store_lambdas/" # on local machine
#savePath = '/work/dipierrolab/douglas/lambdas/' # on discovery cluster

pat_type_sequence_path = seqPath + "chr_"+pat_type_sequence+"_2500_beads.txt"
mat_type_sequence_path = seqPath + "chr_"+mat_type_sequence+"_2500_beads.txt"
pairing_type_sequence_path = seqPath + 'chr_chr_'+pairing_type_sequence_name+'_2500_2500_beads.txt'


#============Chromatin=Types===============
seq_paternal_string = loadtxt(pat_type_sequence_path,str) #array of strings encoding chromatin types for the paternal sequence of beads
seq_maternal_string = loadtxt(mat_type_sequence_path,str) #array of strings encoding chromatin types for the maternal sequence of beads
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
[-0.262513,-0.342020]])

typeToType /= type_to_type_divisor # Divide the strength of type-to-type interactions by a user-defined number.

#===============Lengthwise=Compaction===================

# gammas from files
cis_gammas = loadtxt(gammas_path+cis_ideal_chromosome_file)
def cis_gamma(d):
    output = cis_gammas[d]
    return output

trans_gammas = loadtxt(gammas_path+trans_ideal_chromosome_file)
def trans_gamma(d):
    output = trans_gammas[d]
    return output

kb50 = 100 #50kb converted to beads. 50kb is the genomic distance at which loose and tight pairing have the same probability. (1 bead = .5 kb)
loose_pairing_strength = trans_gamma(kb50)

#===========Pairing=Types======================
pairing_types_sequence = loadtxt(pairing_type_sequence_path,str)#array of strings encoding pairing types for corresponding beads on the separate chromosomes.

pairing_types_matrix = zeros([N,N],int)# Will be made into a matrix of pairing types between loci. M[i,j] = 0 if locus i and locus j don't pair, 1 if they pair loosely, and 2 if they pair tightly.
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

Lambda = zeros([N+N,N+N])

# Add loops and links without using delta functions
#square loop
if loop == "True":
    for i in range(250,251+M):
        for j in range(750,751+M):
            Lambda[i,j] += loop_strength
            Lambda[j,i] += loop_strength

#square link
if link == "True":
    for i in range(1250,1251+M):
        for j in range(750,751+M):
            Lambda[N+i,j] += loop_strength
            Lambda[j,N+i] += loop_strength # the matrix needs to be symmetric otherwise Ailun's and my chromosome dynamics module will complain

#=======================================
# Make the lambdas matrix from formulas. This is inefficient, but arguably more human readable. Since this is not the computational bottleneck, we take liberty.
delta_function = eye(3) # toggles which pairing types add to various indices

# cis paternal; i.e. top left
for i in range(N):
    for j in range(N):
        Lambda[i,j] += cis_gamma(abs(i-j))# ideal chromosome
        Lambda[i,j] += typeToType[seq_paternal[i],seq_paternal[j]]# chromatin type

# trans on top right
for i in range(N):
    for j in range(N):
        Lambda[i,j+N] += delta_function[1,pairing_types_matrix[i,j]] * loose_pairing_strength
        Lambda[i,j+N] += delta_function[2,pairing_types_matrix[i,j]] * trans_gamma(abs(i-j))# tight pairing
        Lambda[i,j+N] += typeToType[seq_paternal[i],seq_maternal[j]]# chromatin type

# trans on bottom left
for i in range(N):
    for j in range(N):
        Lambda[i+N,j] += delta_function[1,pairing_types_matrix[i,j]] * loose_pairing_strength
        Lambda[i+N,j] += delta_function[2,pairing_types_matrix[i,j]] * trans_gamma(abs(i-j))# tight pairing
        Lambda[i+N,j] += typeToType[seq_maternal[i],seq_paternal[j]]# chromatin type

# cis maternal; i.e. bottom right
for i in range(N):
    for j in range(N):
        Lambda[i+N,j+N] += cis_gamma(abs(i-j))# ideal chromosome
        Lambda[i+N,j+N] += typeToType[seq_maternal[i],seq_maternal[j]]# chromatin type

# Just in case self interactions are a problem, make them zero
for i in range(2*N):
    Lambda[i,i] = 0.0

for i in range(2*N-1):
    if i !=2499:
        Lambda[i,i+1] = 0.0
        Lambda[i+1,i] = 0.0

#======================================
# Save and display the lambdas matrix.

savetxt(savePath + "lambdas"+directory_number + "_0.txt",Lambda[0:N,0:N],delimiter=',')# delimiter of ',' makes output into a csv file
savetxt(savePath + "lambdas"+directory_number + "_1.txt",Lambda[N:N+N,N:N+N],delimiter=',')
savetxt(savePath + "lambdas"+directory_number + ".txt",Lambda,delimiter=',')
imshow(Lambda,vmin=Lambda[0,2],vmax =Lambda[0,4999])
title('simulation '+str(directory_number)+'   AA/'+str(type_to_type_divisor))
colorbar()
savefig(savePath+"lambdas"+directory_number+".png",dpi=300)
show()
