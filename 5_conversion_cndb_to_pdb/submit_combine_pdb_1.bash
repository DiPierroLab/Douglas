#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --mem=100G
#SBATCH --time=24:00:00
#SBATCH --job-name=combine_1
#SBATCH -o combine_1.out

source ~/miniconda3/etc/profile.d/conda.sh

conda activate simulation

python combine_pdb_1.py
