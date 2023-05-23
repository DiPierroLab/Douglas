for j in `seq 1 32`
do
cp -R ./directory_segment_index/part_$j/traj_0.cndb /work/dipierrolab/secret/final_structures/traj_0_sim_segment_index.cndb
cp -R ./directory_segment_index/part_$j/traj_1.cndb /work/dipierrolab/secret/final_structures/traj_1_sim_segment_index.cndb
done
