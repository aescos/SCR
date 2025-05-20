drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

Basic structure:
1.  DATA-ORIGIN:
0003_dmle_3UTR.fa

2.  DATA-DATE:
02042025

3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
6.  METHODS/WORKFLOWS

### Trim sequences before prediction

Trim the file to take the 60 first nt of the 3'UTR

- trim_length = 60

```zsh 5.9 (arm64-apple-darwin24.0)

    python3 0003_test.py

```

```python 3.12.4 # script 0004_trim.py
import os
import glob

def read_fasta(file_path):
    with open(file_path, 'r') as file:
        header = ''
        sequence = ''
        for line in file:
            if line.startswith('>'):
                if header:
                    yield (header, sequence)
                header = line.strip()
                sequence = ''
            else:
                sequence += line.strip()
        if header:
            yield (header, sequence)

def save_trimmed_fasta(input_file, output_file, trim_length):
    with open(output_file, 'w') as out_file:
        for header, sequence in read_fasta(input_file):
            trimmed_sequence = sequence[:trim_length]
            out_file.write(f"{header}\n{trimmed_sequence}\n")

# settings
input_file = '/Users/alejandraescos/Documents/github/SCR/data/0003_dmle_3UTR.fa'
output_file = '/Users/alejandraescos/Documents/github/SCR/data/0004_dmle_3UTR_trim.fa'
trim_length = 60

save_trimmed_fasta(input_file, output_file, trim_length)
```
