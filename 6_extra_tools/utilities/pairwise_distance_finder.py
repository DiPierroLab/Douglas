from numpy import array, loadtxt, savetxt, sort
from numpy.linalg import norm

t0 = loadtxt('traj_0_block_1.txt')
t1 = loadtxt('traj_1_block_1.txt')

file = open('pairwise_distances_block_1.txt','w')
N = 2500
#cis
for i in range(N):
    for j in range(i+1,N):
        file.write(str(i)+' '+str(j)+' '+str(norm(array(t0[i])-array(t0[j])))+'\n')
        file.write(str(i+N)+' '+str(j+N)+' '+str(norm(array(t1[i])-array(t1[j])))+'\n')
#trans
for i in range(N):
    for j in range(N):
        file.write(str(i)+' '+str(j+N)+' '+str(norm(array(t0[i])-array(t1[j])))+'\n')
file.close()
dtype = [('index0',float),('index1',float),('pairwise_distance',float)]
pds = loadtxt('./pairwise_distances_block_1.txt',dtype=dtype)
pds = sort(pds, axis = 0, order = 'pairwise_distance')
savetxt('sorted_pairwise_distances_block_1.txt',pds)
