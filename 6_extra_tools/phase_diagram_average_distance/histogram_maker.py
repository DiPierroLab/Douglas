import numpy as np
import matplotlib.pyplot as plt

def read_coordinates_from_pdb(pdb_file):
    """
    Reads coordinates from a PDB file and extracts bead 1250's position.
    Assumes the PDB format has columns for atom name, residue name, residue ID, and x, y, z coordinates.
    Modify this function based on your PDB file format.
    """
    bead_1250_coordinates = []
    with open(pdb_file, 'r') as f:
        for line in f:
            if line.startswith('ATOM') or line.startswith('HETATM'):
                atom_name = line[12:16].strip()
                residue_id = int(line[22:26])
                x, y, z = float(line[30:38]), float(line[38:46]), float(line[46:54])
                if residue_id == 1250 and atom_name == 'CA':  # Assuming bead 1250 is represented by CA atom
                    bead_1250_coordinates.append((x, y, z))
    return np.array(bead_1250_coordinates)

def calculate_distances(coords1, coords2):
    """
    Calculates Euclidean distances between corresponding bead 1250 positions.
    """
    return np.linalg.norm(coords1 - coords2, axis=1)

def plot_histogram(distances):
    """
    Creates a histogram of distances.
    """
    plt.hist(distances, bins=20, edgecolor='black', alpha=0.7)
    plt.xlabel('Distance (Å)')
    plt.ylabel('Frequency')
    plt.title('Histogram of Distances between Bead 1250')
    plt.grid(True)
    plt.savefig('Histogram_of_distances_between_1250P_and_1250M.png')
    plt.show()

# Example usage
pdb_file1 = 'traj_0.pdb'
pdb_file2 = 'traj_1.pdb'

coords1 = read_coordinates_from_pdb(pdb_file1)
coords2 = read_coordinates_from_pdb(pdb_file2)

distances = calculate_distances(coords1, coords2)
plot_histogram(distances)

average = np.array([np.mean(distances)])
np.savetxt('average.txt',average)
