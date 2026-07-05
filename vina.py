import subprocess
import os
def run_docking():
    print("--- 1. Generating Vina Configuration File ---")
    config_content = """receptor = receptor.pdbqt
ligand = ligand.pdbqt
center_x = 30.012
center_y = -1.913
center_z = 24.207
size_x = 20
size_y = 20
size_z = 20
exhaustiveness = 8
cpu = 10
"""
    with open("config.txt", "w") as f:
        f.write(config_content)
    print(" config.txt created successfully.")
    print("\n--- 2. Executing AutoDock Vina ---")
    print(" Firing up the simulation... (Utilizing 10 CPU Threads)")
    cmd = [
        "vina", 
        "--config", "config.txt", 
        "--out", "docking_results.pdbqt"
    ]
    with open("docking_log.txt", "w") as log_file:
        process = subprocess.run(cmd, stdout=log_file, stderr=subprocess.STDOUT)
    if process.returncode == 0 and os.path.exists("docking_results.pdbqt"):
        print("\n Docking Complete!")
        print("Results are saved in:")
        print(" - Poses: docking_results.pdbqt")
        print(" - Energies: docking_log.txt")
    else:
        print("\n Error: Docking failed. Make sure 'vina' is installed and accessible in the terminal.")
if __name__ == '__main__':
    if os.path.exists("receptor.pdbqt") and os.path.exists("ligand.pdbqt"):
        run_docking()
    else:
        print("Error: receptor.pdbqt or ligand.pdbqt not found! Did you run the preparation script?")
