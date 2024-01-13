#!/bin/bash
#SBATCH --nodes=1
#SBATCH --partition=gpu
#SBATCH --time=08:00:00
#SBATCH --job-name=MiChroM
#SBATCH --mem=100Gb
#SBATCH --gres=gpu:1
#SBATCH -o MiChroM_sim_from_initial_structure.out

# Set the number of copies and other parameters
num_copies=10
path='/home/white.do/DiPierroLab_Douglas/3_simulations'
scratch_path='/scratch/white.do/Pairing/directory_59/part_1'
script_name="$path/Toy_directory_N_dir_59_from_initial_structure.py"
conda_environment="simulation"

# Submit the first job without dependencies
first_job_id=$(sbatch --export=conda_environment=$conda_environment $script_name | awk '{print $4}')

# Submit the remaining jobs with dependencies on the previous job
for ((i=2; i<=$num_copies; i++))
do
    # Submit the job with dependency on the previous job
    job_id=$(sbatch --dependency=afterok:$first_job_id --export=conda_environment=$conda_environment $script_name | awk '{print $4}')

    # Update the first job ID for the next iteration
    first_job_id=$job_id
done

echo "All jobs submitted with dependencies."

