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

sort -k1,1V -k2,2n 0016_dmle_selected_three_prime_utr_extend.bed > dmle_selected_three_prime_utr_sorted.bed

srun singularity exec     --bind $PWD:/data:rw \
    ${PDC_SHUB}/cactus-v2.9.8.img \
    cactus-hal2maf \
      /data/tmp \
      /data/cactus_alignment.hal \
      /data/three_prime_utrs_extend.maf \
      --refGenome 0005_Drosophila_melanogaster_dna_masked \
      --noAncestors \
      --dupeMode single \
      --chunkSize 1000000 \
      --filterGapCausingDupes \
      --bedRanges dmle_selected_three_prime_utr_sorted.bed \
      --index


srun singularity exec --bind $PWD:/data:rw ${PDC_SHUB}/cactus-v2.9.8.img bash <<'EOF'
while read chrom start end geneid rest; do
out="maf_chunks/${geneid}_${chrom}_${start}_${end}.maf"
region="0005_Drosophila_melanogaster_dna_masked.${chrom}:${start}-${end}"
taffy view -i three_prime_utrs_extend.maf -r ${region} -m > ${out}
echo "Written ${out}"
done < dmle_selected_three_prime_utr_sorted.bed
EOF
