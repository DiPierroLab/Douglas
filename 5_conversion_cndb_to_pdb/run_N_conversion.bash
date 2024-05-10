for i in 363 367

do

for j in 1
do
cd /scratch/white.do/Pairing/directory_$i/part_$j
sbatch /home/white.do/DiPierroLab_Douglas/5_conversion_cndb_to_pdb/submit_conversion_0.bash
sbatch /home/white.do/DiPierroLab_Douglas/5_conversion_cndb_to_pdb/submit_conversion_1.bash
cd ../..
done

done
