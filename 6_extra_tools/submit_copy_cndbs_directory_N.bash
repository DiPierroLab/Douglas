#!/bin/bash
#SBATCH --nodes=1
#SBATCH --partition=short
#SBATCH --time=24:00:00
#SBATCH --job-name=cp_cndbs
bash copy_cndbs_directoryjparti.bash
