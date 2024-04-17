#Make a histogram of distances between corresponding loci (running average over all corresponding pairs of loci)
#Written by Microsoft Copilot; edited by Douglas

# Load the two trajectory files
mol new traj_0.pdb
mol new traj_1.pdb

# Set the bead selection (you may need to adjust this based on your system)
set bead_selection "name CA"

# Initialize an empty list to store distances
set distances {}

# Iterate over bead indices
for {set i 1} {$i <= 2500} {incr i} {
    # Compute the distance between bead i in traj_0.pdb and traj_1.pdb
        set dist [measure bond $bead_selection [atomselect 0 "index $i"] [atomselect 1 "index $i"]]
            lappend distances $dist
            }

            # Create a histogram of distances
            set num_bins 50
            set hist [histogram $distances $num_bins]

            # Save the histogram data to a file
            set output_file "histogram_data.txt"
            set file_id [open $output_file w]
            puts $file_id "Distance (Angstroms) Frequency"
            foreach {bin freq} $hist {
                puts $file_id "$bin $freq"
                }
                close $file_id

                puts "Histogram data saved to $output_file"
                
