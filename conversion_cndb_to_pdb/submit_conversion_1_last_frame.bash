#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --time=24:00:00
#SBATCH --job-name=last_frame_1

source ~/miniconda3/etc/profile.d/conda.sh

conda activate simulation

/home/white.do/DiPierroLab_Douglas/conversion_cndb_to_pdb/ndb2pdb.py -f chr10_chr10_1_block30000.ndb -n last_frame_1
