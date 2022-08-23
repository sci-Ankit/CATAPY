"""
Intension of the file is to be able to read and write POSCAR file, with latter as a tool expanded to handle other file formats too
---

Information about the POSCAR file is taken from VASP wiki
and as much features as possible are tried to be implemented

## Current Features
1. Handling direct and absolute coordinates, hence data from POSCAR and CONTCAR
2. 


Future Handling
1. Selective Dynamics



### General information
The program is hand coded to read as per the standard given by the vasp team. flexibility is given only for things specially mentioned in the main wiki and nothing else is been considered

1. ln1 - First line is comment
2. ln2 - scaling factor
3. ln3, ln4, ln5 - Lattice vectors
4. This is optional line Species name 


"""
import numpy as np

def head_reader(file): ## this code reads the bare poscar, list of tuple with all adsorbate and there qty
    f = open(file,"r")

    poscar_title = f.readline().strip()
    poscar_scale=list(map(float,f.readline().split()))
    poscar_lattice = np.zeros([3,3])
    for i in range(3):
        poscar_lattice[i] = list(map(float, f.readline().split()))
    tmp = f.readline().split()
    print(tmp)
    if tmp[0].isalpha():
        print("run")
        atoms_symbols = tmp
        print(atoms_symbols)
        tmp = f.readline().split()
    atoms_num = tmp
    print(atoms_num)


    f.close()
    return (0)


"""
everything below this has to be removed
"""

head_reader("/media/sf_Shared/Github_new/CATAPY/examples/hepo_1/POSCAR")