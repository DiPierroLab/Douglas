#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --time=24:00:00
#SBATCH --job-name=frame_extractor
#SBATCH -o frame_extractors.out

source ~/miniconda3/etc/profile.d/conda.sh

conda activate toy_pairing_environment

python /home/white.do/DiPierroLab_Douglas/conversion_cndb_to_pdb/frame_extractor_traj_0.py
python /home/white.do/DiPierroLab_Douglas/conversion_cndb_to_pdb/frame_extractor_traj_1.py
