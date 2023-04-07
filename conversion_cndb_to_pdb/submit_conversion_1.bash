#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --time=24:00:00
#SBATCH --job-name=cndb_ndb_pdb

source ~/miniconda3/etc/profile.d/conda.sh

conda activate simulation

~/cndb2ndbAilun.py -f traj_1.cndb -n traj_1
~/ndb2pdb.py -f traj_1.ndb -n traj_1
