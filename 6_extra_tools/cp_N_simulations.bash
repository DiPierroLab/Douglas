cd /scratch/white.do/Pairing/

for j in `seq 12 17`
do 
sed "s/segment_index/$j/g" /home/white.do/DiPierroLab_Douglas/6_extra_tools/submit_cp_simulation.bash > ./submit_cp_simulation_directory_$j.bash
sbatch submit_cp_simulation_directory_$j.bash 
done
