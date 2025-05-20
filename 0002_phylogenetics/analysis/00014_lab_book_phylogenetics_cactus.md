Basic structure:
1.  DATA-ORIGIN:
2.  DATA-DATE:
3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
6.  METHODS/WORKFLOWS

drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

### CACTUS progressive pipeline


1.  DATA-ORIGIN:
path(/Users/alejandraescos/Documents/github/SCR/0002_phylogenetics/data)

2.  DATA-DATE:
20250515

3.  DATA-VERSION:
0005_seqfile.txt file structure:

Newick tree
full path for each variable in Newick tree


4.  DOWLOADED-SCRIPT:
Run cactus progressive in dardel

```
#!/bin/bash -l
#
# SBATCH directives
#
# (1) Account to charge
#SBATCH -A naiss2025-22-683
#
# (2) Job name
#SBATCH -J cactus_progressive
#
# (3) Partition (queue)
#SBATCH -p main
#
# (4) Wall‐time (HH:MM:SS)
#SBATCH -t 24:00:00
#
# (5) Resources: here we use 1 node, 1 task, and 10 threads
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=128
#
# (6) Output files
#SBATCH -o cactus.%j.out
#SBATCH -e cactus.%j.err

# ============ Your commands start here ============

# Load the cactus progressive module that PDC provides
module load PDC singularity

# Move into the directory where your cactus lives
cd //cfs/klemming/projects/supr/naiss2025-22-683/0005_cactus

# Launch Progressive Cactus
srun singularity exec ${PDC_SHUB}/cactus-v2.9.8.img cactus cactus_workdir 0005_seqfile.txt cactus_alignment.hal
```

It took more than 24 h so I rerun again justa adding --restart

```
#!/bin/bash -l
#
# SBATCH directives
#
# (1) Account to charge
#SBATCH -A naiss2025-22-683   # ← replace with your project/allocation
#
# (2) Job name
#SBATCH -J cactus_progressive
#
# (3) Partition (queue)
#SBATCH -p main
#
# (4) Wall‐time (HH:MM:SS)
#SBATCH -t 24:00:00
#
# (5) Resources: here we use 1 node, 1 task, and 10 threads
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=128
#
# (6) Output files
#SBATCH -o cactus.%j.out
#SBATCH -e cactus.%j.err

# ============ Your commands start here ============

# Load the cactus progressive module that PDC provides
# module load bioinfo-tools
module load PDC singularity
# To complete the module load
# source $PCROOT/environment
# Move into the directory where your cactus lives
cd /cfs/klemming/projects/supr/naiss2025-22-683/0005_cactus

# Launch Progressive Cactus
srun singularity exec ${PDC_SHUB}/cactus-v2.9.8.img cactus --restart  cactus_workdir 0005_seqfile.txt cactus_alignment.hal
```

5.  SOFTWARE-VERSION:
cactus-v2.9.8

