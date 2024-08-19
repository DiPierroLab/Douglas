for i in `seq 411 435` 

do

for j in 2
do
cd /scratch/white.do/Pairing/directory_$i/part_$j
sbatch /home/white.do/DiPierroLab_Douglas/5_conversion_cndb_to_pdb/submit_conversion_0_last_frame.bash
sbatch /home/white.do/DiPierroLab_Douglas/5_conversion_cndb_to_pdb/submit_conversion_1_last_frame.bash
cd ../..
done

done
