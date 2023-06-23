from MoleculeParser import File_2_obmol, Get_bonds, Get_atoms
from SceneGenerator import generate_3d_model_file

def Render_molecule(in_filename: str):
    out_filename = '3d_model.html'
    mol = File_2_obmol(in_filename)
    atoms = Get_atoms(mol)
    return generate_3d_model_file(atoms, out_filename)

if __name__ == '__main__':
    in_filename = 'H2O.xyz'
    print(Render_molecule(in_filename))
