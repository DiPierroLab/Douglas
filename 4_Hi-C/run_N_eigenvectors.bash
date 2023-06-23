cd /work/dipierrolab/douglas/final_Hi-C_maps/
for j in 1
do 
sed "s/segment_index/$j/g" /home/white.do/DiPierroLab_Douglas/4_Hi-C/submit_eigenvector.bash > ./submit_eigenvector_$j.bash
sbatch submit_eigenvector_$j.bash 
done
