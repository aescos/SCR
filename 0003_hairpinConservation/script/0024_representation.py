#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

# Load the parsed table
df = pd.read_csv("/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/data/0023_hairpin_structure_conservation_table.txt", sep="\t")

# Optional: sort for visibility
df_filtered = df[df["total_mfe"] < 0]
df_sorted = df_filtered.sort_values(by="total_mfe")  # Most negative = most stable

# Free energy (MFE) for each gene
plt.figure(figsize=(18, 6))
plt.bar(df_sorted["gene_id"], df_sorted["total_mfe"])
plt.xticks(rotation=90, fontsize=6)
plt.ylabel("Total MFE (kcal/mol)")
plt.title("RNAalifold Minimum Free Energy per Gene")
plt.tight_layout()
plt.show()

# Covariation bonues
plt.figure(figsize=(18, 6))
plt.bar(df_sorted["gene_id"], df_sorted["covariation"])
plt.xticks(rotation=90, fontsize=6)
plt.ylabel("Covariation Bonus")
plt.title("Covariation Support per Gene")
plt.tight_layout()
plt.show()

# Plot 3: Ensemble Diversity
plt.figure(figsize=(18, 6))
plt.bar(df_sorted["gene_id"], df_sorted["diversity"])
plt.xticks(rotation=90, fontsize=6)
plt.ylabel("Ensemble Diversity")
plt.title("Structural Consistency Across Sequences")
plt.tight_layout()
plt.show()

# Plot 4: MFE Frequency
plt.figure(figsize=(18, 6))
plt.bar(df_sorted["gene_id"], df_sorted["mfe_freq"])
plt.xticks(rotation=90, fontsize=6)
plt.ylabel("MFE Frequency")
plt.title("Ensemble Frequency of Predicted Structure")
plt.tight_layout()
plt.show()
