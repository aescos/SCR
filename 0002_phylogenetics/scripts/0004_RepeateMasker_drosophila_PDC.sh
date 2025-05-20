#!/bin/bash -l
#
# SBATCH directives
#
# (1) Account to charge
#SBATCH -A naiss2025-22-683
#
# (2) Job name
#SBATCH -J RepeatMasker
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
#SBATCH -o repeatmasker.%j.out
#SBATCH -e repeatmasker.%j.err

# ============ Your commands start here ============

# Load the RepeatMasker module that PDC provides
module load RepeatMasker

# Move into the directory lives
cd /cfs/klemming/home/a/aescos/Private/0004_masked

# Loop over all FASTA files (*.fa)
for f in *.fa; do
  base=${f%.fa}   # strip the .fa extension

  echo "Masking $f → ${base}_masked.fa"

  # Run RepeatMasker on this file
  srun RepeatMasker \
    -pa 128 \
    -species "Drosophila melanogaster" \
    -xsmall \
    -dir repeatmasker_out \
    "$f"

  # Rename the masked output back into current dir
  mv repeatmasker_out/"${base}.fa.masked" "${base}_masked.fa"
done