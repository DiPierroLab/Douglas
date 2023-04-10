Numerical order roughly orders the workflow. 

We seek to sample the canonical ensemble for two interacting polymer chains with 2500 beads each.
1. Generate a sequence of chromatin types (A or B) and a sequences of pairing types (T, L, or N) for each chain.
2. Create a lambdas matrix which comprises the Hamiltonian.
     Run lambda_matrix_maker.py in an interactive session and feed in arguments.
     This helps define the interaction energies for a structure.
     Make a colorful .pdf of your lambdas matrix with the visualize_lambdas.ipynb Jupyter notebook. 
3. Run computational experiments. 
     For each experiment, run multiple simulations with the same code. This will speed up sampling.
     Run each simulation on a GPU to speed up computations.
4. Make Hi-C maps for each experiment.
     Start by making a Hi-C map for each simulation.
     Average the Hi-C maps from the same experiment. This produces a higher quality Hi-C map. 
     Convert the output .txt file to .hic file. Open the .hic file in juicebox to render the Hi-C map as a .pdf file.

Optional
5. Visualize a simulation in VMD. 
     First, convert binary .cndb files into .pdb files.
     Next, open one .pdb file for each chain as a new molecule in VMD.
6. If you need me to explain what "6_extra_tools" means, then you haven't gotten read this far.
