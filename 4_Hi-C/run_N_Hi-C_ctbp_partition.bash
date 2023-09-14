for i in 12 13 14

do

for j in `seq 1 32` 
do
cd /scratch/white.do/Pairing/directory_$i/part_$j
sbatch /home/white.do/DiPierroLab_Douglas/4_Hi-C/submit_Hi-C_ctbp_partition.bash
cd ../..
done

done
