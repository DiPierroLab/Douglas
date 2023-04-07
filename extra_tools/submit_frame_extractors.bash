#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --time=24:00:00
#SBATCH --job-name=frame_extractor

source ~/miniconda3/etc/profile.d/conda.sh

conda activate simulation

python ~/frame_extractor_traj_0.py
python ~/frame_extractor_traj_1.py
