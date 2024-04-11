for i in 178 185 192 199 213 220 228 235 242 249 256 263

do

for j in 1
do
cd /scratch/white.do/Pairing/directory_$i/part_$j
sbatch /home/white.do/DiPierroLab_Douglas/4_Hi-C/submit_Hi-C.bash
cd ../..
done

done
