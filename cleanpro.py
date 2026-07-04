from Bio.PDB import PDBList, PDBParser, PDBIO, Select
class ProteinCleaner(Select):
    def __init__(self, target_chain):
        self.target_chain = target_chain
    def accept_chain(self, chain):
        if chain.get_id() == self.target_chain:
            return 1
        return 0
    def accept_residue(self, residue):
        if residue.id[0] == " ":
            return 1
        return 0
if __name__ == '__main__':
    pdb_id = "3ERT"
    target_chain = "A"
    downloaded_file = f"pdb{pdb_id.lower()}.ent" 
    output_file = f"{pdb_id}_clean.pdb"
    print(f"--- 1. Downloading {pdb_id} from PDB Server ---")
    pdbl = PDBList()
    pdbl.retrieve_pdb_file(pdb_id, pdir=".", file_format="pdb")
    print(f"\n--- 2. Cleaning {pdb_id} (Keeping Chain {target_chain}, Removing Water/Ligands) ---")
    parser = PDBParser(QUIET=True)
    try:
        structure = parser.get_structure(pdb_id, downloaded_file)
        io = PDBIO()
        io.set_structure(structure)
        io.save(output_file, ProteinCleaner(target_chain=target_chain))
        print(f"--- Success! Clean protein saved as '{output_file}' ---")
    except FileNotFoundError:
        print("Error: Download failed or file not found.")