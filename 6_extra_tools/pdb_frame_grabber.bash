#cp this to the directory in which the pdb files lie.

frame = 1999865 # number of the frame before the error 

file_0 = traj_0.pdb # pdb file 
x_frame_0 = $(egrep "MODEL.* $frame$" $file_0)
sed -n "/$x_frame_0/,/ENDMDL/p" $file > ${file_0::-4}_frame_$frame.pdb

file_1 = traj_1.pdb # pdb file 
x_frame_1 = $(egrep "MODEL.* $frame$" $file_1)
sed -n "/$x_frame_1/,/ENDMDL/p" $file > ${file::-4}_frame_$frame.pdb
