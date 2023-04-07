#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --time=24:00:00
#SBATCH --job-name=cndb_frame_grabber
#SBATCH --mem=128Gb

cd /scratch/white.do/Pairing/directory_158/part_2

source ~/miniconda3/etc/profile.d/conda.sh

conda activate simulation

python ~/cndb_frame_grabber_0.py
