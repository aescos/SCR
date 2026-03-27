Basic structure:
1.  DATA-ORIGIN:
2.  DATA-DATE:
3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
6.  METHODS/WORKFLOWS

drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

### Use RNAolif to detec pair conservation of the hairpin

1.  DATA-ORIGIN:
path(/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation)
0020_I_fa_chunks_trimmed_by_stop

2.  DATA-DATE:
20250624

3.  DATA-VERSION:
0022_structure_conservation.txt

4.  DOWLOADED-SCRIPT:

0022_hairpin_structure_conservation.sh

```
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

```