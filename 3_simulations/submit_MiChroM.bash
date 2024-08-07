#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=gpu
#SBATCH --time=08:00:00
#SBATCH --job-name=MiChroM
#SBATCH --mem=100Gb
#SBATCH --gres=gpu:1
#SBATCH -o MiChroM_sim.out 

source ~/miniconda3/etc/profile.d/conda.sh

conda activate toy_pairing_environment

python /scratch/white.do/Pairing/directory_segment_index/Toy_directory_segment_index.py
