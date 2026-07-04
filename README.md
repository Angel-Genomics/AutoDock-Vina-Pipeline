#  Automated Protein-Ligand Docking Pipeline

A fully automated, Python-based pipeline for high-throughput Virtual Screening and Molecular Docking. This workflow streamlines the transition from raw `.pdb` files to fully analyzed and simulated docking poses.

##  Key Features

* **Automated Structure Preparation (`cleanpro.py`)**: Utilizes `BioPython` to clean raw protein structures, remove water molecules, and isolate specific chains.
* **Smart Active Site Mapping (`ligand.py` / `pdock.py`)**: Dynamically calculates the center of mass of native ligands to define precise Grid Box coordinates (X, Y, Z) for targeted docking.
* **Seamless Docking Execution (`vina.py`)**: Directly interfaces with `AutoDock Vina` using Python's `subprocess`, utilizing multi-threading for fast simulations and automatic log generation.
* **Bond Order Preservation**: Integrates `OpenBabel` to convert Vina's `.pdbqt` outputs into `.mol2` format, perfectly retaining structural integrity for 2D/3D interaction visualization.

##  Tech Stack

* **Language:** Python 3
* **Libraries:** BioPython, subprocess, os, math
* **Computational Tools:** AutoDock Vina 1.2, OpenBabel
* **Visualization:** BIOVIA Discovery Studio Visualizer

##  Sample Results

The pipeline successfully validated the binding pose of Tamoxifen against the Human Estrogen Receptor (PDB ID: 3ERT), achieving a stable binding affinity of **-9.8 kcal/mol** and predicting crucial hydrogen bonds (e.g., GLU:353).

> **Note:** To see the 2D interaction map generated from this pipeline's output, please refer to the `result_2D.png` file in this repository.
