#!/bin/bash
#SBATCH --nodes=1
#SBATCH --partition=short
#SBATCH --time=24:00:00
#SBATCH --job-name=cp_pdbs
#SBATCH -o copy_pdbs_directory_N.out
bash copy_pdbs_directoryjparti.bash
