import mdtraj as md

# List of trajectory files
traj_files = [
    'traj_0_timespan_2.pdb',
    'traj_0_timespan_3.pdb',
    'traj_0_timespan_4.pdb',
    'traj_0_timespan_5.pdb',
    'traj_0_timespan_6.pdb',
    'traj_0_timespan_7.pdb',
    'traj_0_timespan_8.pdb',
    'traj_0_timespan_9.pdb',
    'traj_0_timespan_10.pdb'
]

# Load trajectories
trajectories = [md.load(file, stride=10) for file in traj_files]

# Concatenate trajectories
combined_traj = md.join(trajectories, check_topology=True)

# Save the combined trajectory to a new file
combined_traj.save('traj_0_combined.pdb', overwrite=True, options='model')

