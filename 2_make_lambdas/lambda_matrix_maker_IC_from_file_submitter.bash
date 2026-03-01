#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=short
#SBATCH --time=24:00:00
#SBATCH --job-name=make_Lambda
#SBATCH -o make_Lambda.out

source ~/miniconda3/etc/profile.d/conda.sh

conda activate toy_pairing_environment

python /home/white.do/DiPierroLab_Douglas/2_make_lambdas/lambda_matrix_maker_IC_from_file.py segment_index AAAA AAAA gamma_phase_diagram_cis.txt gamma_trans_segment_index.txt TTTTT False False 2
