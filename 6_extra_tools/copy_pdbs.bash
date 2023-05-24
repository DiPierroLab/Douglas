cd /scratch/white.do/Pairing/

for j in `seq 192 200`
do
cd directory_$j/part_1/
sed "s/directoryjparti/directory_${j}_part_1/g" /home/white.do/DiPierroLab_Douglas/6_extra_tools/copy_pdbs_directory_N.bash > ./copy_pdbs_directory_${j}_part_1.bash
sed "s/directoryjparti/directory_${j}_part_1/g" /home/white.do/DiPierroLab_Douglas/6_extra_tools/submit_copy_pdbs_directory_N.bash > ./submit_copy_pdbs_directory_${j}_part_1.bash
sbatch submit_copy_pdbs_directory_${j}_part_1.bash
cd ../..
done
