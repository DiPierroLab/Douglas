cd /scratch/white.do/Pairing/

for j in 55
do 
for i in 1
do
mkdir -p directory_$j
cd directory_$j
sed "s/segment_index/$j/g" /home/white.do/DiPierroLab_Douglas/3_simulations/Toy_directory_N_from_initial_structure.py > ./Toy_directory_${j}_from_initial_structure.py
mkdir -p part_$i
cd part_$i
sed "s/segment_index/$j/g" /home/white.do/DiPierroLab_Douglas/3_simulations/submit_MiChroM_from_initial_structure.bash > ./submit_MiChroM_from_initial_structure.bash
bash /home/white.do/DiPierroLab_Douglas/6_extra_tools/awk_pot_Rg.bash
sbatch submit_MiChroM_from_initial_structure.bash 
cd ../..
done
done
