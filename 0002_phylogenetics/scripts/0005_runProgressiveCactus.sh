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
cd /cfs/klemming/home/a/aescos/Private/0005_cactus

# Launch Progressive Cactus
# export CACTUS_TMPDIR=/cfs/klemming/home/a/aescos/Private/0005_cactus/tmp/
srun singularity exec ${PDC_SHUB}/cactus-v2.9.8.img cactus cactus_workdir 0005_seqfile.txt cactus_alignment.hal
