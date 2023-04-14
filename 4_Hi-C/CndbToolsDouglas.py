# Copyright (c) 2020-2021 The Center for Theoretical Biological Physics (CTBP) - Rice University
# This file is from the Open-MiChroM project, released under the MIT License.
# This file was edited by Douglas with the Douglas Foundation for Computational Theoretical Physical Super Genetics.

R"""
The :class:`~.cndbTools` class perform analysis from **cndb** or **ndb** - (Nucleome Data Bank) file format for storing an ensemble of chromosomal 3D structures.
Details about the NDB/CNDB file format can be found at the `Nucleome Data Bank <https://ndb.rice.edu/ndb-format>`__.
"""

import h5py
import numpy as np
import os
from scipy.spatial import distance

class cndbTools:
#=================================================================================================
    def __init__(self):
        self.Type_conversion = {'A1':0, 'A2':1, 'B1':2, 'B2':3,'B3':4,'B4':5, 'NA' :6}
        self.Type_conversionInv = {y:x for x,y in self.Type_conversion.items()}
#=================================================================================================
    def load(self, filename1,filename2):
        R"""
        Receives the path to **cndb** or **ndb** file to perform analysis.
        
        Args:
            filename1 (file, required):
                Path to cndb or ndb file. If an ndb file is given, it is converted to a cndb file and saved in the same directory.
        """
        f1_name, file1_extension = os.path.splitext(filename1)
        f2_name, file2_extension = os.path.splitext(filename2)
        
        if file1_extension == ".ndb":
            filename1 = self.ndb2cndb(f1_name)
            
        if file2_extension == ".ndb":
            filename2 = self.ndb2cndb(f2_name)

        self.cndb1 = h5py.File(filename1, 'r')
        self.cndb2 = h5py.File(filename2, 'r')
        
        self.ChromSeq_numbers1 = np.array(self.cndb1['types'])
        self.ChromSeq_numbers2 = np.array(self.cndb2['types'])
        
        #self.ChromSeq1 = [self.Type_conversionInv[x] for x in self.ChromSeq_numbers1]
        #self.ChromSeq2 = [self.Type_conversionInv[x] for x in self.ChromSeq_numbers2]
        
        self.ChromSeq1 = [x.decode('utf-8') for x in self.ChromSeq_numbers1]
        self.ChromSeq2 = [x.decode('utf-8') for x in self.ChromSeq_numbers2]
        
        self.uniqueChromSeq1 = set(self.ChromSeq1)
        self.uniqueChromSeq2 = set(self.ChromSeq2)
        
        self.dictChromSeq1 = {}
        self.dictChromSeq2 = {}
        
        for tt in self.uniqueChromSeq1:
            self.dictChromSeq1[tt] = ([i for i, e in enumerate(self.ChromSeq1) if e == tt])
        for tt in self.uniqueChromSeq2:
            self.dictChromSeq2[tt] = ([i for i, e in enumerate(self.ChromSeq2) if e == tt])
        
        self.Nbeads1 = len(self.ChromSeq_numbers1)
        self.Nbeads2 = len(self.ChromSeq_numbers2)
        self.Nframes = len(self.cndb1.keys()) -1
        
        return(self)
#==============================================================================
    def xyz1(self, frames=[1,None,1], beadSelection='all', XYZ=[0,1,2]):
        R"""
        Get the selected beads' 3D position from a **cndb** or **ndb** for multiple frames.
        
        Args:
            frames (list, required):
                Define the range of frames that the position of the bead will get extracted. The range list is defined by :code:`frames=[initial, final, step]`. (Default value = :code: `[1,None,1]`, all frames)
            beadSelection (list of ints, required):
                List of beads to extract the 3D position for each frame. The list is defined by :code: `beadSelection=[1,2,3...N]`. (Default value = :code: `'all'`, all beads) 
            XYZ (list, required):
                List of the axis in the Cartesian coordinate system that the position of the bead will get extracted for each frame. The list is defined by :code: `XYZ=[0,1,2]`. where 0, 1 and 2 are the axis X, Y and Z, respectively. (Default value = :code: `XYZ=[0,1,2]`) 
    
        Returns:
            :math:`(frames, beadSelection, XYZ)` :class:`numpy.ndarray`:
                Returns an array of the 3D position of the selected beads for different frames.
        """
        frame_list1 = []
        
        if beadSelection == 'all':
            selection = np.arange(self.Nbeads1)
        else:
            selection = np.array(beadSelection)
            
        if frames[1] == None:
            frames[1] = self.Nframes
        
        for i in range(frames[0],frames[1],frames[2]):
            frame_list1.append(np.take(np.take(np.array(self.cndb1[str(i)]), selection, axis=0), XYZ, axis=1))
        return(np.array(frame_list1))
#------------------------------------------------------------------------------    
    def xyz2(self, frames=[1,None,1], beadSelection='all', XYZ=[0,1,2]):
        
        frame_list2 = []
        
        if beadSelection == 'all':
            selection = np.arange(self.Nbeads2)
        else:
            selection = np.array(beadSelection)
            
        if frames[1] == None:
            frames[1] = self.Nframes
        
        for i in range(frames[0],frames[1],frames[2]):
            frame_list2.append(np.take(np.take(np.array(self.cndb2[str(i)]), selection, axis=0), XYZ, axis=1))
        return(np.array(frame_list2))
