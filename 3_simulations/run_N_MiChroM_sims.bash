cd /scratch/white.do/Pairing/

for j in `seq 167 167`
do 
for i in `seq 1 32`
do
mkdir -p directory_$j
cd directory_$j
sed "s/segment_index/$j/g" /home/white.do/DiPierroLab_Douglas/simulations/Toy_directory_N.py > ./Toy_directory_$j.py
mkdir -p part_$i
cd part_$i
sed "s/segment_index/$j/g" /home/white.do/DiPierroLab_Douglas/simulations/submit_MiChroM.bash > ./submit_MiChroM.bash
sbatch submit_MiChroM.bash 
cd ../..
done
done