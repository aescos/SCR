Basic structure:
1.  DATA-ORIGIN:
2.  DATA-DATE:
3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
6.  METHODS/WORKFLOWS

drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

### Parse RNAolif for graph preparation
https://www.tbi.univie.ac.at/RNA/ViennaRNA/refman/tutorial/RNAalifold.html#introduction

I am using vvl/dfr (FBgn0086680) as an example.

**MFE (Minimum Free Energy)** structure is the most thermodynamically stable structure predicted for the RNA sequence. It has base energy + covariance term.

```
............(((((((.((.(.((((....)))).))).)))))))........... (-17.36 = -17.36 +   0.00)
```
**Centroid Structure:** the structure with the minimum average distance to all structures in the ensemble.

```
............(((((((.(,{(.((((....)))).))).)))))))........... [-18.00]
```

**Structure with Ensemble Distance**: Representative structure with a specific base pair distance (d=1.31) from the ensemble centroid

```
............(((((((.(.((.((((....)))).))).)))))))........... {-17.36 = -17.36 +   0.00 d=1.31}
```

**Frequency of mfe structure in ensemble:** The frequency value here tells you how often this structure appears in the Boltzmann ensemble of all possible secondary structures, weighted by their thermodynamic probability. (How many other structures with similar free energies are also likely)

```
frequency of mfe structure in ensemble 0.0744065
```

**Ensemble diversity:** how diverse the ensemble is in terms of structure. The average base pair distance between all structures in the ensemble

```
ensemble diversity 15.35
```

1.  DATA-ORIGIN:
path(/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/data)
0022_hairpin_structure_conservation.txt

Bernhart, Stephan H., Ivo L. Hofacker, Sebastian Will, Andreas R. Gruber, and Peter F. Stadler. “RNAalifold: Improved Consensus Structure Prediction for RNA Alignments.” BMC Bioinformatics 9, no. 1 (November 11, 2008): 474. https://doi.org/10.1186/1471-2105-9-474.

2.  DATA-DATE:
20250624

3.  DATA-VERSION:
0023_hairpin_structure_conservation_table.txt

4.  DOWLOADED-SCRIPT:
Process this file to generate a comprehensive table

0023_test_parsing_structure_conservation.py
```
#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
import re

# Paths to input and output
input_file = Path('/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/data/0022_hairpin_structure_conservation.txt')
output_file = Path('/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/data/0023_hairpin_structure_conservation_table.txt')

records = []

def hairpin_cons(file_path):
    table_cons = None
    sequence_line = None
    structure_lines = []

    with open(file_path, 'r') as infile:
        for line in infile:
            line = line.strip()

            # New block starts
            if line.startswith('Processing'):
                # Save the previous block if valid
                if table_cons:
                    table_cons["sequence"] = sequence_line
                    if len(structure_lines) >= 3:
                        table_cons["mfe_structure"] = structure_lines[0]
                        table_cons["mean_structure"] = structure_lines[1]
                        table_cons["centroid_structure"] = structure_lines[2]
                    records.append(table_cons)

                # Reset for new entry
                sequence_line = None
                structure_lines = []
                seen_structure = False
                basename = line.split("/")[-1]
                parts = basename.split("_")
                table_cons = {
                    "gene_id": parts[0],
                    "chr": parts[1],
                    "start": parts[2],
                    "end": parts[3].replace('.sto', '')
                }

            elif table_cons is not None:
                # Capture sequence line (consensus)
                if sequence_line is None and not seen_structure and re.match(r'^[ACGU_-]+$', line):

                    sequence_line = line

                # Capture structure lines
                elif re.match(r'^[.(){}\[\]]+\s+\(', line):
                    structure_lines.append(line.split()[0])
                elif re.match(r'^[.(){}\[\]]+\s+\[', line):
                    structure_lines.append(line.split()[0])
                elif re.match(r'^[.(){}\[\]]+\s+\{', line):
                    structure_lines.append(line.split()[0])

                # Number of sequences and alignment length
                match = re.search(r"(\d+)\s+sequences;\s+length of alignment\s+(\d+)", line)
                if match:
                    table_cons["num_seqs"] = int(match.group(1))
                    table_cons["aln_len"] = int(match.group(2))

                # MFE and covariation
                mfe_match = re.search(r"\(\s*([-\d.]+)\s*=\s*([-\d.]+)\s*\+\s*([-\d.]+)", line)
                if mfe_match:
                    table_cons["total_mfe"] = float(mfe_match.group(1))
                    table_cons["mfe_energy"] = float(mfe_match.group(2))
                    table_cons["covariation"] = float(mfe_match.group(3))

                # Frequency and diversity
                freq_match = re.search(r"frequency of mfe structure.*?([\d.]+);.*?diversity ([\d.]+)", line)
                if freq_match:
                    table_cons["mfe_freq"] = float(freq_match.group(1))
                    table_cons["diversity"] = float(freq_match.group(2))

    # Save the last block
    if table_cons:
        table_cons["sequence"] = sequence_line
        if len(structure_lines) >= 3:
            table_cons["mfe_structure"] = structure_lines[0]
            table_cons["mean_structure"] = structure_lines[1]
            table_cons["centroid_structure"] = structure_lines[2]
        records.append(table_cons)

# Run and save
hairpin_cons(input_file)
df = pd.DataFrame(records)
df.to_csv(output_file, sep='\t', index=False)
```

