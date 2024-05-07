#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --mem=100G
#SBATCH --time=24:00:00
#SBATCH --job-name=combine_0
#SBATCH -o combine_0.out

source ~/miniconda3/etc/profile.d/conda.sh

conda activate toy_pairing_environment

python combine_pdb_0.py
