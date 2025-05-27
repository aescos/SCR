#!/bin/bash -l
#
# SBATCH directives
#
# (1) Account to charge
#SBATCH -A naiss2025-22-683
#
# (2) Job name
#SBATCH -J cactus-hal2maf
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
#SBATCH -o cactus-hal2maf.%j.out
#SBATCH -e cactus-hal2maf.%j.err

# ============ Your commands start here ============

# Load the cactus progressive module that PDC provides
module load PDC singularity

# Move into the directory where your cactus lives
cd /cfs/klemming/projects/supr/naiss2025-22-683/0003_hairpinConservation/data

# Launch Progressive Cactus
srun singularity exec     --bind $PWD:/data:rw \
    ${PDC_SHUB}/cactus-v2.9.8.img \
    cactus-hal2maf \
      /data/cactus_workdir \
      /data/cactus_alignment.hal \
      /data/0019_cactus_alignment.maf \
      --refGenome 0005_Drosophila_melanogaster_dna_masked \
      --noAncestors \
      --dupeMode single \
      --chunkSize 1000000 \
      --filterGapCausingDupes
