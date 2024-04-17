#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --mem=100Gb
#SBATCH --time=24:00:00
#SBATCH --job-name=pdb_combiner_vmd_0
#SBATCH -o pdb_combiner_vmd_0.out

module load vmd/1.9.4

# Set input files (traj_0.pdb and traj_1.pdb)
input_traj_0="traj_0.pdb"
input_traj_1="traj_1.pdb"

# Run your VMD Tcl script
vmd -dispdev text -e /home/white.do/DiPierroLab_Douglas/6_extra_tools/histogram_distance_order_parameter/vmd_histogram_distances.tcl

# Clean up temporary files (if needed)
# rm -f temp_files/*.pdb

# End of script
