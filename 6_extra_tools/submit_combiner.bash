#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --mem=100Gb
#SBATCH --time=24:00:00
#SBATCH --job-name=pdb_combiner
#SBATCH -o pdb_combiner.out

source ~/miniconda3/etc/profile.d/conda.sh

conda activate toy_pairing_environment

python combiner.py
