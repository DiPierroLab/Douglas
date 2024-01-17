#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--partition=gpu
#SBATCH --time=08:00:00
#SBATCH --job-name=MiChroM
#SBATCH --mem=100Gb
#SBATCH --gres=gpu:1
#SBATCH -o timespan.out 

cd /scratch/white.do/Pairing/directory_59/part_1

mv traj_0.cndb traj_0_timespan_1.cndb
mv traj_0.ndb traj_0_timespan_1.ndb
mv traj_0.pdb traj_0_timespan_1.pdb
mv traj_1.cndb traj_1_timespan_1.cndb
mv traj_1.ndb traj_1_timespan_1.ndb
mv traj_1.pdb traj_1_timespan_1.pdb

source ~/miniconda3/etc/profile.d/conda.sh

conda activate simulation

python /home/white.do/DiPierroLab_Douglas/3_simulations/Toy_directory_59_from_initial_structure.py
