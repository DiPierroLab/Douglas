#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --time=24:00:00
#SBATCH --job-name=HiC

source ~/miniconda3/etc/profile.d/conda.sh

conda activate simulation

python ~/Hi-C_double.py
