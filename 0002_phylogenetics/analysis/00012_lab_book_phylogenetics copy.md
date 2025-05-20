Basic structure:
1.  DATA-ORIGIN:
2.  DATA-DATE:
3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
6.  METHODS/WORKFLOWS

drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

### BUSCO from orthoBD
You can install the BUSCO_Phylogenomics package with Conda from the Bioconda channel
https://github.com/jamiemcg/BUSCO_phylogenomics

1.  DATA-ORIGIN:
path(/Users/alejandraescos/Documents/github/SCR/0002_phylogenetics/data)

2.  DATA-DATE:
20250508

3.  DATA-VERSION:
SUPERMATRIX.fasta

4.  DOWLOADED-SCRIPT:
```zsh
conda create -n BUSCO_phylogenomics -c bioconda busco_phylogenomics
conda activate BUSCO_phylogenomics
cd /Users/alejandraescos/BUSCO_phylogenomics
ln -s /Users/alejandraescos/Documents/github/SCR/0002_phylogenetics/data/0002_BUSCO_results ./BUSCO_results

python BUSCO_phylogenomics.py -i BUSCO_results -o 0003_busco_phylogenomics -t 10 --supermatrix_only
```

I have now a concatenated file of all the protein sequences and I will generate the tree from this file with iqtree2 using PDC Dardel.

```pdc darcel
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
# (5) Resources: here we use 1 node, 1 task, and 10 threads
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
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
     -nt $SLURM_CPUS_PER_TASK \
     -pre supermatrix

```

5.  SOFTWARE-VERSION:
iqtree2