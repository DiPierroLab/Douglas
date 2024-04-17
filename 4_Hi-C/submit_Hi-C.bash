#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --time=24:00:00
#SBATCH --job-name=HiC
#SBATCH -o Hi-C.out

source ~/miniconda3/etc/profile.d/conda.sh

conda activate simulation

python /home/white.do/DiPierroLab_Douglas/4_Hi-C/Hi-C_double.py traj_0.cndb traj_1.cndb Hi-C_multi 10 10000
