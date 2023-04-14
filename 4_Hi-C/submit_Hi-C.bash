#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --time=24:00:00
#SBATCH --job-name=HiC

source ~/miniconda3/etc/profile.d/conda.sh

conda activate simulation

python /home/white.do/DiPierroLab_Douglas/Hi-C/Hi-C_double.py