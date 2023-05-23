cd /scratch/white.do/Pairing/

for j in `seq 192 200`
do
for i in `seq 1 32`
do
cd directory_$j
sed "s/segment_index/$j/g" /home/white.do/DiPierroLab_Douglas/6_extra_tools/copy_trajectories_directory_N.bash > ./copy_trajectories_directory_$j.bash
sed "s/segment_index/$j/g" /home/white.do/DiPierroLab_Douglas/6_extra_tools/submit_copy_trajectories_directory_N.bash > ./submit_copy_trajectories_directory_$j.bash
sbatch submit_copy_trajectories_directory_$j.bash
done
done