#=========================================================================================
    def calc_prob(self,data1,data2, mu, rc):
        return 0.5 * (1.0 + np.tanh(mu * (rc - distance.cdist(data1, data2, 'euclidean'))))
#-------------------------------------------------------------------------------
    def traj2HiC12(self, xyz1, xyz2, mu=3.22, rc = 1.78):

        size1 = len(xyz1[0])
        size2 = len(xyz2[0])
        P12 = np.zeros((size1, size2)) #size1=rows size2=columns
        Ntotal = 0
        
        for i in range(len(xyz2)):
            data1 = xyz1[i]
            data2 = xyz2[i]
            P12 += self.calc_prob(data1,data2, mu, rc)
            Ntotal += 1
            if i % 500 == 0:
                print("Reading frame {:} of {:}".format(i, len(xyz2)))
        
        return(np.divide(P12 , Ntotal)) #np.divide is elementwise division 

#----------------------------------------------------------
    def traj2HiC(self, xyz1, xyz2):
        size1 = len(xyz1[0])
        size2 = len(xyz2[0])
        
        P = np.zeros((size1+size2, size1+size2))
        P11 = self.traj2HiC12(xyz1,xyz1)
        P12 = self.traj2HiC12(xyz1,xyz2)
        P21 = np.transpose(P12)
        P22 = self.traj2HiC12(xyz2,xyz2)
        P[0:size1,0:size1] = P11
        P[size1:size1+size2,0:size1] = P21
        P[0:size1,size1:size1+size2] = P12
        P[size1:size1+size2,size1:size1+size2] = P22
        
        return(P)
#================================================================        
    def ndb2cndb(self, filename1):
        R"""
        Converts an **ndb** file format to **cndb**.
        
        Args:
            filename (path, required):
                 Path to the ndb file to be converted to cndb.
        """
        Main_chrom      = ['ChrA','ChrB','ChrU'] # Type A B and Unknow
        Chrom_types     = ['ZA','OA','FB','SB','TB','LB','UN']
        Chrom_types_NDB = ['A1','A2','B1','B2','B3','B4','UN']
        Res_types_PDB   = ['ASP', 'GLU', 'ARG', 'LYS', 'HIS', 'HIS', 'GLY']
        Type_conversion = {'A1': 0,'A2' : 1,'B1' : 2,'B2' : 3,'B3' : 4,'B4' : 5,'UN' : 6}
        title_options = ['HEADER','OBSLTE','TITLE ','SPLT  ','CAVEAT','COMPND','SOURCE','KEYWDS','EXPDTA','NUMMDL','MDLTYP','AUTHOR','REVDAT','SPRSDE','JRNL  ','REMARK']
        model          = "MODEL     {0:4d}"
        atom           = "ATOM  {0:5d} {1:^4s}{2:1s}{3:3s} {4:1s}{5:4d}{6:1s}   {7:8.3f}{8:8.3f}{9:8.3f}{10:6.2f}{11:6.2f}          {12:>2s}{13:2s}"
        ter            = "TER   {0:5d}      {1:3s} {2:1s}{3:4d}{4:1s}"

        file_ndb = filename + str(".ndb")
        name     = filename + str(".cndb")

        cndbf = h5py.File(name, 'w')
        
        ndbfile = open(file_ndb, "r")
        
        loop = 0
        types = []
        types_bool = True
        loop_list = []
        x = []
        y = [] 
        z = []

        frame = 0

        for line in ndbfile:
    
            entry = line[0:6]

            info = line.split()


            if 'MODEL' in entry:
                frame += 1

                inModel = True

            elif 'CHROM' in entry:

                subtype = line[16:18]

                types.append(subtype)
                x.append(float(line[40:48]))
                y.append(float(line[49:57]))
                z.append(float(line[58:66]))

            elif 'ENDMDL' in entry:
                if types_bool:
                    typelist = [Type_conversion[x] for x in types]
                    cndbf['types'] = typelist
                    types_bool = False

                positions = np.vstack([x,y,z]).T
                cndbf[str(frame)] = positions
                x = []
                y = []
                z = []

            elif 'LOOPS' in entry:
                loop_list.append([int(info[1]), int(info[2])])
                loop += 1
        
        if loop > 0:
            cndbf['loops'] = loop_list

        cndbf.close()
        return(name)

    
