#!/usr/bin/env python3

############################################
imp_file = "coors.dat"
out_file1 = "coordMR.dat"
out_file2 = "velocMR.dat"
out_file3 = "forceMR.dat"
############################################

#reading the imput file and skipping first 5 lines that are not important
with open (imp_file, "r") as f:
  
   lines_after_5 = f.readlines()[5:]

#determining the number of atoms (9N + 2) and preparing output files separation for each time step (iteration)
   for line in lines_after_5:
      l = line.split()
      num_atoms = int((len(l) - 2)/9)
      with open (out_file1, "a") as f:
         f.write(str(num_atoms) + "\n")
         f.write(str(l[0]) + " " + str(l[1]) + "\n")
      with open (out_file2, "a") as f:
         f.write(str(num_atoms) + "\n")
         f.write(str(l[0]) + " " + str(l[1]) + "\n")
      with open (out_file3, "a") as f:
         f.write(str(num_atoms) + "\n")
         f.write(str(l[0]) + " " + str(l[1]) + "\n")
      

#dividing line into 3 parts = coordinates (conversion into angstroms), velocities, forces
      for i in range(1, num_atoms+1):
         coord_i = [float(l[3*i-1])/0.52917720859, float(l[3*i])/0.52917720859, float(l[3*i+1])/0.52917720859]
         with open (out_file1, "a") as f:
            f.write(str(coord_i[0]) + " " + str(coord_i[1]) + " " + str(coord_i[2]) + "\n")
         
         veloc_i = [l[3*i+17], l[3*i+18], l[3*i+19]]
         with open (out_file2, "a") as f:
            f.write(str(veloc_i[0]) + " " + str(veloc_i[1]) + " " + str(veloc_i[2]) + "\n")

         force_i = [l[3*i+35], l[3*i+36], l[3*i+37]]
         with open (out_file3, "a") as f:
            f.write(str(force_i[0]) + " " + str(force_i[1]) + " " + str(force_i[2]) + "\n")


