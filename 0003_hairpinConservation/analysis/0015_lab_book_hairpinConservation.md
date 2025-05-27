Basic structure:
1.  DATA-ORIGIN:
2.  DATA-DATE:
3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
6.  METHODS/WORKFLOWS

drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

### Hairpin conservation for a list of genes from drosophila melanogaster


1.  DATA-ORIGIN:
path(/Users/alejandraescos/Documents/github/SCR/0002_phylogenetics/data)

2.  DATA-DATE:
20250512

3.  DATA-VERSION:
SUPERMATRIX.fasta

4.  DOWLOADED-SCRIPT:
Run hal2maf in docker

```
awk '
  BEGIN { FS=OFS="\t" }
  NR==FNR { genes[$1]=1; next }
  {
    # Extract gene_id from the attributes column ($9):
    g=$9
    sub(/.*gene_id "/, "", g)
    sub(/".*/, "", g)
    # If it’s in our list, print the line
    if (g in genes) print
  }
' 0007_subopt_Y_minMFE.bed 0002_dmle_3UTR.gtf \
> 0016_dmle_selected_3UTR.gtf

```

```
awk 'BEGIN{FS=OFS="\t"}
     # skip headers
     !/^#/ {
       # $1=chr, $4=start(1-based), $5=end
       printf "%s\t%d\t%d\n", $1, $4-1, $5
     }' 0002_dmle_selected_3UTR.gtf \
  > 0017_utr3.bed
```

changing gtf to bed format

```
import gffutils
import pandas as pd

sel = pd.read_csv("/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/data/0007_subopt_Y_minMFE.bed",skiprows=1,sep='\t',header=None)
selected_list = list(sel[0])

# === CONFIG ===
gtf_file = "Drosophila_melanogaster.BDGP6.46.60.gtf"
output_bed = "dmle_selected_three_prime_utr.bed"
feature_type = "three_prime_utr"  # can be "CDS", "gene", etc.
attribute_key = "gene_id"  # or "gene_id"

# === BUILD DATABASE ===
db = gffutils.create_db(gtf_file, dbfn=':memory:', force=True, keep_order=True, merge_strategy='merge', sort_attribute_values=True)

with open(output_bed, 'w') as bedout:
    for feature in db.features_of_type(feature_type):
        chrom = feature.chrom
        start = feature.start - 1  # BED is 0-based
        end = feature.end         # BED end is non-inclusive
        strand = feature.strand
        attrs = feature.attributes
        name = attrs.get(attribute_key, ["NA"])[0]
        if name in selected_list:
            bedout.write(f"{chrom}\t{start}\t{end}\t{name}\t.\t{strand}\n")

```
Testing

import gffutils
import pandas as pd

# Read selected gene list from BED file
sel = pd.read_csv(
    "/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/data/0007_subopt_Y_minMFE.bed",
    skiprows=1,
    sep='\t',
    header=None
)
selected_list = set(sel[0].astype(str))

# === CONFIG ===
gtf_file = "Drosophila_melanogaster.BDGP6.46.60.gtf"
output_bed = "dmle_selected_three_prime_utr.bed"
feature_type = "three_prime_utr"
attribute_key = "gene_id"

# Build an in-memory GFF database
db = gffutils.create_db(
    gtf_file,
    dbfn=':memory:',
    force=True,
    keep_order=True,
    merge_strategy='merge',
    sort_attribute_values=True
)

# Dictionary to hold the earliest 3' UTR per gene
gene_utrs = {}

# Iterate over all 3' UTR features
for feature in db.features_of_type(feature_type):
    chrom = feature.chrom
    start = feature.start - 1  # BED is 0-based
    end = feature.end          # BED end is non-inclusive
    strand = feature.strand
    attrs = feature.attributes
    gene_id = attrs.get(attribute_key, ["NA"])[0]

    # Only keep features for genes in our selected list
    if gene_id in selected_list:
        # Construct the BED line
        line = f"{chrom}\t{start}\t{end}\t{gene_id}\t.\t{strand}"

        # Keep only the earliest (lowest 'start') 3' UTR per gene
        if gene_id not in gene_utrs or start < gene_utrs[gene_id]['start']:
            # Replace literal 'three_prime_utr' text with the gene_id
            gene_utrs[gene_id] = {
                'line': line.strip().replace("three_prime_utr", gene_id),
                'start': start,
                'end': end
            }

# Write out the filtered BED entries
with open(output_bed, 'w') as bedout:
    for data in gene_utrs.values():
        bedout.write(data['line'] + "\n")





