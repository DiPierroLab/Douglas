#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --time=24:00:00
#SBATCH --job-name=cndb_ndb_pdb

source ~/miniconda3/etc/profile.d/conda.sh

conda activate simulation

/home/white.do/DiPierroLab_Douglas/conversion_cndb_to_pdb/cndb2ndbAilun.py -f traj_1.cndb -n traj_1
/home/white.do/DiPierroLab_Douglas/conversion_cndb_to_pdb/ndb2pdb.py -f traj_1.ndb -n traj_1
