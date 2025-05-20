#!/bin/bash
# Change to your working directory (if not already there)
cd /Users/alejandraescos/Documents/github/SCR/0002_phylogenetics/data/data

# Loop over each file matching "*longest_isoform.fa"
for file in *longest_isoform.fa; do
    # Get the base filename (remove the extension)
    base_name=$(basename "$file" .fa)
    
    # Construct an output folder name, e.g., "filename_busco"
    output_folder="${base_name}_busco"
    
    # Print information for the current file
    echo "Processing $file, output will be saved in $output_folder"
    
    # Run BUSCO using Docker on the current file
    docker run --rm -v "$PWD":/data -w /data ezlabgva/busco:v5.4.7_cv1 busco -i "$file" -o "$output_folder" -m proteins -l diptera_odb10 -f
done
