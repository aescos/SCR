#!/usr/bin/env python3
from Bio import AlignIO, SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from collections import defaultdict, Counter
from itertools import chain
from pathlib import Path
import os

# 1) read the BED to get the strand for each region
maf_strand = {}
with open("/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/data/0016_dmle_selected_three_prime_utr_extend.bed") as bed:
    for line in bed:
        if not line.strip(): continue
        chrom, start, end, name, *_ , strand = line.split()
        key = f"0017_filtered_mafs/{name}_{chrom}_{start}_{end}.maf"
        maf_strand[key] = strand

# 2) process each MAF
for maf_file, strand in maf_strand.items():
    out_fa = maf_file.replace("0017_filtered_mafs", "0018_fa_chunks").replace(".maf", ".fa")
    os.makedirs(os.path.dirname(out_fa), exist_ok=True)

    # collect and stitch blocks
    concatenated = defaultdict(str)
    total_cols = 0

    with open(maf_file) as handle:
        for aln in AlignIO.parse(handle, "maf"):
            blk_len = aln.get_alignment_length()
            # pad any new species to the current total, then append this block
            for rec in aln:
                if rec.id not in concatenated:
                    concatenated[rec.id] = ""
                pad = total_cols - len(concatenated[rec.id])
                if pad > 0:
                    concatenated[rec.id] += "-" * pad
                concatenated[rec.id] += str(rec.seq)
            total_cols += blk_len

    # final pad so everyone reaches total_cols
    for k in concatenated:
        trailing = total_cols - len(concatenated[k])
        if trailing > 0:
            concatenated[k] += "-" * trailing

    # 3) drop duplicate contigs per species (choose best against the first key)
    ref = next(iter(concatenated))
    # group by “species” prefix (adjust split as appropriate)
    groups = defaultdict(list)
    for k in concatenated:
        species = k.split(".")[0]  # or however you identify your species
        groups[species].append(k)

    to_remove = []
    for species, keys in groups.items():
        if len(keys) <= 1:
            continue
        # score each contig vs ref
        scores = {}
        for k in keys:
            s = sum(
                2 if a == b and a != "-" else
                1 if a == b == "-" else
                0
                for a, b in zip(concatenated[ref], concatenated[k])
            )
            scores[k] = s
        # keep only the best one
        best = max(scores, key=scores.get)
        keys.remove(best)
        to_remove.extend(keys)

    # 4) build SeqRecords (and rc if needed) and write FASTA
    records = []
    for k, seq in concatenated.items():
        if k in to_remove:
            continue
        s = Seq(seq)
        if strand == "-":
            s = s.reverse_complement()
        records.append(SeqRecord(s, id=k, description=""))

    with open(out_fa, "w") as out_h:
        SeqIO.write(records, out_h, "fasta")
