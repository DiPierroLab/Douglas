# Extracts potential energy and radius of gyration from a MiChroM simulation log file.
# Usage: bash awk_pot_Rg.bash (run from the directory containing the .out file)
awk '/bl=/ {print substr( $8, 5, 5 )}' MiChroM_sim.out >> pot.txt
awk '/bl=/ {print substr( $9, 4, 6 )}' MiChroM_sim.out >> Rg.txt
