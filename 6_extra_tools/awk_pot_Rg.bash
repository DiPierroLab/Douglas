awk '/bl=/ {print substr( $8, 5, 5 ) "\t" substr( $9, 4, 6 )}' MiChroM_sim.out > pot_Rg.txt
