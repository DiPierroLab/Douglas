cd /scratch/white.do/Pairing/

for j in `seq 183 191`
do 
for i in 1
do
mkdir -p directory_$j
cd directory_$j
sed "s/segment_index/$j/g" /home/white.do/DiPierroLab_Douglas/3_simulations/Toy_directory_${j}_from_initial_structure.py > ./Toy_directory_${j}_from_initial_structure.py
mkdir -p part_$i
cd part_$i
sed "s/segment_index/$j/g" /home/white.do/DiPierroLab_Douglas/3_simulations/submit_MiChroM_from_initial_structure.bash > ./submit_MiChroM_from_initial_structure.bash
sbatch submit_MiChroM_from_initial_structure.bash 
cd ../..
done
done
