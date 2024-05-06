Before starting to follow the pipeline outlined below, create a new conda environment.

1. Install anaconda or miniconda onto your supercomputer or less favorably your local machine.
I used Python 3.8.13.

2. Run the following command:
conda create --name simulation --file ./requirements_conda.txt
#'simulation' is the environment name. If you change it, you will also need to change it in the submission scripts.

Next, adjust the paths in the .py files.

The codes are written to be ran on a supercomputer using slurm.

We seek to sample the canonical ensemble for two interacting polymer chains with 2500 beads each.

1. Generate a sequence of chromatin types (A or B) and a sequences of pairing types (T, L, or N) for each chain. Do this by running an appropriate script from 1_make_sequences. To make your own script, edit and run one of those provided.
 
2. Create a lambdas matrix which comprises the Hamiltonian.
     Run lambda_matrix_maker.py in an interactive session and feed in arguments.
     This helps define the interaction energies for a structure.
     Make a colorful .pdf visualization of your lambdas matrix with the visualize_lambdas.ipynb Jupyter notebook. 

3. Run computational experiments (a.k.a., simulations). 
     For each experiment, run multiple simulations with the same code. Such trivial parallelization speeds up sampling. To do this, run run_N_MiChroM_sims.bash, which modifies the submission script submit_MiChroM.bash to submit multiple copies of Toy_directory_N.py. 
     Run each simulation on a GPU to speed up computations. This is an advantage of using an openmm integrator.

4. Make Hi-C maps for each experiment.
     Start by making a Hi-C map for each simulation. Do this by running run_N_Hi-C.bash, which modifies the submission script submit_Hi-C.bash to submit one copy of Hi-C_double.py (double because there are two chromosomes) for each simulation copy that you ran in step 3.
     After individual Hi-C maps for each simulation are finished, average them using Hi-C_adder.py.
     Convert the resulting Hi-C_directory_N.txt file into a .hic file by running run_N_dense_to_hic.bash, which submits submit_dense_to_hic.bash. 
     Open the .hic file in the juicebox program by aidenlab https://aidenlab.org/software.html to render the Hi-C map as a .pdf file.

Optional (as is pretty much everything else in life)

5. Visualize a simulation in VMD. 
     First, convert binary .cndb files into .pdb files. To do this, run the bash script run_N_conversion.bash, which submits .cndb to .ndb to .pdb converters using modifications of submit_conversion_0.bash and submit_conversion_1.bash.
     Next, open one .pdb file for each chain as a new molecule in the protein visualization program VMD.

6. Extra tools include hicTools, which can find eigenvectors or pick out quadrants of a Hi-C map. hicTools can also write a file of contact probabilities vs genomic distance. Ps_vs_genomic can then visualize the written files.
