from poscar_i_o import *
from HER import molecules
import numpy as np
import os
import copy

import sys 

if len(sys.argv) != 4:
    print("Please provide two numbers as command line arguments.")
else:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    num3 = float(sys.argv[3])

    print(f"First number: {num1}")
    print(f"Second number: {num2}")
    print(f"Third number: {num3}")


def lattice_inverse(poscar_data):
    lattice_vector_array = np.array(poscar_data["lattice_vectors"])    
    return np.linalg.inv(lattice_vector_array)


poscar_data1 = read_poscar("POSCAR")


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

lattice_invers = lattice_inverse(poscar_data1)


def shift(positions0, lattice_inverse0, shift0=[0,0,0], shift1=[0,0,0]):
    print(positions0)
    shift0 = np.array(shift0)
    shift1 = np.array(shift1)

    for position in positions0:
        pos = position[1]

        pos = np.array(pos)

        pos = np.add(pos, shift0)

        pos = lattice_inverse0.dot(pos)
        pos = np.add(pos, shift1)

        position[1] = pos.tolist()

    return positions0

def counter(positions_counter):
    count_name=[]
    count_num=[]
    for posi in positions_counter:
        if posi[0] not in count_name:
            count_name.append(posi[0])
            count_num.append(0)
        for i,name in enumerate(count_name):
            if posi[0] is name:
                count_num[i]+=1
    

    return (count_name,count_num)

path = os.getcwd()  # get the current working directory
new_folder_path = os.path.join(path, "simulation")
os.mkdir(new_folder_path)
os.chdir(new_folder_path)


def different_Site(molecules,poscar_data1,site):
    site_name=site[0]
    site_position=site[1]
    c_shift=site[2]*site[3]
    for name, positions in molecules.items():
        name=site_name+"-"+name

        current_poscar = copy.deepcopy(poscar_data1)
        path = os.getcwd()  # get the current working directory
        new_folder_path = os.path.join(path, name)  # create the path for the new folder

        try:
            os.mkdir(new_folder_path)  # create the new folder
            print(f"Successfully created folder {name} in {path}")
        except FileExistsError:
            print(f"Folder {name} already exists in {path}")
        except Exception as e:
            print(f"Error creating folder {name}: {e}")
        
        positions_0 = copy.deepcopy(positions)

        if site[3] is -1:
            positions = shift(positions_0,np.array([[1, 0, 0],[0,1,0],[0,0,-1]]))

        positions = shift(
            positions_0,
            lattice_invers,
            [0,0,c_shift],
            site_position,
        )

        species_name, species_num=counter(positions)

        current_poscar["positions"] = current_poscar["positions"] + positions

        species_position = species_positions(current_poscar)
        current_poscar["species_symbols"]+=species_name
        current_poscar["num_atoms"]+=species_num
        print(  f'Atoms {current_poscar["species_symbols"]}, numbers {current_poscar["num_atoms"]} \n\n')

        write_poscar(new_folder_path + "/POSCAR", current_poscar)
        write_poscar(new_folder_path + ".POSCAR.vasp", current_poscar)
    return


sitedata = [
["HER",[num1,num2,num3],1.00,1],
]

for site_adsor in sitedata:
    different_Site(molecules,poscar_data1,site_adsor)


