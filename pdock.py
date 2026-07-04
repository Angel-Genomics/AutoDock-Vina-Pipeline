import subprocess
import os
def convert_to_pdbqt(input_pdb, output_pdbqt, is_receptor=True):
    if not os.path.exists(input_pdb):
        print(f"Error: {input_pdb} not found!")
        return
    if is_receptor:
        cmd = ["obabel", input_pdb, "-O", output_pdbqt, "-h", "-xr"]
    else:
        cmd = ["obabel", input_pdb, "-O", output_pdbqt, "-h"]
    print(f"Converting {input_pdb} to {output_pdbqt}...")
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.path.exists(output_pdbqt):
        print(f"✅ Success: {output_pdbqt} created.")
    else:
        print(f"❌ Failed to create {output_pdbqt}.")
if __name__ == '__main__':
    print("--- Starting Format Conversion for AutoDock Vina ---")
    convert_to_pdbqt("3ERT_clean.pdb", "receptor.pdbqt", is_receptor=True)
    convert_to_pdbqt("OHT_ligand.pdb", "ligand.pdbqt", is_receptor=False)
    print("\nAll files are ready for docking!")