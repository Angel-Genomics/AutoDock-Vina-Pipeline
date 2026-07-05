import numpy as np
from Bio.PDB import PDBList, PDBParser, PDBIO, Select, Selection, NeighborSearch
class LigandSelector(Select):
    def __init__(self, ligand_name):
        self.ligand_name = ligand_name
    def accept_residue(self, residue):
        if residue.resname == self.ligand_name:
            return 1
        return 0
if __name__ == '__main__':
    pdb_id = "3ERT"
    ligand_name = "OHT"  
    chain_id = "A"
    print(f"--- 1. Downloading {pdb_id} ---")
    pdbl = PDBList()
    pdbl.retrieve_pdb_file(pdb_id, pdir=".", file_format="pdb")
    downloaded_file = f"pdb{pdb_id.lower()}.ent"
    print(f"\n--- 2. Parsing Structure ---")
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure(pdb_id, downloaded_file)
    model = structure[0]
    chain = model[chain_id]
    ligand_atoms = []
    for residue in chain:
        if residue.resname == ligand_name:
            ligand_atoms.extend(residue.get_atoms())
    if not ligand_atoms:
        print(f"Error: Ligand {ligand_name} not found in Chain {chain_id}!")
    else:
        coords = np.array([atom.get_coord() for atom in ligand_atoms])
        center = coords.mean(axis=0)
        print(f"\n✅ --- Grid Box Coordinates (Center of Mass) ---")
        print(f"X: {center[0]:.3f} | Y: {center[1]:.3f} | Z: {center[2]:.3f}")
        all_atoms = Selection.unfold_entities(chain, 'A')
        ns = NeighborSearch(all_atoms)
        interacting_residues = set()
        for atom in ligand_atoms:
            neighbors = ns.search(atom.get_coord(), 5.0, level='R')
            for res in neighbors:
                if res.resname != ligand_name and res.id[0] == " ":
                    interacting_residues.add(res)
        print(f"\n✅ --- Active Site Residues (5 Å Radius) ---")
        for res in sorted(interacting_residues, key=lambda x: x.id[1]):
            print(f"{res.resname} {res.id[1]}")
        io = PDBIO()
        io.set_structure(structure)
        io.save(f"{ligand_name}_ligand.pdb", LigandSelector(ligand_name))
        print(f"\n✅ --- Ligand File Saved: {ligand_name}_ligand.pdb ---")