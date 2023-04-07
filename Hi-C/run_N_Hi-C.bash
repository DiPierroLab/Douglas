for i in `seq 160 167` 

do

for j in `seq 1 32`
do
cd /scratch/white.do/Pairing/directory_$i/part_$j
sbatch ~/submit_Hi-C.bash
cd ../..
done

done
