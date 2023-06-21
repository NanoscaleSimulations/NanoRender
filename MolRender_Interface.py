from .MoleculeParser import parse_xyz_format
from .SceneGenerator import generate_3d_model_file

def Render_molecule(molecule: str):
    filename = '3d_model.html'
    scene_data = parse_xyz_format(molecule)
    return generate_3d_model_file(scene_data, filename)

if __name__ == '__main__':
    molecule = """
    4
    Atoms. File written by MM. MMMMM
    C   -0.0000    0.0000    0.0000
    H   -0.0000    0.0000    1.0890
    H    1.0267    0.0000   -0.3630
    H   -0.5133   -0.8892   -0.3630
    """
    print(Render_molecule(molecule))