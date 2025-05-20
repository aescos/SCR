Basic structure:
1.  DATA-ORIGIN:
2.  DATA-DATE:
3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
6.  METHODS/WORKFLOWS

drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

### Parse protein data


1.  DATA-ORIGIN:
path(/Users/alejandraescos/Documents/github/SCR/0002_phylogenetics/data)

2.  DATA-DATE:
20250416

3.  DATA-VERSION:
0001_parse_fasta.py

4.  DOWLOADED-SCRIPT:
```
import glob
import os
import re
from Bio import SeqIO

# Change the working directory to your target folder
os.chdir("/Users/alejandraescos/Documents/github/SCR/PEC1/2025_drosophila_vvl_paper/data/data")

# Get all FASTA files in the current folder (assuming extension ".fa")
fasta_files = glob.glob("*.fa")

for file in fasta_files:
    input_file = file
    base_name, _ = os.path.splitext(os.path.basename(file))
    
    # Split base_name on both "_" and "." to build a species name from the first two parts
    parts = re.split(r'[_\.]', base_name)
    if len(parts) >= 2:
        species_name = f"{parts[0]}_{parts[1]}"
    else:
        species_name = base_name
    
    # Create the output filename: 0001_{species_name}_longest_isoform.fa
    output_file = f"0001_{species_name}_longest_isoform.fa"
    
    # Dictionary to store the longest record per gene.
    # Key: gene ID (extracted from the "gene:" field)
    # Value: tuple(record, actual_length)
    gene_dict = {}
    
    # Parse the FASTA file and process each record
    for record in SeqIO.parse(input_file, "fasta"):
        header = record.description
        
        # Extract gene ID from the "gene:" field.
        # It assumes that the header contains a segment like "gene:FBgnXXXXXXXX" followed by a space.
        if "gene:" in header:
            gene_field = header.split("gene:")[-1]
            gene_id = gene_field.split(" ")[0]
        else:
            gene_id = record.id  # Fallback if "gene:" is not found
        
        # Determine the protein length by counting amino acids directly in the sequence.
        actual_length = len(record.seq)
        
        # For each gene, keep only the record with the greatest actual length.
        if gene_id not in gene_dict:
            gene_dict[gene_id] = (record, actual_length)
        else:
            _, current_length = gene_dict[gene_id]
            if actual_length > current_length:
                gene_dict[gene_id] = (record, actual_length)
    
    # Gather the selected (longest) records for each gene.
    selected_records = [record for (record, _) in gene_dict.values()]
    
    # Write the selected records to the output FASTA file (headers remain unchanged).
    SeqIO.write(selected_records, output_file, "fasta")
    print(f"Processed {input_file}: saved {len(selected_records)} records to {output_file}")
```
5.  SOFTWARE-VERSION:
python 3.12.4

