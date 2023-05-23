cd /work/dipierrolab/secret/final_Hi-C_maps/
for j in `seq 192 200`
do 
sed "s/segment_index/$j/g" /home/white.do/DiPierroLab_Douglas/4_Hi-C/submit_dense_to_hic.bash > ./submit_dense_to_hic_$j.bash
sbatch submit_dense_to_hic_$j.bash 
done
