#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --time=24:00:00
#SBATCH --job-name=HiC
#SBATCH -o histogram.out

source ~/miniconda3/etc/profile.d/conda.sh

conda activate simulation

python /home/white.do/DiPierroLab_Douglas/6_extra_tools/phase_diagram_average_distance/histogram_maker.py
