for i in `seq 345 352`

do

for j in 1
do
cd /scratch/white.do/Pairing/directory_$i/part_$j
sbatch /home/white.do/DiPierroLab_Douglas/4_Hi-C/submit_Hi-C.bash
cd ../..
done

done
