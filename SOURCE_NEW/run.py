from poscar_i_o import *
from nrr import NRR
import numpy as np
import os


def lattice_inverse(poscar_data):
    lattice_vector_array=np.array(poscar_data["lattice_vectors"])
    #lattice_vector_array=np.transpose(lattice_vector_array)
    return(np.linalg.inv(lattice_vector_array))


poscar_data1 = read_poscar('POSCAR')


"""

        'comment': comment,
        'scaling_factor': scaling_factor,
        'lattice_vectors': lattice_vectors,
        'position_type' : position_type,
        'species_symbols': species_symbols,
        'num_atoms': num_atoms,
        'selective_dynamics': selective_dynamics,
        'positions': positions

        """



lattice_invers=lattice_inverse(poscar_data1)

def shift(positions0,lattice_inverse0,shift0,shift1):
    shift0=np.array(shift0)
    shift1=np.array(shift1)

    for position in positions0:
        pos = position[1]

        pos=np.array(pos)
  
        pos=np.add(pos,shift0)
 
        pos = lattice_inverse0.dot(pos)
        pos=np.add(pos,shift1)

        position[1]=pos.tolist()
    return(positions0)



path = os.getcwd() # get the current working directory
new_folder_path = os.path.join(path, "simulation")
os.mkdir(new_folder_path)
os.chdir(new_folder_path)

current_poscar=poscar_data1
values_positon = poscar_data1["positions"]

for name, positions in NRR.items():
    
    path = os.getcwd() # get the current working directory
    new_folder_path = os.path.join(path, name) # create the path for the new folder


    try:
        os.mkdir(new_folder_path) # create the new folder
        print(f"Successfully created folder {name} in {path}")
    except FileExistsError:
        print(f"Folder {name} already exists in {path}")
    except Exception as e:
        print(f"Error creating folder {name}: {e}")
    
    positions=shift(positions,lattice_invers,[0.0, 0.0, 2.0],[0.4999963812138326,  0.5000036187861676,  0.5841845913497856])



    current_poscar["positions"]=current_poscar["positions"] + positions
 
    species_position=species_positions(current_poscar)


    current_poscar["species_symbols"], current_poscar["num_atoms"] = species_number(species_position)
    write_poscar(new_folder_path+'/POSCAR', current_poscar)
    write_poscar(new_folder_path+'POSCAR.vasp', current_poscar)
    current_poscar["positions"] = values_positon
 

