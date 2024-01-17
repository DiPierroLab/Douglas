#!/bin/bash
#SBATCH --nodes=1
#SBATCH --partition=short
#SBATCH --time=1:00:00
#SBATCH --job-name=submit_timeframe
#SBATCH -o submit_timeframe.out

j=10
cd /scratch/white.do/Pairing/directory_59/part_1
sed "s/segment_index/$j/g" /home/white.do/DiPierroLab_Douglas/3_simulations/rename_traj.bash > rename_traj_N.bash
bash rename_traj_N.bash
bash /home/white.do/DiPierroLab_Douglas/3_simulations/run_N_MiChroM_sims_from_initial_structure.bash
