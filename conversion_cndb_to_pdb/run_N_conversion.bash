for i in `seq 159 159`

do

for j in 1 2
do
cd /scratch/white.do/Pairing/directory_$i/part_$j
sbatch ~/submit_conversion_0.bash
sbatch ~/submit_conversion_1.bash
cd ../..
done

done
