def parse_xyz_format(molecule_data):
    lines = molecule_data.strip().split('\n')
    atom_count = int(lines[0].strip())
    atoms = []

    for i in range(2, atom_count + 2):
        atom_info = lines[i].strip().split()
        if len(atom_info) < 4:
            continue
        atom_name = atom_info[0]
        atom_position = [float(coord) for coord in atom_info[1:4]]

        atoms.append({
            'name': atom_name,
            'position': atom_position
        })

    return atoms