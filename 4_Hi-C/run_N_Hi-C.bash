for i in 362

do

for j in `seq 1 8`
do
cd /scratch/white.do/Pairing/directory_$i/part_$j
sbatch /home/white.do/DiPierroLab_Douglas/4_Hi-C/submit_Hi-C.bash
cd ../..
done

done
