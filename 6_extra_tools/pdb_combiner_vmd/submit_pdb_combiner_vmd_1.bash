#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --mem=100Gb
#SBATCH --time=24:00:00
#SBATCH --job-name=pdb_combiner_vmd_1
#SBATCH -o pdb_combiner_vmd_1.out

module load vmd/1.9.4

vmd -dispdev text -e pdb_combiner_vmd_1.tcl
