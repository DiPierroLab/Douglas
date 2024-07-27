from numpy import zeros, array, savetxt, loadtxt, eye, exp
from matplotlib.pyplot import imshow, show, colorbar, savefig, title
import argparse

# User inputs
parser = argparse.ArgumentParser()

parser.add_argument('directory_number',metavar='dir', type=str, help='identifying number for simulation')

parser.add_argument('pat_type_sequence',metavar='pat', type=str, help='paternal AB chromatin type sequence identifyer e.g., AAAA, ABAB')
parser.add_argument('mat_type_sequence',metavar='mat', type=str, help='maternal AB chromatin type sequence identifyer e.g., AAAA, ABAB')
parser.add_argument('AA',metavar='AA', type=float, help='AA interaction strength original_AA/2=-0.134)')
parser.add_argument('BB',metavar='BB', type=float, help='BB interaction strength original_BB/2=-0.171)')

# gamma(d)= -C * exp(-d/D) 
parser.add_argument('pairing_type_sequence_name',metavar='pt', type=str, help='')
parser.add_argument('C_cis',metavar='C_cis', type=float, help='energy scale for ideal chromosome gamma_cis(d)= -C_cis * exp(-d/D_cis) ')
parser.add_argument('D_cis',metavar='D_cis', type=float, help='characteristic decay genomic distance for ideal chromosome gamma_cis(d)= -C_cis * exp(-d/D_cis) ')
parser.add_argument('C_trans',metavar='C_trans', type=float, help='energy scale for trans ideal chromosome pairing gamma_trans(d)= -C_trans * exp(-d/D_trans) ')
parser.add_argument('D_trans',metavar='D_trans', type=float, help='characteristic decay genomic distance for trans ideal chromosome pairing gamma_trans(d)= -C_trans * exp(-d/D_trans) ')
parser.add_argument('Loose_pairing_dist', type=int, help='Genomic distance (in kb) at which loose pairing and tight pairing have the same energy')

parser.add_argument('loop_strength',metavar='lst',type=float,help='interaction energy between bead pairs in the same loop or link')
parser.add_argument('loop_size',metavar='lsz',type=int,help='side length of a square region to which to add loop energies')
parser.add_argument('chr0_loop',metavar='chr0_loop', type=str, help='path to cndb trajectory of first molecule')
parser.add_argument('chr1_loop',metavar='chr1_loop', type=str, help='path to cndb trajectory of first molecule')
parser.add_argument('chr0_chr1_loops',metavar='chr0_chr1_loops', type=str, help='path to cndb trajectory of first molecule')
parser.add_argument('link',metavar='link', type=str, help='path to cndb trajectory of second molecule')

# parse args
args = parser.parse_args()

# assign variables from argparse
directory_number = args.directory_number # file name for cndb trajectory of first molecule

pat_type_sequence = args.pat_type_sequence
mat_type_sequence = args.mat_type_sequence
AA = args.AA
AB = AA # Set these to the same value for simplicity. This is ok because they were about the same anyways in the MiChroM paper.
BB = args.BB

pairing_type_sequence_name = args.pairing_type_sequence_name
C_cis = args.C_cis
D_cis = args.D_cis
C_trans = args.C_trans
D_trans = args.D_trans
Loose_pairing_dist = args.Loose_pairing_dist

loop_strength = args.loop_strength # loop_strength = -0.8264462879099161 * 2.0
M = args.loop_size # loop size in beads
chr0_loop = args.chr0_loop
chr1_loop = args.chr1_loop
chr0_chr1_loops = args.chr0_chr1_loops
link = args.link

# Paths

#path to the sequences of chromatin types and pairing types
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
typeToType = array([[AA,AB], # AA,AB
                    [AB,BB]])

#===============Lengthwise=Compaction===================

# gammas from files
def cis_gamma(d):
    output = -C_cis * exp(-d/D_cis)
    return output

def trans_gamma(d):
    output = -C_trans * exp(-d/D_trans)
    return output

Loose_pairing_beads = 2*Loose_pairing_dist #Loose_pairing_dist (in kb) converted to beads.
loose_pairing_strength = cis_gamma(Loose_pairing_beads)
print('loose_pairing_strength =',loose_pairing_strength)

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

# [   0.,  417.,  833., 1250., 1667., 2083., 2500.]
# [2500., 2917., 3333., 3750., 4167., 4583., 5000.]

# Last four boolean input parameters decide whether
# 1 there is a loop in chromosome 0
# 2 there is a loop in chromosome 1 in a different place
# 3 there is a loop in chromosome 0 and in the analogous place in chromosome 1
# 4 there is a link between chromosomes 0 and 1
# All four of these will be in different places in the Hi-C map.


#square loop on paternal chromosome
if chr0_loop == 'True':
    for i in range(417,417+M+1):
        for j in range(833,833+M+1):
            Lambda[i,j] += loop_strength
            Lambda[j,i] += loop_strength

#square loop on maternal chromosome
if chr1_loop == 'True':
    for i in range(3333,3333+M+1):
        for j in range(3750,3750+M+1):
            Lambda[i,j] += loop_strength
            Lambda[j,i] += loop_strength
            
#two square loops
if chr0_chr1_loops == 'True':
    for i in range(1250,1250+M+1):
        for j in range(1667,1667+M+1):
            Lambda[i,j] += loop_strength
            Lambda[j,i] += loop_strength
    for i in range(3750,3750+M+1):
        for j in range(4167,4167+M+1):
            Lambda[i,j] += loop_strength
            Lambda[j,i] += loop_strength

#square link between maternal and paternal chromosomes
if link == 'True':
    for i in range(1667,1667+M+1):
        for j in range(2083,2083+M+1):
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
title('simulation '+str(directory_number))
colorbar()
savefig(savePath+"lambdas"+directory_number+".png",dpi=300)
show()
