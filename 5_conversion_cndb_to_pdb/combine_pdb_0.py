print('afsdasdf',flush=True)
from Bio import PDB

def extract_tenth_frame(input_file):
    # Parse PDB file
    print('1',flush=True)
    parser = PDB.PDBParser(QUIET=True)
    structure = parser.get_structure("protein", input_file)

    # Select every tenth model
    tenth_frame = [model for i, model in enumerate(structure) if i % 10 == 0]

    return tenth_frame

def combine_pdb_files(input_files, output_file):
    # Create a new structure to store combined frames
    print('2',flush=True)
    combined_structure = PDB.Structure.Structure("combined_structure")

    # Iterate through input files and extract every tenth frame
    for input_file in input_files:
        # Create a new structure for each input file
        input_structure = PDB.Structure.Structure("input_structure")
        input_frames = extract_tenth_frame(input_file)

        # Add frames to the input structure
        for frame in input_frames:
            input_structure.add(frame)

        # Add the input structure to the combined structure
        combined_structure.add(input_structure)

    # Write the combined structure to the output file
    io = PDB.PDBIO()
    io.set_structure(combined_structure)
    io.save(output_file, write_model=True)

print('0',flush=True)
traj_0_timespan_2 = '/scratch/white.do/Pairing/directory_55/part_1/traj_0_timespan_2.pdb'
traj_0_timespan_3 = '/scratch/white.do/Pairing/directory_55/part_1/traj_0_timespan_3.pdb'
traj_0_timespan_4 = '/scratch/white.do/Pairing/directory_55/part_1/traj_0_timespan_4.pdb'
traj_0_timespan_5 = '/scratch/white.do/Pairing/directory_55/part_1/traj_0_timespan_5.pdb'
traj_0_timespan_6 = '/scratch/white.do/Pairing/directory_55/part_1/traj_0_timespan_6.pdb'
traj_0_timespan_7 = '/scratch/white.do/Pairing/directory_55/part_1/traj_0_timespan_7.pdb'
traj_0_timespan_8 = '/scratch/white.do/Pairing/directory_55/part_1/traj_0_timespan_8.pdb'
traj_0_timespan_9 = '/scratch/white.do/Pairing/directory_55/part_1/traj_0_timespan_9.pdb'
traj_0_timespan_10 = '/scratch/white.do/Pairing/directory_55/part_1/traj_0_timespan_10.pdb'

print('Combining traj_0s')
input_files_0 = [traj_0_timespan_2,traj_0_timespan_3,traj_0_timespan_4,traj_0_timespan_5,traj_0_timespan_6,traj_0_timespan_7,traj_0_timespan_8,traj_0_timespan_9,traj_0_timespan_10]
output_file_0 = '/scratch/white.do/Pairing/directory_55/part_1/traj_0_timespans_2_to_10_every_10th_frame.pdb'
combine_pdb_files(input_files_0, output_file_0)
