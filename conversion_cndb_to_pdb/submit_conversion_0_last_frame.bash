#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --time=24:00:00
#SBATCH --job-name=last_frame_0

source ~/miniconda3/etc/profile.d/conda.sh

conda activate simulation

~/ndb2pdb.py -f chr10_chr10_0_block30005.ndb -n last_frame_0
