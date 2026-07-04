# Automated Protein-Ligand Docking Pipeline

A fully automated, Python-based pipeline designed for high-throughput Virtual Screening and Molecular Docking in Cellular and Molecular Biology research. This workflow streamlines the transition from raw `.pdb` files to fully analyzed and simulated docking poses.

## Key Features & Workflow

* **Automated Structure Preparation (`cleanpro.py`)**: Utilizes `Bio.PDB` (`PDBList`, `PDBParser`, `Select`, `PDBIO`) to automatically download structures, thoroughly clean raw proteins, remove water molecules/heteroatoms, and isolate specific target chains.
* **Smart Active Site Mapping (`ligand.py`)**: Employs `numpy` for coordinate matrix calculations and `Bio.PDB.NeighborSearch` to dynamically calculate the center of mass of native ligands. This defines precise Grid Box coordinates (X, Y, Z) for targeted docking without manual intervention.
* **Format Conversion & Optimization (`pdock.py`)**: Integrates `OpenBabel` via CLI to seamlessly convert `.pdb` structures into `.pdbqt` format for the receptor, and docking results into `.mol2` format to perfectly retain structural integrity and chemical bonds.
* **Seamless Docking Execution (`vina.py`)**: Directly interfaces with `AutoDock Vina` using Python's `subprocess` module, leveraging multi-threading for rapid simulations and automatic configuration/log generation.

## Tech Stack

* **Language:** Python 3
* **Bioinformatics Libraries:** `BioPython` (`Bio.PDB`)
* **Data Science Libraries:** `numpy`
* **Standard Python Libraries:** `subprocess`, `os`
* **Computational Engines:** AutoDock Vina 1.2, OpenBabel
* **Visualization:** BIOVIA Discovery Studio Visualizer

## Validation & Results

The pipeline successfully validated the binding pose of Tamoxifen (OHT) against the Human Estrogen Receptor (PDB ID: 3ERT). 
* **Binding Affinity:** Achieved a highly stable score of **-9.8 kcal/mol**.
* **Interactions:** Accurately predicted crucial hydrogen bonds (e.g., with GLU:353) inside the active site pocket.

> **Note:** Please refer to the `result_2D.png` file in this repository to view the high-resolution 2D ligand-protein interaction map generated from this pipeline's automated output.
