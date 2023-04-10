import random

# Assuming you want to modify the species in the 2nd index to be represented by Ni and Fe:
species_symbols = ['Ni', 'Fe', 'Cr']
num_atoms = [5, 10, 5]

# Generate positions for Ni atoms
ni_positions = []
for i in range(num_atoms[0]):
    position = [species_symbols[0], [random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)], ['T', 'T', 'T']]
    ni_positions.append(position)

# Generate positions for Fe atoms
fe_positions = []
for i in range(num_atoms[1]):
    position = [species_symbols[1], [random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)], ['T', 'T', 'T']]
    fe_positions.append(position)

# Merge the positions for Ni and Fe atoms
all_positions = ni_positions + fe_positions + [['Cr', [random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)], ['T', 'T', 'T']] * num_atoms[2]

# Shuffle the positions list to randomize the order of atoms
random.shuffle(all_positions)

# Combine the species_symbols and num_atoms lists to create the final poscar_data dictionary
poscar_data = {
    'comment': 'My POSCAR file',
    'scaling_factor': 1.0,
    'lattice_vectors': [[10.0, 0.0, 0.0], [0.0, 10.0, 0.0], [0.0, 0.0, 10.0]],
    'species_symbols': ['Ni', 'Fe', 'Cr'],
    'num_atoms': [len(ni_positions), len(fe_positions), num_atoms[2]],
    'selective_dynamics': False,
    'positions': all_positions
}
In this example, the species_symbols list is initially ['Ni', 'Fe', 'Cr'] and the num_atoms list is [5, 10, 5], indicating that there are 5 Ni atoms, 10 Fe atoms, and 5 Cr atoms. The code generates random positions for the Ni and Fe atoms and then combines them into a single all_positions list, with the remaining positions being generated for Cr atoms. Finally, the species_symbols and num_atoms lists are combined with the all_positions list to create the poscar_data dictionary.