#########################################################################################
#### Analisys start here!
#########################################################################################

    def compute_Chirality(self,xyz,neig_beads=4):
        R"""
        Calculates the Chirality parameter :math:`\Psi`. Details are decribed in "Zhang, B. and Wolynes, P.G., 2016. Shape transitions and chiral symmetry breaking in the energy landscape of the mitotic chromosome. Physical review letters, 116(24), p.248101."
        
        Args:
            xyz (:math:`(frames, beadSelection, XYZ)` :class:`numpy.ndarray`, required):
                Array of the 3D position of the selected beads for different frames extracted by using the :code: `xyz()` function.
            neig_beads (int, required):
                Number of neighbor beads to consider in the calculation (Default value = 4).  
                       
        Returns:
            :class:`numpy.ndarray`:
                Returns the Chirality parameter :math:`\Psi` for each bead.
        """
        Psi=[]
        for frame in range(len(xyz)):
            XYZ = xyz[frame]
            Psi_per_bead=[]
            for i in range(0,np.shape(xyz)[0] - np.ceil(1.25*neig_beads).astype('int')):
                a=i
                b=np.int(np.round(i+0.5*neig_beads))
                c=np.int(np.round(i+0.75*neig_beads))
                d=np.int(np.round(i+1.25*neig_beads))

                AB = XYZ[b]-XYZ[a]
                CD = XYZ[d]-XYZ[c]
                E = (XYZ[b]-XYZ[a])/2.0 + XYZ[a]
                F = (XYZ[d]-XYZ[c])/2.0 + XYZ[c]
                Psi_per_bead.append(np.dot((F-E),np.cross(CD,AB))/(np.linalg.norm(F-E)*np.linalg.norm(AB)*np.linalg.norm(CD)))
            Psi.append(Psi_per_bead)
            
        return np.asarray(Psi)



    def compute_RG(self,xyz): 
        R"""
        Calculates the Radius of Gyration. 
        
        Args:
            xyz (:math:`(frames, beadSelection, XYZ)` :class:`numpy.ndarray`, required):
                Array of the 3D position of the selected beads for different frames extracted by using the :code: `xyz()` function.  
                       
        Returns:
            :class:`numpy.ndarray`:
                Returns the Radius of Gyration in units of :math:`\sigma`.
        """
        rg = []
        for frame in range(len(xyz)):
            data = xyz[frame]
            data = data - np.mean(data, axis=0)[None,:]
            rg.append(np.sqrt(np.sum(np.var(np.array(data), 0))))
        return np.array(rg) 
        
    def compute_RDP(self, xyz, radius=20.0, bins=200):
        R"""
        Calculates the RDP - Radial Distribution Probability. Details can be found in the following publications: 
        
            - Oliveira Jr., A.B., Contessoto, V.G., Mello, M.F. and Onuchic, J.N., 2021. A scalable computational approach for simulating complexes of multiple chromosomes. Journal of Molecular Biology, 433(6), p.166700.
            - Di Pierro, M., Zhang, B., Aiden, E.L., Wolynes, P.G. and Onuchic, J.N., 2016. Transferable model for chromosome architecture. Proceedings of the National Academy of Sciences, 113(43), pp.12168-12173.
        
        Args:
            xyz (:math:`(frames, beadSelection, XYZ)` :class:`numpy.ndarray`, required):
                Array of the 3D position of the selected beads for different frames extracted by using the :code: `xyz()` function. 
            radius (float, required):
                Radius of the sphere in units of :math:`\sigma` to be considered in the calculations. The radius value should be modified depending on your simulated chromosome length. (Default value = 20.0).
            bins (int, required):
                Number of slices to be considered as spherical shells. (Default value = 200).
                       
        Returns:
            :math:`(N, 1)` :class:`numpy.ndarray`:
                Returns the radius of each spherical shell in units of :math:`\sigma`.
            :math:`(N, 1)` :class:`numpy.ndarray`:
                Returns the RDP - Radial Distribution Probability for each spherical shell.
        """
        
        def calcDist(a,b):
            R"""
            Internal function that calculates the distance between two beads. 
            """
            return np.sqrt( (a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2  )
        
        def calc_gr(ref, pos, R, dr):
            R"""
            Internal function that calculates the distance RDP - Radial Distribution Probability. 
            """
            g_r =  np.zeros(int(R/dr))
            dd = []
            for i in range(len(pos)):
                dd.append(calcDist(pos[i],ref))
            raddi =dr
            k = 0
            while (raddi <= R):
                for i in range(0,len(pos)):
                    if (dd[i] >= raddi and dd[i] < raddi+dr):
                        g_r[k] += 1

                g_r[k] = g_r[k]/(4*np.pi*dr*raddi**2)
                raddi += dr
                k += 1
            return g_r 
        
        R_nucleus = radius
        deltaR = R_nucleus/bins                  
   
        n_frames = 0 
        g_rdf = np.zeros(bins)
 
        for i in range(len(xyz)):
            frame = xyz[i]
            centroide = np.mean(frame, axis=0)[None,:][0]
            n_frames += 1
            g_rdf += calc_gr(centroide, frame, R_nucleus, deltaR)
        
        Rx = []   
        for i in np.arange(0, int(R_nucleus+deltaR), deltaR):
            Rx.append(i)
        return(Rx, g_rdf/n_frames) 
            
        
    def __repr__(self):
        return '<{0}.{1} object at {2}>\nCndb file has {3} frames, with {4} beads and {5} types '.format(
      self.__module__, type(self).__name__, hex(id(self)), self.Nframes, self.Nbeads, self.uniqueChromSeq)