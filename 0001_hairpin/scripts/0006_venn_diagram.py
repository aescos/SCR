import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Paths to input and output
file_mfe = '/Users/alejandraescos/Documents/github/SCR/0001_hairpin/data/0007_subopt_Y_minMFE.txt'
file_genelist = '/Users/alejandraescos/Documents/github/SCR/0001_hairpin/data/jungreis_genelist_2016.txt'
output_dir = '/Users/alejandraescos/Documents/github/SCR/0001_hairpin/results_figures'
output_file = os.path.join(output_dir, 'venn_diagram.png')

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)
# Read the first column (column 0) from the MinMFE file
df_mfe = pd.read_csv('/Users/alejandraescos/Documents/github/SCR/0001_hairpin/data/0007_subopt_Y_minMFE.txt', sep='\t', header=None, usecols=[0])
set_mfe = set(df_mfe.iloc[:, 0].dropna().astype(str))

# Read the second column (column 1) from the Jungreis gene list file
df_genelist = pd.read_csv('/Users/alejandraescos/Documents/github/SCR/0001_hairpin/data/jungreis_genelist_2016.txt', sep='\t', header=None, usecols=[1])
set_genelist = set(df_genelist.iloc[:, 0].dropna().astype(str))

# Plot Venn diagram with custom colors
plt.figure(figsize=(6, 6))
v = venn2([set_mfe, set_genelist], set_labels=('Hairpin prediction', 'Jungreis GeneList'))
v.get_patch_by_id('10').set_color('#66c2a5')  # Color for Hairpin prediction
v.get_patch_by_id('01').set_color('#fc8d62')  # Color for Jungreis GeneList
v.get_patch_by_id('11').set_color('#8da0cb')  # Color for intersection

plt.title("Venn Diagram")

# Save the figure
plt.savefig(output_file, dpi=300, bbox_inches='tight')
plt.show()