Basic structure:
1.  DATA-ORIGIN:
2.  DATA-DATE:
3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
6.  METHODS/WORKFLOWS

drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

### Obtain fasta_chunks taking into account if + or - strand


1.  DATA-ORIGIN:
path(/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation)

2.  DATA-DATE:
20250521

3.  DATA-VERSION:


4.  DOWLOADED-SCRIPT:

0018_AlignIO.py
``` 
from Bio import AlignIO
from collections import defaultdict
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from collections import Counter
from itertools import chain
import os

# Input BED file
input_bed = "/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/data/0016_dmle_selected_three_prime_utr_extend.bed"

maf_strand = defaultdict(str)

# Read BED file and collect MAF file paths and strands
with open(input_bed, "r") as infile:
    for line in infile:
        if line.strip() == "":
            continue

        fields = line.strip().split("\t")
        chrom, start, end, name, score, strand = fields
        maf_strand[f"0017_maf_chunks/{name}_{chrom}_{start}_{end}.maf"] = strand

# Process each MAF file
for maf_file, strand in maf_strand.items():
    fasta_file = maf_file.replace(
        "0017_maf_chunks", "0018_fa_chunks").replace(".maf", ".fa")

    # Ensure output directory exists
    os.makedirs(os.path.dirname(fasta_file), exist_ok=True)

    # Concatenate sequences by species
    concatenated = defaultdict(str)

    n = 0
    with open(maf_file) as handle:
        for multiple_alignment in AlignIO.parse(handle, "maf"):
            for i,record in enumerate(multiple_alignment):
                if i == 0:
                    b = len(record.seq)
                    n += b
                concatenated[record.id] += "-" * (n-b-len(concatenated.get(record.id,"")))
                concatenated[record.id] += record.seq 
        for org, seq in concatenated.items():
            concatenated[org] += "-" * (n - len(seq))

    # Create SeqRecords with or without reverse complement
    duplicates = [
        item
        for item, count in Counter(
            [k.split(".")[0] for k in concatenated.keys()]
        ).items()
        if count > 1
    ]

    duplicates = {org: [k for k in concatenated.keys() if k.split(".")[0] == org] for org in duplicates}  

    ref = list(concatenated.keys())[0]
    for org, contigs in duplicates.items():
        scores = defaultdict(int)
        for c in contigs:
            s = 0
            for a, b in zip(concatenated[ref], concatenated[c]):
                if a == b:
                    s += 2 if a != '-' else 1
            scores[c] = s
        key_to_remove = max(scores, key=scores.get)
        duplicates[org].remove(key_to_remove)

    sequences_to_remove = list(chain.from_iterable(duplicates.values()))

    records = [
        SeqRecord(
            Seq(seq) if strand == "+" else Seq(seq).reverse_complement(),
            id=species,
            description="",
        )
        for species, seq in concatenated.items() if not species in sequences_to_remove
    ]

   # Write output FASTA
    with open(fasta_file, "w") as out_handle:
        SeqIO.write(records, out_handle, "fasta")

```

5.  SOFTWARE-VERSION:

