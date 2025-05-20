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
