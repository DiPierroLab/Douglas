
cd /scratch/white.do/Pairing/

for i in `seq 175 223`
do

mkdir -p directory_$i
cd directory_$i
sed "s/segment_index/$i/g" /home/white.do/DiPierroLab_Douglas/2_make_lambdas/submit_make_lambdas.bash > ./make_lambda.bash
sbatch make_lambda.bash 
cd ..

done
