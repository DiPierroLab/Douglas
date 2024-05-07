#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=ctbp
#SBATCH --time=24:00:00
#SBATCH --job-name=HiC
#SBATCH -o Hi-C.out

source ~/miniconda3/etc/profile.d/conda.sh

conda activate toy_pairing_environment

python /home/white.do/DiPierroLab_Douglas/4_Hi-C/Hi-C_double.py
