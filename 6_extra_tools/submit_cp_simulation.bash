#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --time=24:00:00
#SBATCH --job-name=cp_sim
#SBATCH -o cp_sim_segment_index.out

cp -rf directory_segment_index /work/dipierrolab/douglas/final_simulations/
