#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --time=24:00:00
#SBATCH --job-name=pairwise_distance_finder
#SBATCH --mem=128Gb

source ~/miniconda3/etc/profile.d/conda.sh

conda activate simulation

python ~/pairwise_distance_finder.py
