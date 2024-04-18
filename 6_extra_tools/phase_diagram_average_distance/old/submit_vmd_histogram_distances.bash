#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --mem=100Gb
#SBATCH --time=24:00:00
#SBATCH --job-name=pdb_combiner_vmd_0
#SBATCH -o pdb_combiner_vmd_0.out

module load vmd/1.9.4

vmd -dispdev text -e /home/white.do/DiPierroLab_Douglas/6_extra_tools/histogram_distance_order_parameter
/vmd_histogram_distances.tcl
