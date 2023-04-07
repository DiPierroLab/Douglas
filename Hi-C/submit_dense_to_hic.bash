#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --time=24:00:00
#SBATCH --job-name=dense_to_hic
#SBATCH --mem=50Gb

mkdir -p directory_segment_index
cd directory_segment_index
python3 /home/white.do/DiPierroLab_Douglas/Hi-C/DAT2HIC.py 1 50000 ../Hi-C_directory_segment_index.txt ~/juicer_tools_1.22.01.jar
mv chr1.hic ../Hi-C_directory_segment_index.hic
cd ..
rm -r directory_segment_index

