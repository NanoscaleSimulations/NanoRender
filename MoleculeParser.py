from dataclasses import dataclass
from Chemistry import Atom
from openbabel import openbabel
from typing import List

def parse_xyz_format(molecule_data):
    print('This function should be removed soon at it is not intended for use anymore')
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

def File_2_obmol(filename: str) -> openbabel.OBMol:
    mol = openbabel.OBMol()
    conv = openbabel.OBConversion()
    file_extension = filename.split('.')[-1]
    file_data = open(filename, 'r')
    if conv.SetInFormat(file_extension) == False:
        print('File format is not supported')
    conv.ReadString(mol, file_data.read())
    file_data.close()
    return mol

def Get_atoms(mol: openbabel.OBMol) -> List[openbabel.OBAtom]:
    return [atom for atom in openbabel.OBMolAtomIter(mol)]

def Get_bonds(mol: openbabel.OBMol) -> List[openbabel.OBBond]:
    return [bond for bond in openbabel.OBMolBondIter(mol)]

if __name__ == '__main__':
    filename = 'H2O.xyz'
    mol = File_2_obmol(filename)
    print(mol.NumAtoms() == 3)
    atoms = Get_atoms(mol)
    print(len(atoms) == 3)
    bonds = Get_bonds(mol)
    print(len(bonds) == 2)