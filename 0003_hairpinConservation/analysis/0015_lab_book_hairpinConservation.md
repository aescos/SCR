Basic structure:
1.  DATA-ORIGIN:
2.  DATA-DATE:
3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
6.  METHODS/WORKFLOWS

drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

### Have an index of locations of interest from the hairpin prediction


1.  DATA-ORIGIN:
path(/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation)

2.  DATA-DATE:
20250521

3.  DATA-VERSION:
0007_subopt_Y_minMFE.bed

4.  DOWLOADED-SCRIPT:

``` 0015_3utr_conserved_selection.py
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
output_bed = "0015_dmle_selected_three_prime_utr.bed"
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

Then I extended these nucleotides 33 before the start codon taking into accoun if the 3'UTR is in the + strand or if it is in the - strand.

```0016_dmle_three_prime_utr_extend.py
# Input and output file paths
input_bed = "/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/data/0015_dmle_selected_three_prime_utr.bed"
output_bed = "/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/data/0016_dmle_selected_three_prime_utr_extend.bed"

# Process the BED file
with open(input_bed, "r") as infile, open(output_bed, "w") as outfile:
    for line in infile:
        if line.strip() == "":
            continue  # Skip empty lines

        fields = line.strip().split("\t")
        chrom, start, end, name, score, strand = fields

        start = int(start)
        end = int(end)

        if strand == "+":
            start = max(0, start - 33)  # Ensure start doesn't go below 0
        elif strand == "-":
            end = end + 33

        # Write modified line
        outfile.write(f"{chrom}\t{start}\t{end}\t{name}\t{score}\t{strand}\n")
```

5.  SOFTWARE-VERSION:

