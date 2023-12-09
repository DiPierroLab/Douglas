lambdas_file_name = "lambdas167"#segment_index"#you should have three .txt files in dense format in the lambdas folder; 
#segment_index is changed by a different script into the simulation number in order to reference the correct lambdas matrix.
dt = .01 #timestep for the main simulation; dt=.01 in tutorial
stepsPerBlock = 1000 #steps per block (standard is 1000)
n_blocks = 30000 #number of blocks (standard is 30000)
initial_block_number = 30000 #number of the initial structure; the number of the previous run's final block
#========================================
import datetime
import sys
sys.path.append('/home/white.do/DiPierroLab_Douglas/3_simulations')
from ChromDynamicsDouglasCompareAilun import MiChroM
#===========================================
startTime = datetime.datetime.now()
print("start time:")
print(str(startTime))
#======================================================
sim = MiChroM(name="chr_chr", temperature=1.0, time_step=dt)
sim.setup(platform="opencl")
sim.saveFolder('./')
Struc = sim.loadNDB(NDBfiles=['/scratch/white.do/Pairing/directory_55/part_1/chr_chr_0_block'+initial_block_number+'.ndb','/scratch/white.do/Pairing/directory_55/part_1/chr_chr_0_block'+initial_block_number+'.ndb'])
Struc = sim.setFibPosition(Struc, dist=(1.5,3.0))
sim.loadStructure(Struc, center=False)
sim.saveStructure(mode='ndb')
#Homopolymer Potentials
sim.addFENEBonds(kfb=30.0)
sim.addAngles(ka=2.0)
sim.addRepulsiveSoftCore(Ecut=4.0)
sim.addFlatBottomHarmonic(n_rad=20)
#adding MiChroM energy with a lambdas matrix
sim.addLambdas(mu=3.22, rc = 1.78, LambdasArray='/work/dipierrolab/douglas/lambdas/'+lambdas_file_name+'.txt')
#adding 12th power repulsion to prevent corresponding beads from overlapping in trans
sim.addTransRepulsions(k=30.0)
#================================================================
#setup complete
sim.initStorage('traj', mode='w')
for _ in range(n_blocks):
    sim.runSimBlock(stepsPerBlock,increment=True)
    sim.saveStructure()

sim.storage[0].close() #close the cndb file for chr_copy1
sim.storage[1].close() #close the cndb file for chr_copy2

sim.saveStructure(mode="ndb")
sim.saveStructure(mode="pdb")
#==========================================
endTime = datetime.datetime.now()
print("start time:")
print(str(startTime))
print("end time: ")
print(str(endTime))
