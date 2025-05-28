#!/usr/bin/env python3
import glob
import os
import re

import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------------------
# CONFIGURE THIS: wherever your .txt files live
stats_dir = "/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/data/0021_fa_chunks_60nt_stats"
pattern   = os.path.join(stats_dir, "*.txt")
# ----------------------------------------------------------------

# 1) collect all records
records = []
txt_files = glob.glob(pattern)
print(f"found files: {len(txt_files)}")

for path in txt_files:
    name = os.path.basename(path).replace(".txt","")
    txt  = open(path).read()
    Lm   = re.search(r"Alignment length:\s+(\d+)", txt)
    Im   = re.search(r"Average identity:\s+(\d+)%", txt)
    if not Lm or not Im:
        continue
    L = int(Lm.group(1))
    I = float(Im.group(1))
    records.append({
        "alignment":   name,
        "aln_length":  L,
        "avg_identity": I
    })

# 2) build DataFrame
df = pd.DataFrame(records)
print("number of records parsed:", len(df))
print("columns:", df.columns.tolist())
print(df.head())

# ** NEW: keep only the 60-nt windows **
df60 = df[df["aln_length"] == 60].copy()
print("only 60-nt windows:", len(df60))

# 3) plot distribution of alignment lengths
plt.figure()
df["aln_length"].hist(bins=30)
plt.xlabel("Alignment length (columns)")
plt.ylabel("Count")
plt.title("Distribution of alignment lengths")
plt.tight_layout()
plt.show()

# 4) plot distribution of average identity
plt.figure()
df60["avg_identity"].hist(bins=30)
plt.xlabel("Average identity (%)")
plt.ylabel("Count")
plt.title("Distribution of average identity")
plt.tight_layout()
plt.show()

# 5) pull out the most and least conserved by quantile
high_q = df60["avg_identity"].quantile(0.9)
low_q  = df60["avg_identity"].quantile(0.1)

most_conserved = df60[df60["avg_identity"] >= high_q]
least_conserved = df60[df60["avg_identity"] <= low_q]

out_dir = "/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/results_figures"
most_conserved.to_csv(f"{out_dir}/most_conserved_top10pct.csv", index=False)
least_conserved.to_csv(f"{out_dir}/least_conserved_bottom10pct.csv", index=False)