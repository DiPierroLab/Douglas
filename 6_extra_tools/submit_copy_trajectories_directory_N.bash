#!/bin/bash
#SBATCH --nodes=1
#SBATCH --partition=short
#SBATCH --time=24:00:00
#SBATCH --job-name=cp_trajs
bash copy_trajectories_directory_directoryjparti.bash
