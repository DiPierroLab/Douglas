#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --time=24:00:00
#SBATCH --job-name=cndb_ndb_pdb
#SBATCH -o conversion_0.out

source ~/miniconda3/etc/profile.d/conda.sh

conda activate toy_pairing_environment

/home/white.do/DiPierroLab_Douglas/5_conversion_cndb_to_pdb/cndb2ndbAilun.py -f traj_0.cndb -n traj_0
/home/white.do/DiPierroLab_Douglas/5_conversion_cndb_to_pdb/ndb2pdb.py -f traj_0.ndb -n traj_0
