#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --time=24:00:00
#SBATCH --job-name=HiC_averager
#SBATCH -o Hi-C_averager.out

source ~/miniconda3/etc/profile.d/conda.sh

conda activate toy_pairing_environment

python /home/white.do/DiPierroLab_Douglas/4_Hi-C/Hi-C_averager.py
