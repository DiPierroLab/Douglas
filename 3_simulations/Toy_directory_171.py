lambdas_file_name = "lambdas167"#you should have three .txt files in dense format in the lambdas folder; 
#segment_index is changed by a different script into the simulation number in order to reference the correct lambdas matrix.
dt = .01 #timestep for the main simulation; dt=.01 in tutorial
stepsPerBlock = 1000 #steps per block (standard is 1000)
n_blocks = 30000 #number of blocks (standard is 30000)
collapse_stepsPerBlock = 1000
collapse_n_blocks = 500
Ecut = 8.0 #parameter for the force which repels beads from each other when they get close
#========================================
import datetime
import sys
sys.path.append('/home/white.do/DiPierroLab_Douglas/3_simulations')
from ChromDynamicsDouglasCompareAilun import MiChroM
from OpenMiChroM.CndbTools import cndbTools
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
sim_chr_copy1.addRepulsiveSoftCore(Ecut=Ecut)
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
sim_chr_copy2.addRepulsiveSoftCore(Ecut=Ecut)
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
sim.addRepulsiveSoftCore(Ecut=Ecut)
sim.addFlatBottomHarmonic(n_rad=20)
#adding MiChroM energy with a lambdas matrix
sim.addLambdas(mu=3.22, rc = 1.78, LambdasArray='/work/dipierrolab/secret/lambdas/'+lambdas_file_name+'.txt')
#================================================================
#setup complete
sim.initStorage('traj', mode='w')

print("Let the chromosomes settle into each other...")
for _ in range(collapse_n_blocks):
    sim.runSimBlock(stepsPerBlock,increment=False)
#------------------------------------------------------------------
for _ in range(n_blocks):
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
