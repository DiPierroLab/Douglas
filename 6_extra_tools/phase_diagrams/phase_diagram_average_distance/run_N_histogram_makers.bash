for i in `seq 175 344`

do

for j in 1
do
cd /scratch/white.do/Pairing/directory_$i/part_$j
sbatch /home/white.do/DiPierroLab_Douglas/6_extra_tools/phase_diagram_average_distance/submit_histogram_maker.bash
cd ../..
done

done
