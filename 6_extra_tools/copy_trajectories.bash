cd /scratch/white.do/Pairing/

for j in `seq 192 200`
do
cd directory_$j
for i in `seq 1 32`
do
cd part_$i
sed "s/directoryjparti/directory_$j_part_$i/g" /home/white.do/DiPierroLab_Douglas/6_extra_tools/copy_trajectories_directory_N.bash > ./copy_trajectories_directory_$j.bash
sed "s/directoryjparti/directory_$j_part_$i/g" /home/white.do/DiPierroLab_Douglas/6_extra_tools/submit_copy_trajectories_directory_N.bash > ./submit_copy_trajectories_directory_$j.bash
sbatch submit_copy_trajectories_directory_$j.bash
cd ..
done
cd ..
done
