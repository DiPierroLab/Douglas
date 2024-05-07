#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --time=24:00:00
#SBATCH --job-name=cool_to_hic
#SBATCH --mem=128Gb
#SBATCH -o cool2HiC.out

source ~/miniconda3/etc/profile.d/conda.sh

conda activate toy_pairing_environment

python /work/dipierrolab/douglas/cool_to_hic_gpt.py
