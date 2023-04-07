cd /work/dipierrolab/secret/final_Hi-C_maps/
for j in 105 106 107
do 
sed "s/segment_index/$j/g" ~/submit_dense_to_hic.bash > ./submit_dense_to_hic_$j.bash
sbatch submit_dense_to_hic_$j.bash 
done
