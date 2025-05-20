#!/bin/bash -l
#
# SBATCH directives
#
# (1) Account to charge
#SBATCH -A naiss2025-22-683   # ← replace with your project/allocation
#
# (2) Job name
#SBATCH -J iqtree_supermatrix
#
# (3) Partition (queue)
#SBATCH -p main
#
# (4) Wall-time (HH:MM:SS)
#SBATCH -t 24:00:00
#
# (5) Resources: here we use 1 node, 1 task, and 10 threads
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=128
#
# (6) Output files
#SBATCH -o supermatrix.%j.out
#SBATCH -e supermatrix.%j.err

# ============ Your commands start here ============

# Load the IQ‐TREE2 module that PDC provides
ml load PDC iqtree

# Move into the directory where your SUPERMATRIX.fasta lives
cd /cfs/klemming/home/a/aescos/Private

# Run IQ‐TREE2 with 10 threads, ModelFinder+MERGE, and prefix “supermatrix”
srun iqtree2 \
     -s SUPERMATRIX.fasta \
     -m MFP+MERGE \
     -nt 128 \
     -pre supermatrix
