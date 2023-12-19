awk '/bl=/ {print substr( $8, 5, 5 )}' MiChroM_sim_from_initial_structure.out >> pot.txt
awk '/bl=/ {print substr( $9, 4, 6 )}' MiChroM_sim_from_initial_structure.out >> Rg.txt
