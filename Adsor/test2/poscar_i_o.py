import random


def read_poscar(file_path):
    with open(file_path, "r") as f:
        # Read the first six lines (top section) of the POSCAR file
        comment = f.readline().strip()
        scaling_factor = float(f.readline())
        lattice_vectors = []
        for i in range(3):
            lattice_vectors.append(list(map(float, f.readline().split())))
        species_symbols = f.readline().split()
        num_atoms = list(map(int, f.readline().split()))

        # Read the selective dynamics flag, if it exists
        selective_dynamics = False
        line = f.readline().strip()
        if line.lower().startswith("s"):
            selective_dynamics = True
            line = f.readline().strip()

        # Type
        position_type = ""
        if line.lower().startswith("d"):
            position_type = "Direct"
        elif line.lower().startswith("c"):
            position_type = "Cartesian"
        else:
            print("Position type can be only direct or cartesian")
            return ()

        # Read the atomic positions
        positions = []
        j = 0
        k = 0
        species = species_symbols[k]
        for i in range(sum(num_atoms)):
            line = f.readline().split()
            position = list(map(float, line[:3]))
            if j == num_atoms[k]:
                j = 0
                k += 1
                species = species_symbols[k]
            dynamics = line[3:] if selective_dynamics else None
            positions.append([species, position, dynamics])
            j += 1
        if species_symbols[0]=="0":
            species_symbols=[]
            num_atoms=[]
        

    return {
        "comment": comment,
        "scaling_factor": scaling_factor,
        "lattice_vectors": lattice_vectors,
        "position_type": position_type,
        "species_symbols": species_symbols,
        "num_atoms": num_atoms,
        "selective_dynamics": selective_dynamics,
        "positions": positions,
    }


def write_poscar(file_path, poscar_data):
    with open(file_path, "w") as f:
        # Write the top section of the POSCAR file
        f.write(poscar_data["comment"] + "\n")
        f.write(str(poscar_data["scaling_factor"]) + "\n")
        for v in poscar_data["lattice_vectors"]:
            f.write(" ".join(map(str, v)) + "\n")
        f.write(" ".join(poscar_data["species_symbols"]) + "\n")
        f.write(" ".join(map(str, poscar_data["num_atoms"])) + "\n")

        # Write the selective dynamics flag, if applicable
        if poscar_data["selective_dynamics"]:
            f.write("Selective dynamics\n")

        # position type
        f.write(poscar_data["position_type"] + "\n")

        # Write the atomic positions
        for atom in poscar_data["positions"]:
            species = atom[0]
            position = atom[1]
            dynamics = atom[2]
            line = " ".join(map(str, position))
            if poscar_data["selective_dynamics"]:
                line += " " + " ".join(dynamics)
            f.write(line + "\n")


def shuffle_poscar(poscar_data):
    random.shuffle(poscar_data["positions"])
    return poscar_data


def species_positions(poscar_data):
    positions = poscar_data["positions"]
    species_positions = {}

    for species in set([p[0] for p in positions]):
        species_positions[species] = []

    # Loop over each position and add it to the corresponding sublist
    for position in positions:
        species_positions[position[0]].append([position[0], position[1], position[2]])

    return species_positions


def species_number(species_position):
    species_jugaad = ['Mo', 'S', 'Ni', 'N', 'H']
    species_symbols = []
    num_atoms = []
    for species in species_jugaad:
        if species in species_position:
            species_symbols.append(species)
            num_atoms.append(len(species_position[species]))
        else:
            continue

    return (species_symbols, num_atoms)
