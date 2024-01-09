from Bio import PDB

def extract_tenth_frame(input_file, output_file):
    try:
        # Parse PDB file using MMCIFParser
        parser = PDB.MMCIFParser(QUIET=True)
        structure = parser.get_structure("protein", input_file)

        # Write models directly to the output file
        io = PDB.PDBIO()
        for i, model in enumerate(structure):
            if i % 10 == 0:
                io.set_structure(model)
                io.save(output_file, write_model=True)

    except KeyError as e:
        print(f"Error parsing {input_file}: {e}")

def combine_pdb_files(input_files, output_file):
    # Iterate through input files and extract every tenth frame
    for input_file in input_files:
        extract_tenth_frame(input_file, output_file)

traj_0_timespan_2 = '/scratch/white.do/Pairing/directory_55/part_1/traj_0_timespan_2.pdb'
traj_0_timespan_3 = '/scratch/white.do/Pairing/directory_55/part_1/traj_0_timespan_3.pdb'
traj_0_timespan_4 = '/scratch/white.do/Pairing/directory_55/part_1/traj_0_timespan_4.pdb'
traj_0_timespan_5 = '/scratch/white.do/Pairing/directory_55/part_1/traj_0_timespan_5.pdb'
traj_0_timespan_6 = '/scratch/white.do/Pairing/directory_55/part_1/traj_0_timespan_6.pdb'
traj_0_timespan_7 = '/scratch/white.do/Pairing/directory_55/part_1/traj_0_timespan_7.pdb'
traj_0_timespan_8 = '/scratch/white.do/Pairing/directory_55/part_1/traj_0_timespan_8.pdb'
traj_0_timespan_9 = '/scratch/white.do/Pairing/directory_55/part_1/traj_0_timespan_9.pdb'
traj_0_timespan_10 = '/scratch/white.do/Pairing/directory_55/part_1/traj_0_timespan_10.pdb'

print('Combining traj_0s',flush=True)
input_files_0 = [traj_0_timespan_2,traj_0_timespan_3,traj_0_timespan_4,traj_0_timespan_5,traj_0_timespan_6,traj_0_timespan_7,traj_0_timespan_8,traj_0_timespan_9,traj_0_timespan_10]
output_file_0 = '/scratch/white.do/Pairing/directory_55/part_1/traj_0_timespans_2_to_10_every_10th_frame.pdb'
combine_pdb_files(input_files_0, output_file_0)
