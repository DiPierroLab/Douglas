cd /scratch/white.do/Pairing/

for j in 159
do 
for i in `seq 3 32`
do
mkdir -p directory_$j
cd directory_$j
mkdir -p part_$i
cp ~/Toy_directory_$j.py ./
cd part_$i
sed "s/segment_index/$j/g" ~/submit_MiChroM_special.bash > ./submit_MiChroM_special.bash 
sbatch submit_MiChroM_special.bash 
cd ../..
done
done
