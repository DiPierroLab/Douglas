cd /scratch/white.do/Pairing/

for j in `seq 174 176`
do 
for i in `seq 1 8`
do
mkdir -p directory_$j
cd directory_$j
mkdir -p part_$i
cp /home/white.do/DiPierroLab_Douglas/3_simulations/Toy_directory_$j.py ./
cd part_$i
sed "s/segment_index/$j/g" /home/white.do/DiPierroLab_Douglas/3_simulations/submit_MiChroM_special.bash > ./submit_MiChroM_special.bash 
sbatch submit_MiChroM_special.bash 
cd ../..
done
done
