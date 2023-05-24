cd /scratch/white.do/Pairing/

for j in `seq 192 200`
do
cd directory_$j
for i in `seq 2 32`
do
cd part_$i
sed "s/directoryjparti/directory_${j}_part_$i/g" /home/white.do/DiPierroLab_Douglas/6_extra_tools/copy_cndbs_directory_N.bash > ./copy_cndbs_directory_${j}_part_$i.bash
sed "s/directoryjparti/directory_${j}_part_$i/g" /home/white.do/DiPierroLab_Douglas/6_extra_tools/submit_copy_cndbs_directory_N.bash > ./submit_copy_cndbs_directory_${j}_part_$i.bash
sbatch submit_copy_cndbs_directory_${j}_part_$i.bash
cd ..
done
cd ..
done
