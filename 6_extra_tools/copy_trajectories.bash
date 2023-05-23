cd /scratch/white.do/Pairing/
for i in `seq 192 200`
do
sed "s/segment_index/$i/g" /home/white.do/DiPierroLab_Douglas/6_extra_tools/copy_trajectories_directory_N.bash > ./copy_trajectories_directory_$i.bash
sed "s/segment_index/$i/g" /home/white.do/DiPierroLab_Douglas/6_extra_tools/submit_copy_trajectories_directory_N.bash > ./submit_copy_trajectories_directory_$i.bash
sbatch submit_copy_trajectories_directory_$i.bash
done

