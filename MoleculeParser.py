from dataclasses import dataclass
from Chemistry import Atom

def parse_xyz_format(molecule_data):
    lines = molecule_data.strip().split('\n')
    num_atoms = int(lines[0].strip())
    atoms = []

    for i in range(2, num_atoms + 2):
        atom_info = lines[i].strip().split()
        if len(atom_info) < 4:
            continue
        atom = Atom(symbol = atom_info[0], position=[float(coord) for coord in atom_info[1:4]])
        atom_name = atom_info[0]
        atom_position = [float(coord) for coord in atom_info[1:4]]

        atoms.append(atom)

    return atoms

if __name__ == '__main__':
    di_atomic = """
        2
        Atoms. File written by MM. MMMMM
        C   -0.0000    0.0000    0.0000
        H   -0.0000    0.0000    1.0890
    """
    print(parse_xyz_format(di_atomic))