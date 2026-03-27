#!/bin/bash

INPUT_DIR="/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/data/0020_I_fa_chunks_trimmed_by_stop"
OUTPUT_FILE="/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/data/0022_structure_conservation.txt"

# Clear the output file if it exists
> "$OUTPUT_FILE"

for file in "$INPUT_DIR"/*.sto; do
    echo "Processing $file" | tee -a "$OUTPUT_FILE"
    
    # Run RNAalifold and capture key output
    RNAalifold -p --noPS "$file" 2>&1 | tee -a "$OUTPUT_FILE"
    
    echo -e "\n---------------------------------------------\n" >> "$OUTPUT_FILE"
done
