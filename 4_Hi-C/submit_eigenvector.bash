#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --time=24:00:00
#SBATCH --job-name=eigenvector
#SBATCH --mem=128Gb
#SBATCH -o dense_to_Hi-C.out 

java -jar /home/white.do/juicer_tools_1.22.01.jar eigenvector KR Hi-C_directory_segment_index.hic 1 BP 50000 eigen_directory_segment_index.txt -p
