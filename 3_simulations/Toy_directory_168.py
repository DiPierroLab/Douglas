lambdas_file_name = "lambdas167"#you should have three .txt files in dense format in the lambdas folder; 
#segment_index is changed by a different script into the simulation number in order to reference the correct lambdas matrix.
dt = .01 #timestep for the main simulation; dt=.01 in tutorial
stepsPerBlock = 1 #steps per block (standard is 1000)
n_blocks = 33 #number of blocks (standard is 30000)
collapse_stepsPerBlock = 1000
collapse_n_blocks = 10
#========================================
import datetime
import sys
sys.path.append('/home/white.do/DiPierroLab_Douglas/3_simulations')
from ChromDynamicsDouglasCompareAilun import MiChroM
from OpenMiChroM.CndbTools import cndbTools
import openmm as mm
import numpy as np
#===========================================
startTime = datetime.datetime.now()
print("start time:")
print(str(startTime))
#===================Collapses==========================
sim_chr_copy1 = MiChroM(name="chr_copy1", temperature=1.0, time_step=.01)
sim_chr_copy1.setup(platform="opencl")
sim_chr_copy1.saveFolder('./')
Chrom10_copy1 = sim_chr_copy1.create_springSpiral(ChromSeq='/work/dipierrolab/secret/lambdas/chr_AAAA_2500_beads.txt')
sim_chr_copy1.loadStructure(Chrom10_copy1, center=True)

sim_chr_copy1.addFENEBonds(kfb=30.0)
sim_chr_copy1.addAngles(ka=2.0)
sim_chr_copy1.addRepulsiveSoftCore(Ecut=4.0)
sim_chr_copy1.addFlatBottomHarmonic()

#adding MiChroM energy with a lambdas matrix
sim_chr_copy1.addLambdas(mu=3.22, rc = 1.78, LambdasArray='/work/dipierrolab/secret/lambdas/'+lambdas_file_name+'_0.txt')

print("Performing paternal collapse simulation...")
for _ in range(collapse_n_blocks):
    sim_chr_copy1.runSimBlock(collapse_stepsPerBlock, increment=False)

sim_chr_copy1.saveStructure(filename="chr_copy1" ,mode="ndb")
del sim_chr_copy1
#------------------------------------------------------------------------------

sim_chr_copy2 = MiChroM(name="chr_copy2", temperature=1.0, time_step=0.01)
sim_chr_copy2.setup(platform="opencl")
sim_chr_copy2.saveFolder('./')
Chrom10_copy2 = sim_chr_copy2.create_springSpiral(ChromSeq='/work/dipierrolab/secret/lambdas/chr_AAAA_2500_beads.txt')
sim_chr_copy2.loadStructure(Chrom10_copy2, center=True)

sim_chr_copy2.addFENEBonds(kfb=30.0)
sim_chr_copy2.addAngles(ka=2.0)
sim_chr_copy2.addRepulsiveSoftCore(Ecut=4.0)
sim_chr_copy2.addFlatBottomHarmonic()

#adding MiChroM energy with a lambdas matrix
sim_chr_copy2.addLambdas(mu=3.22, rc = 1.78, LambdasArray='/work/dipierrolab/secret/lambdas/'+lambdas_file_name+'_1.txt')

print("Perform maternal collapse simulation...")
for _ in range(collapse_n_blocks):
    sim_chr_copy2.runSimBlock(collapse_stepsPerBlock, increment=False)

sim_chr_copy2.saveStructure(filename="chr_copy2", mode="ndb")
del sim_chr_copy2
#==============================================================

sim = MiChroM(name="chr_chr", temperature=1.0, time_step=dt)
sim.setup(platform="opencl")
sim.saveFolder('./')
Struc = sim.loadNDB(NDBfiles=['./chr_copy1_0_block0.ndb','./chr_copy2_0_block0.ndb'])
Struc = sim.setFibPosition(Struc, dist=(1.5,3.0))
sim.loadStructure(Struc, center=True)
sim.saveStructure(mode='ndb')
#Homopolymer Potentials
sim.addFENEBonds(kfb=30.0)
sim.addAngles(ka=2.0)
sim.addRepulsiveSoftCore(Ecut=4.0)
sim.addFlatBottomHarmonic(n_rad=20)
#adding MiChroM energy with a lambdas matrix
sim.addLambdas(mu=3.22, rc = 1.78, LambdasArray='/work/dipierrolab/secret/lambdas/'+lambdas_file_name+'.txt')
#adding 12th power repulsion to prevent corresponding beads from overlapping in trans
sim.addTransRepulsions(k=30.0)
#================================================================
#setup complete
sim.initStorage('traj', mode='w')

print("Let the chromosomes settle into each other...")
for _ in range(10000):
    sim.runSimBlock(collapse_stepsPerBlock,increment=False)
#------------------------------------------------------------------
# I create a new simulation (called sim2) for each pair (i,j) of loci at each timestep t .
# To each simulation, I use only the structure at timestep t of the main simulation (called sim).
# The only force that I add to it is the TransRepulsion force between i and j.
# Note: sim2 does not evolve in time. 

for t in range(n_blocks):
    sim.saveStructure(filename = 'structure'+str(t), mode = 'ndb') #save ndb for use in the extra loops
    positions = sim.getPositions()#These won't change until the next time evolution, so it I pulled this out of the i and j loops for efficiency.
    for i in range(0,2499): #extra loop 1
        j = i + 2501 # we don't need to loop over j because the number of bead pairs which interact with TransRepulsion has order n
        r_tij = np.linalg.norm(positions[i] - positions[j])
        if 0.8 < r_tij < 1.2:
            sim2 = MiChroM() #create a new sim for use in pairwise energy calculation
            sim2.loadStructure('structure'+str(t)+'.ndb') #load NDB file written at current timestep
            sim2.addTransRepulsion(i,j,k=30) #add only one force between one pair of beads to sim2
            TRenergy_tij = sim2.context.getState.getPotentialEnergy()
            print('t i j r TransRepulsionEnergy(r) =',t,i,j,r_tij,TRenergy_tij)
            del sim2
        else:
            print('r_tij =',r_tij)
    #still need to copy the above code twice and edit the values that i and j will hold
    sim.runSimBlock(stepsPerBlock,increment=True)
    sim.saveStructure()

sim.storage[0].close() #close the cndb file for chr_copy1
sim.storage[1].close() #close the cndb file for chr_copy2

sim.saveStructure(mode="ndb")
#==========================================
endTime = datetime.datetime.now()
print("start time:")
print(str(startTime))
print("end time: ")
print(str(endTime))
