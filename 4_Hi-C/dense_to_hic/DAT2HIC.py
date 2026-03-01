import numpy  as np
import scipy  as sc
import sys
import subprocess
from   scipy     import sparse

'''
run with arguments 
$1 : Chr number
$3 : Resolution 
$2 : .dense file
$3 : juicer tools executable
'''

c = int(sys.argv[1])
RES = int(sys.argv[2])
d = str(sys.argv[3])
juicer = str(sys.argv[4])


# [ Initializing variables ]

H  = []
C1 = []
C2 = []
chro = [c,c]

MAX_READ = 1


dense = np.loadtxt(d)

dense = np.int64(dense*10000000)


sparse = sc.sparse.coo_matrix(dense)

for i in range(len(sparse.row)):
    H.append(['0', chro[0], (sparse.row[i] + 1) * RES, '1', '0', chro[1], (sparse.col[i] + 1) * RES, '0',
                  sparse.data[i]])

    C1.append(chro[0])
    C2.append(chro[1])

Hs = open('preHIC.txt', 'w+')

for i in np.lexsort((C1, C2)):
    Hs.write(' '.join([str(elem) for elem in H[i]]))
    Hs.write('\n')

Hs.close()

print("Writing file.size\n")

size = open('chr'+str(chro[0])+'.size', 'w+')

size.write(str(chro[0]) + '    ' + str(len(dense[0]) * RES)+ '\n')
size.close()


print("gziping file...\n")
subprocess.run(['gzip', 'preHIC.txt'])

print("creating .HIC...\n")
subprocess.run(['java', '-jar', juicer, 'pre', '-r', '100000,50000,25000,10000',
		 'preHIC.txt.gz','chr'+str(chro[0])+'.hic', 'chr'+str(chro[0])+'.size'])

subprocess.run(['rm', 'preHIC.txt.gz'] )

print("creating eigenvector...\n")
subprocess.run(['java', '-jar', juicer, 'eigenvector', '-p', 'NONE', 'chr'+str(chro[0])+'.hic', str(chro[0]), 'BP', str(RES), 'chr'+str(chro[0])+'.eigen'])

out_file = open('chr'+str(chro[0])+'_woNaN.eigen', "w")
subprocess.run(['sed', 's/NaN/0.0/g', 'chr'+str(chro[0])+'.eigen'], stdout=out_file)

print('############################################################')