```
docker run -v $(pwd):/data --rm -it quay.io/comparative-genomics-toolkit/cactus:v2.9.8 bash

while read chrom start end name score strand; do
    hal2maf \
        --refGenome 0005_Drosophila_melanogaster_dna_masked \
        --refSequence $chrom \
        --start $start \
        --length $((end - start)) \
        --targetGenomes 0005_Drosophila_albomicans_dna_masked,0005_Drosophila_innubila_dna_masked,0005_Drosophila_simulans_dna_masked,0005_Drosophila_ananassae_dna_masked,0005_Drosophila_mauritiana_dna_masked,0005_Drosophila_subobscura_dna_masked,0005_Drosophila_arizonae_dna_masked,0005_Drosophila_melanogaster_dna_masked,0005_Drosophila_subpulchrella_dna_masked,0005_Drosophila_biarmipes_dna_masked,0005_Drosophila_miranda_dna_masked,0005_Drosophila_suzukii_dna_masked,0005_Drosophila_busckii_dna_masked,0005_Drosophila_mojavensis_dna_masked,0005_Drosophila_takahashii_dna_masked,0005_Drosophila_elegans_dna_masked,0005_Drosophila_navojoa_dna_masked,0005_Drosophila_teissieri_dna_masked,0005_Drosophila_erecta_dna_masked,0005_Drosophila_obscura_dna_masked,0005_Drosophila_virilis_dna_masked,0005_Drosophila_eugracilis_dna_masked,0005_Drosophila_persimilis_dna_masked,0005_Drosophila_willistoni_dna_masked,0005_Drosophila_grimshawi_dna_masked,0005_Drosophila_pseudoobscura_dna_masked,0005_Drosophila_yakuba_dna_masked,0005_Drosophila_guanche_dna_masked,0005_Drosophila_rhopaloa_dna_masked,0005_Glossina_morsitans_dna_masked,0005_Drosophila_gunungcola_dna_masked,0005_Drosophila_santomea_dna_masked,0005_Lucilia_cuprina_dna_masked,0005_Drosophila_hydei_dna_masked,0005_Drosophila_sechellia_dna_masked \
        --noAncestors \
        cactus_alignment.hal \
        stdout \
    > maf/${chrom}_${start}_${end}.maf
done < dmle_selected_three_prime_utr.bed
```

***BigMaf***

UCSC BigMaf is an indexed version of MAF (see above) that can viewed on the Genome Browser. cactus-maf2bigmaf can be used to convert MAF (as output by cactus-hal2maf) into BigMaf.

It is recommended to create the maf using the --noAncestors options with cactus-hal2maf. The Browser does not support duplicates, so cactus-maf2bigmaf will automatically filter them out using mafDuplicateFilter -k.

cactus-maf2bigmaf ./js ./evolverMammals.maf.gz ./evolverMammals.bigmaf.bb --refGenome simHuman_chr6 --halFile evolverMammals.hal
This will produce the BigMaf file evolverMammals.bigmaf.bb along with the summary file evolverMammals.bigmaf.summary.bb which is used by the browser for zoomed out summary display.

The chromosome sizes of the reference genome must be provided via the original hal file via --halFile.

```
# 1) Re‐export the MAF via cactus-hal2maf
docker run -v $(pwd):/data --rm quay.io/comparative-genomics-toolkit/cactus:v2.9.8 \
  cactus-hal2maf \
    /data/cactus_workdir                         \
    /data/cactus_alignment.hal         \
    /data/cactus_alignment.maf.gz      \
    --refGenome 0005_Drosophila_melanogaster_dna_masked         \
    --noAncestors                    \
    --dupeMode single                \
    --chunkSize 1000000              \
    --filterGapCausingDupes

```

```
# 2) Convert that MAF into a bigMaf.bb via cactus-maf2bigmaf
docker run -v $(pwd):/data --rm quay.io/comparative-genomics-toolkit/cactus:v2.9.8 \
  cactus-maf2bigmaf \
    --refGenome 0005_Drosophila_melanogaster_dna_masked               \
    --halFile /data/cactus_alignment.hal      \
    /data/js                                \
    /data/cactus_alignment.maf.gz             \
    /data/cactus_alignment.bigmaf.bb

```


5.  SOFTWARE-VERSION:

***ChatGPT***



3. Assess secondary-structure conservation
A. Using RNAz
Install: part of the Vienna-RNA package + RNAz.

Run on each MAF:

```
rnazWindow.pl --maf maf/${name}.maf --window 120 --slide 40 \
  | rnazCompute.pl > rnaz/${name}.rnaz
This splits the UTR alignment into overlapping windows (120 nt wide, 40 nt slide).

RNAz assigns a p-value and “RNA class” probability for each window.

Parse results to find windows with P > 0.5 (likely conserved structures) and map back to coordinates.

B. Using EvoFold (alternative)
EvoFold from UCSC also detects conserved RNA structures in MAF blocks; you’d need the phyloP tree model for Drosophila.
```