drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

Basic structure:
1.  DATA-ORIGIN:
2.  DATA-DATE:
3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
6.  METHODS/WORKFLOWS

```zsh 5.9 (arm64-apple-darwin24.0)
# Bash: folder location of the project
cd /Users/alejandraescos/Documents/github

# Create a folder
mkdir -p SCR

# Bash: Creates the folder structure directly.
mkdir  -p SCR/{data/seqs,scripts,analysis}

# Content of the folder
ls -lahtr

# Move back a folder
cd ..
```




### Download GTF from ensemble of 12 Drosophila genus:

1.  DATA-ORIGIN: 
ensembl

2.  DATA-DATE: 
20250312

3.  DATA-VERSION: 
Drosophila_melanogaster.BDGP6.46.113
Drosophila_ananassae.dana_caf1.60
Drosophila_erecta.dere_caf1.60
Drosophila_pseudoobscura.Dpse_3.0.60
Drosophila_simulans.ASM75419v3.60
Drosophila_virilis.dvir_caf1.60
Drosophila_grimshawi.dgri_caf1.60
Drosophila_mojavensis.dmoj_caf1.60
Drosophila_persimilis.dper_caf1.60
Drosophila_sechellia.dsec_caf1.60
Drosophila_willistoni.dwil_caf1.60
Drosophila_yakuba.dyak_caf1.60

4.  DOWLOADED-SCRIPT:
```
# Drosophila melanogaster = Dmel = 
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/gtf/drosophila_melanogaster/Drosophila_melanogaster.BDGP6.46.60.gtf.gz"
gunzip Drosophila_melanogaster.BDGP6.46.60.gtf.gz
cp {,0001_}Drosophila_melanogaster.BDGP6.46.60.gtf


# Drosophila ananassae = Dana = 
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/gtf/drosophila_ananassae/Drosophila_ananassae.dana_caf1.60.gtf.gz"
gunzip Drosophila_ananassae.dana_caf1.60.gtf.gz
cp {,0001_}Drosophila_ananassae.dana_caf1.60.gtf

# Drosophila erecta = Dere = 
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/gtf/drosophila_erecta/Drosophila_erecta.dere_caf1.60.gtf.gz"
gunzip Drosophila_erecta.dere_caf1.60.gtf.gz
cp {,0001_}Drosophila_erecta.dere_caf1.60.gtf

# Drosophila pseudoobscura pseudoobscura = Dpse = 
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/gtf/drosophila_pseudoobscura/Drosophila_pseudoobscura.Dpse_3.0.60.gtf.gz"
gunzip Drosophila_pseudoobscura.Dpse_3.0.60.gtf.gz
cp {,0001_}Drosophila_pseudoobscura.Dpse_3.0.60.gtf

# Drosophila simulans = Dsim = 
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/gtf/drosophila_simulans/Drosophila_simulans.ASM75419v3.60.gtf.gz"
gunzip Drosophila_simulans.ASM75419v3.60.gtf.gz
cp {,0001_}Drosophila_simulans.ASM75419v3.60.gtf

# Drosophila virilis = Dvir = 
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/gtf/drosophila_virilis/Drosophila_virilis.dvir_caf1.60.gtf.gz"
gunzip Drosophila_virilis.dvir_caf1.60.gtf.gz
cp {,0001_}Drosophila_virilis.dvir_caf1.60.gtf.gz

# Drosophila grimshawi = Dgri = 
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/gtf/drosophila_grimshawi/Drosophila_grimshawi.dgri_caf1.60.gtf.gz"
gunzip Drosophila_grimshawi.dgri_caf1.60.gtf.gz
cp {,0001_}Drosophila_grimshawi.dgri_caf1.60.gtf

# Drosophila mojavensis = Dmoj = 
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/gtf/drosophila_mojavensis/Drosophila_mojavensis.dmoj_caf1.60.gtf.gz"
gunzip Drosophila_mojavensis.dmoj_caf1.60.gtf.gz
cp {,0001_}Drosophila_mojavensis.dmoj_caf1.60.gtf

# Drosophila persimilis = Dper = 
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/gtf/drosophila_persimilis/Drosophila_persimilis.dper_caf1.60.gtf.gz"
gunzip Drosophila_persimilis.dper_caf1.60.gtf.gz
cp {,0001_}Drosophila_persimilis.dper_caf1.60.gtf


# Drosophila sechellia = Dsec = 
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/gtf/drosophila_sechellia/Drosophila_sechellia.dsec_caf1.60.gtf.gz"
gunzip Drosophila_sechellia.dsec_caf1.60.gtf.gz
cp {,0001_}Drosophila_sechellia.dsec_caf1.60.gtf

# Drosophila willistoni = Dwil = 
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/gtf/drosophila_willistoni/Drosophila_willistoni.dwil_caf1.60.gtf.gz"
gunzip Drosophila_willistoni.dwil_caf1.60.gtf.gz
cp {,0001_}Drosophila_willistoni.dwil_caf1.60.gtf

# Drosophila yakuba = Dyak = 
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/gtf/drosophila_yakuba/Drosophila_yakuba.dyak_caf1.60.gtf.gz"
gunzip Drosophila_yakuba.dyak_caf1.60.gtf.gz
cp {,0001_}Drosophila_yakuba.dyak_caf1.60.gtf

# culex_quinquefasciatus = mosquito
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/gtf/culex_quinquefasciatus/Culex_quinquefasciatus.CpipJ2.60.gtf.gz"
gunzip Culex_quinquefasciatus.CpipJ2.60.gtf.gz
cp {,0001_}Culex_quinquefasciatus.CpipJ2.60.gtf

# anopheles_darlingi = mosquito
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/gtf/anopheles_darlingi/Anopheles_darlingi.AdarC3.60.gtf.gz"
gunzip Anopheles_darlingi.AdarC3.60.gtf.gz
cp {,0001_}Anopheles_darlingi.AdarC3.60.gtf

# anopheles_gambiae = mosquito
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/gtf/anopheles_gambiae/Anopheles_gambiae.AgamP4.60.gtf.gz"
gunzip Anopheles_gambiae.AgamP4.60.gtf.gz
cp {,0001_}Anopheles_gambiae.AgamP4.60.gtf
```

5.  SOFTWARE-VERSION: 
zsh 5.9 (arm64-apple-darwin24.0)

6.  METHODS/WORKFLOWS


### Download FASTA from ensembl

1. DATA-ORIGIN: 
Ensembl

2. DATA-DATE: 
20250313

3. DATA-VERSION: 

Drosophila_melanogaster.BDGP6.46.dna.toplevel.fa
Drosophila_ananassae.dana_caf1.dna.toplevel.fa
Drosophila_erecta.dere_caf1.dna.toplevel.fa
Drosophila_pseudoobscura.Dpse_3.0.dna.toplevel.fa
Drosophila_simulans.ASM75419v3.dna.toplevel.fa
Drosophila_virilis.dvir_caf1.dna.toplevel.fa
Drosophila_grimshawi.dgri_caf1.dna.toplevel.fa
Drosophila_mojavensis.dmoj_caf1.dna.toplevel.fa
Drosophila_persimilis.dper_caf1.dna.toplevel.fa
Drosophila_sechellia.dsec_caf1.dna.toplevel.fa
Drosophila_willistoni.dwil_caf1.dna.toplevel.fa
Drosophila_yakuba.dyak_caf1.dna.toplevel.fa
Culex_quinquefasciatus.CpipJ2.dna.toplevel.fa
Anopheles_darlingi.AdarC3.dna.toplevel.fa
Anopheles_gambiae.AgamP4.dna.toplevel.fa

4. DOWLOADED-SCRIPT
```
# Drosophila melanogaster = Dmel = 
wget "https://ftp.ensembl.org/pub/release-113/fasta/drosophila_melanogaster/dna/Drosophila_melanogaster.BDGP6.46.dna.toplevel.fa.gz"
gunzip Drosophila_melanogaster.BDGP6.46.dna.toplevel.fa.gz
cp {,0001_}Drosophila_melanogaster.BDGP6.46.dna.toplevel.fa

# Drosophila ananassae = Dana = 
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/fasta/drosophila_ananassae/dna/Drosophila_ananassae.dana_caf1.dna.toplevel.fa.gz"
gunzip Drosophila_ananassae.dana_caf1.dna.toplevel.fa.gz
cp {,0001_}Drosophila_ananassae.dana_caf1.dna.toplevel.fa

# Drosophila erecta = Dere = 
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/fasta/drosophila_erecta/dna/Drosophila_erecta.dere_caf1.dna.toplevel.fa.gz"
gunzip Drosophila_erecta.dere_caf1.dna.toplevel.fa.gz
cp {,0001_}Drosophila_erecta.dere_caf1.dna.toplevel.fa

# Drosophila pseudoobscura pseudoobscura = Dpse = 
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/fasta/drosophila_pseudoobscura/dna/Drosophila_pseudoobscura.Dpse_3.0.dna.toplevel.fa.gz"
gunzip Drosophila_pseudoobscura.Dpse_3.0.dna.toplevel.fa.gz
cp {,0001_}Drosophila_pseudoobscura.Dpse_3.0.dna.toplevel.fa

# Drosophila simulans = Dsim = 
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/fasta/drosophila_simulans/dna/Drosophila_simulans.ASM75419v3.dna.toplevel.fa.gz"
gunzip Drosophila_simulans.ASM75419v3.dna.toplevel.fa.gz
cp {,0001_}Drosophila_simulans.ASM75419v3.dna.toplevel.fa

# Drosophila virilis = Dvir = 
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/fasta/drosophila_virilis//dna/Drosophila_virilis.dvir_caf1.dna.toplevel.fa.gz"
gunzip Drosophila_virilis.dvir_caf1.dna.toplevel.fa.gz
cp {,0001_}Drosophila_virilis.dvir_caf1.dna.toplevel.fa

# Drosophila grimshawi = Dgri = 
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/fasta/drosophila_grimshawi/dna/Drosophila_grimshawi.dgri_caf1.dna.toplevel.fa.gz"
gunzip Drosophila_grimshawi.dgri_caf1.dna.toplevel.fa.gz
cp {,0001_}Drosophila_grimshawi.dgri_caf1.dna.toplevel.fa

# Drosophila mojavensis = Dmoj = 
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/fasta/drosophila_mojavensis/dna/Drosophila_mojavensis.dmoj_caf1.dna.toplevel.fa.gz"
gunzip Drosophila_mojavensis.dmoj_caf1.dna.toplevel.fa.gz
cp {,0001_}Drosophila_mojavensis.dmoj_caf1.dna.toplevel.fa

Drosophila persimilis = Dper = 
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/fasta/drosophila_persimilis/dna/Drosophila_persimilis.dper_caf1.dna.toplevel.fa.gz"
gunzip Drosophila_persimilis.dper_caf1.dna.toplevel.fa.gz
cp {,0001_}Drosophila_persimilis.dper_caf1.dna.toplevel.fa

Drosophila sechellia = Dsec = 
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/fasta/drosophila_sechellia/dna/Drosophila_sechellia.dsec_caf1.dna.toplevel.fa.gz"
gunzip Drosophila_sechellia.dsec_caf1.dna.toplevel.fa.gz
cp {,0001_}Drosophila_sechellia.dsec_caf1.dna.toplevel.fa

Drosophila willistoni = Dwil = 
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/fasta/drosophila_willistoni/dna/Drosophila_willistoni.dwil_caf1.dna.toplevel.fa.gz"
gunzip Drosophila_willistoni.dwil_caf1.dna.toplevel.fa.gz
cp {,0001_}Drosophila_willistoni.dwil_caf1.dna.toplevel.fa

Drosophila yakuba = Dyak = 
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/fasta/drosophila_yakuba/dna/Drosophila_yakuba.dyak_caf1.dna.toplevel.fa.gz"
gunzip Drosophila_yakuba.dyak_caf1.dna.toplevel.fa.gz
cp {,0001_}Drosophila_yakuba.dyak_caf1.dna.toplevel.fa

culex_quinquefasciatus
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/fasta/culex_quinquefasciatus/dna/Culex_quinquefasciatus.CpipJ2.dna.toplevel.fa.gz"
gunzip Culex_quinquefasciatus.CpipJ2.dna.toplevel.fa.gz
cp {,0001_}Culex_quinquefasciatus.CpipJ2.dna.toplevel.fa

anopheles_darlingi
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/fasta/anopheles_darlingi/dna/Anopheles_darlingi.AdarC3.dna.toplevel.fa.gz"
gunzip Anopheles_darlingi.AdarC3.dna.toplevel.fa.gz
cp {,0001_}Anopheles_darlingi.AdarC3.dna.toplevel.fa

anopheles_gambiae
wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/fasta/anopheles_gambiae/dna/Anopheles_gambiae.AgamP4.dna.toplevel.fa.gz"
gunzip Anopheles_gambiae.AgamP4.dna.toplevel.fa.gz
cp {,0001_}Anopheles_gambiae.AgamP4.dna.toplevel.fa

```
5. SOFTWARE-VERSION
zsh 5.9 (arm64-apple-darwin24.0)

6. METHODS/WORKFLOWS


### Run script 0001_script.py

Annotation file filtering

```python 3.12.4 # script: 0001_script.py
# splits attribute column and stores in dictionary called later in atr
# 9th column from the gtf

def parse_attributes(attr_string):
    attrs = {}
    # The attribute string is split by semicolons (;), which separates
    # individual attributes
    for attr in attr_string.strip().split(';'):
        if attr:
            # Each attribute is split by the first space, with key
            # holding the attribute name
            key, value = attr.strip().split(' ', 1)
            # The value is stripped of quotes (") and stored in a dictionary
            # attrs with the attribute name as the key
            attrs[key] = value.strip('"')
    return attrs


# get new gtf 'earliest and/or only three_prime_utr per gene_id'

def extr_gtf(file_path):
    gene_utrs = {}

    with open(file_path, 'r') as file:
        for line in file:
            # skip this coment ('#')
            if line.startswith('#'):
                continue
            # Ensures the line is well-formated
            fields = line.strip().split('\t')
            if len(fields) != 9:
                continue
            # keep the the genes with the 'three_prime_utr'
            feature_type = fields[2]
            if feature_type != 'three_prime_utr':
                continue
            # Parses the 9th column attributes
            attributes = parse_attributes(fields[8])
            # Retrieves the gene_id
            gene_id = attributes.get('gene_id')
            if not gene_id:
                continue
            # Integer convert of the end and the start position
            start = int(fields[3])
            end = int(fields[4])
            # Finds the earliest 3'UTR, also if there is only 1 3'UTR 
            if gene_id not in gene_utrs or start < gene_utrs[gene_id]['start']:
                gene_utrs[gene_id] = {
                    'line': line.strip().replace("three_prime_utr",gene_id),
                    'start': start,
                    'end': end
                }
    out = []
    for gene_id, utr_info in gene_utrs.items():
        # Built the Output
        out.append(utr_info['line']+"\n")
    return (out)

import os
os.chdir("/Users/alejandraescos/Documents/drifter_dfr/0001_raw_data/data")

with open("0002_first_3utr_genes.gtf","w") as f:
    f.writelines(extr_gtf("0001_Drosophila_melanogaster.BDGP6.46.113.gtf"))
```

### getfasta program

Use getfasta program to extract the sequence of the 3'UTR using:
https://bedtools.readthedocs.io/en/latest/content/tools/getfasta.html

New gtf : 0002_first_3utr_genes.gtf
FASTA: 0003_Drosophila_melanogaster.BDGP6.46.dna.toplevel.fa

```zsh 5.9 (arm64-apple-darwin24.0)
# brew tap homebrew/science # Install from homebrew
# brew install bedtools
cd /Users/alejandraescos/Documents/drifter_dfr/0001_raw_data/data
bedtools getfasta -fi 0003_Drosophila_melanogaster.BDGP6.46.dna.toplevel.fa -bed 0002_first_3utr_genes.gtf -name > 0004_first_3utr_sequences.fa
```



```python 3.12.4
# View the first 10 lines of your file
with open('first_3utr_genes.gtf', 'r') as file:
    for i, line in enumerate(file):
        if i >= 10:  # Stop after the 10th line
            break
        print(line.strip())  # Print each line without extra newlines
```
### Trim sequences before prediction

Trim the file to take the 60 or 100 first nt of the 3'UTR

- trim_length = 100
- trim_length = 60

```zsh 5.9 (arm64-apple-darwin24.0)
cd /Users/alejandraescos/Documents/drifter_dfr/0001_raw_data
ls -lahtr
python3 0002_script_trim.py
```

```python 3.12.4 # script 0002_script_trim.py
# simple .py script, concatenate, trim, save fasta nucl sequences

def read_fasta(file_path):
    with open(file_path, 'r') as file:
        header = ''
        sequence = ''
        for line in file:
            if line.startswith('>'):
                if header:  # If already processed seq
                    yield (header, sequence)
                header = line.strip()
                sequence = ''
            else:
                sequence += line.strip()
        if header:  # for last seq
            yield (header, sequence)

def save_trimmed_fasta(input_file, output_file, trim_length):
    with open(output_file, 'w') as out_file:
        for header, sequence in read_fasta(input_file):
            trimmed_sequence = sequence[:trim_length]
            out_file.write(f"{header}\n{trimmed_sequence}\n")

# settings
input_file = '/Users/alejandraescos/Documents/drifter_dfr/0001_raw_data/data/0004_first_3utr_sequences.fa'
output_file = '/Users/alejandraescos/Documents/drifter_dfr/0001_raw_data/data/0004_first_3utr_sequences_trimmed_100nt.fa'
trim_length = 100

save_trimmed_fasta(input_file, output_file, trim_length)

trim_length = 60
output_file = '/Users/alejandraescos/Documents/drifter_dfr/0001_raw_data/data/0004_first_3utr_sequences_trimmed_60nt.fa'
save_trimmed_fasta(input_file, output_file, 60)
```

Installation of RNA Vienna package.

[Download RNA Vienna package]: (https://www.tbi.univie.ac.at/RNA/#download)


```zsh 5.9 (arm64-apple-darwin24.0)
cd /Users/alejandraescos/Downloads

tar -zxvf ViennaRNA-2.7.0.tar.gz
cd ViennaRNA-2.7.0
./configure
make
sudo make install

# password from the computer
# confirm installation
RNAsubopt --help
```

### RNA Vienna run

```zsh 5.9 (arm64-apple-darwin24.0)
cd /Users/alejandraescos/Documents/drifter_dfr/0001_raw_data/data
RNAsubopt --stochBT_en=3 < 0004_first_3utr_sequences_trimmed_60nt.fa > 0005_first_3utr_sequences_trimmed_60nt_subopt.txt

cd /Users/alejandraescos/Documents/drifter_dfr/0001_raw_data/data
RNAsubopt --stochBT_en=3 < 0004_first_3utr_sequences_trimmed_100nt.fa > 0005_first_3utr_sequences_trimmed_100nt_subopt.txt

cd /Users/alejandraescos/Documents/drifter_dfr/0001_raw_data/data
RNAfold --stochBT_en=3 < 0004_first_3utr_sequences_trimmed_60nt.fa > 0005_first_3utr_sequences_trimmed_60nt_fold.txt

cd /Users/alejandraescos/Documents/drifter_dfr/0001_raw_data/data
RNAfold --stochBT_en=3 < 0004_first_3utr_sequences_trimmed_100nt.fa > 0005_first_3utr_sequences_trimmed_100nt_fold.txt

# Move the files to another folder
mv "/Users/alejandraescos/Documents/drifter_dfr/0001_raw_data/data/0005_first_3utr_sequences_trimmed_60nt_fold.txt" \
"/Users/alejandraescos/Documents/drifter_dfr/0001_raw_data/data/0005_first_3utr_sequences_trimmed_100nt_fold.txt" \
"/Users/alejandraescos/Documents/drifter_dfr/0003_rna_fold/data"

mv "/Users/alejandraescos/Documents/drifter_dfr/0001_raw_data/data/0005_first_3utr_sequences_trimmed_60nt_fold.txt" \
"/Users/alejandraescos/Documents/drifter_dfr/0001_raw_data/data/0005_first_3utr_sequences_trimmed_100nt_fold.txt" \
"/Users/alejandraescos/Documents/drifter_dfr/0003_rna_fold/data"
```

### Hairpin
Detect hair pin and then do different versions of this script for:
100 nt
60 nt

```zsh 5.9 (arm64-apple-darwin24.0)
cd /Users/alejandraescos/Documents/drifter_dfr/0003_rna_fold
python3 0003_script_hairpin_100nt.py 
python3 0003_script_hairpin_60nt.py
```

then also change the configuration of the hairpin:
Length_min = 35

The output version of the files will be:


```python 3.12.4, 20241118 # 0003_script_hairpin_100nt.py or # 0003_script_hairpin_60nt.py
import re
import csv
import sys

# Config
length_min = 35
loop_min = 3
loop_max = 10
bulge_max = 2

input_file = '/Users/alejandraescos/Documents/drifter_dfr/0003_rna_fold/data/0005_first_3utr_sequences_trimmed_100nt_subopt.txt'
output_file = '/Users/alejandraescos/Documents/drifter_dfr/0003_rna_fold/data/0006_first_3utr_sequences_trimmed_hairpin_100nt.tsv'

def hairpin_check(candidate_hairpin, length_min, loop_min, bulge_max):
    middle_match = re.search((r'\((\.+)\)'), candidate_hairpin)
    if middle_match:
        middle_start = middle_match.start(1)  # refers only to the enclosed dots (group(1)), not the bracket
        middle_end = middle_match.end(1)
    if not middle_match or len(middle_match.group(1)) < loop_min\
            or len(middle_match.group(1)) > loop_max:
        print(f'Rejected!')
        return 'N', candidate_hairpin

    num_dots = (bulge_max + 1) * '\.'
    too_many_dots_upstream = re.compile(rf'\(({num_dots}+)\(')
    too_many_dots_downstream = re.compile(rf'\)({num_dots}+)\)')
    reversed_upstream = candidate_hairpin[:middle_start][::-1]  # reverse upstream for right-to-left search
    match_upstream = too_many_dots_upstream.search(reversed_upstream)
    match_downstream = too_many_dots_downstream.search(candidate_hairpin[middle_end:])
    if match_upstream:
        # Calculates original index in the non-reversed upstream part
        candidate_hairpin = candidate_hairpin[len(reversed_upstream) - match_upstream.start() - 1:]
    if match_downstream:
        middle_match = re.search((r'\((\.+)\)'), candidate_hairpin)  # recalculate, as positions changed
        if middle_match:
            middle_end = middle_match.end(1)
        candidate_hairpin = candidate_hairpin[:middle_end + match_downstream.start() + 1]

    open_count_pre = candidate_hairpin.count('(')
    close_count_pre = candidate_hairpin.count(')')
    diff = abs(open_count_pre - close_count_pre)

    if open_count_pre > close_count_pre:  # trimming to balance brackets
        list_hairpin = list(candidate_hairpin)  # converting to list to easily skip dots
        removed = 0
        for i in range(len(list_hairpin)):
            if list_hairpin[i] == '(':
                list_hairpin[i] = ''
                removed += 1
                if removed == diff:
                    break
        candidate_hairpin = ''.join(list_hairpin)  # converting back

    if open_count_pre < close_count_pre:
        list_hairpin = list(candidate_hairpin[::-1])  # same as above but in reverse
        removed = 0
        for i in range(len(list_hairpin)):
            if list_hairpin[i] == ')':
                list_hairpin[i] = ''
                removed += 1
                if removed == diff:
                    break
        list_hairpin.reverse()  # re-reverse
        candidate_hairpin = ''.join(list_hairpin)  # converting back

    candidate_hairpin = candidate_hairpin.strip('.')  # stripping possible trailing '.' after balancing

    print(f'Post-trimming: {candidate_hairpin}')

    hairpin_length = len(candidate_hairpin)
    if hairpin_length < length_min:
        print(f'Hairpin too short!')
        return 'N', candidate_hairpin
    if hairpin_length >= length_min:
        print(f'Hairpin found!')
        return 'Y', candidate_hairpin
    else:
        print(f'Rejected!')
        return 'N', candidate_hairpin

def parse_rnafold_hairpin(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    data = []
    gene_id = None
    rna = None

    for i, line in enumerate(lines):
        if line.startswith('>'):
            #gene_id_match = re.search(r'gene:([^;]+);', line)
            gene_id_match = re.search(r">(FBgn\d+):", line)
            if gene_id_match:
                gene_id = gene_id_match.group(1)
        elif line.startswith(('A', 'U', 'G', 'C')):
            rna = line.strip()
        elif line.startswith(('.', '(', ')')):
            # Extract MFE value
            mfe_match = re.search(r'\s+([-\d.]+)\s+', line)
            mfe = mfe_match.group(1) if mfe_match else None

            # Process structure
            temp_structure = line.strip()
            structure_parts = temp_structure.split()
            if structure_parts:
                trimmed_structure = structure_parts[0] + '('  # Add '(' at the end

            print(f"Processing: {gene_id}, {trimmed_structure}")  # Debug print

            if trimmed_structure and gene_id:
                start_position = None
                final_position = None
                candidate_hairpin = None
                result = 'N'
                for position, char in enumerate(trimmed_structure):
                    if char == '(' and start_position is None:
                        start_position = position
                    elif char == ')':
                        final_position = position
                    elif char == '(' and final_position is not None:
                        candidate_hairpin = trimmed_structure[start_position:final_position + 1]
                        print(f"Candidate hairpin: {candidate_hairpin}")
                        result, candidate_hairpin = hairpin_check(candidate_hairpin, length_min, loop_min, bulge_max)
                        print(f'Data appended.')
                        if result == 'Y':
                            # Hairpin position updated
                            pattern = re.escape(candidate_hairpin)
                            match = re.search(pattern, trimmed_structure[:-1])
                            if match:
                                exact_start = match.start()
                                exact_end = match.end()
                                rna_segment = rna[exact_start:exact_end] if rna else None
                                data.append([gene_id, result, trimmed_structure[:-1],
                                             candidate_hairpin, exact_start, exact_end,
                                             rna_segment, mfe])
                                break
                        else:
                            start_position = position
                            final_position = None
                if result == 'N':
                    data.append([gene_id, result, trimmed_structure[:-1], candidate_hairpin,  # Remove the added '(' when storing
                               start_position, final_position, rna, mfe])

    # Write output
    headers = ['GeneID', 'Hairpin', 'Trimmed_Str', 'Candidate_Hairpin_Str', 'StartPos', 'EndPos', 'RNA', 'MFE']

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f, delimiter='\t', quoting=csv.QUOTE_NONE)
        writer.writerow(headers)
        writer.writerows(data)
        print(f"Written to TSV: {output_file}")

    return data


parse_rnafold_hairpin(input_file, output_file)
```
### 


```R
rm(list = ls())

library(dplyr)
library(tidyr)

# Read tables
subopt_100 <- read.delim('/Users/alejandraescos/Documents/drifter_dfr/0003_rna_fold/data/0006_first_3utr_sequences_trimmed_hairpin_100nt.tsv', header = TRUE)
subopt_60 <- read.delim('/Users/alejandraescos/Documents/drifter_dfr/0003_rna_fold/data/0006_first_3utr_sequences_trimmed_hairpin_60nt.tsv', header = TRUE)
jungreis <- read.delim('/Users/alejandraescos/Documents/drifter_dfr/0004_tables_fig/table_fig/jungreis_genelist_2016.txt')

# filtering
subopt_Y <- subopt_100 %>% filter(Hairpin == 'Y')
jungreis_15 <- jungreis %>% filter(RT.length..codons. > 15)
jungreis_30 <- jungreis %>% filter(RT.length..codons. > 30)
subopt_early <- subopt_100 %>% filter(Hairpin == 'Y', StartPos > 8, StartPos < 26)

# Rename Gene.ID to GeneID
jungreis_15 <- jungreis_15 %>% rename(GeneID = Gene.ID)
jungreis_30 <- jungreis_30 %>% rename(GeneID = Gene.ID)

# Intersect
Y_15 <- intersect(subopt_Y$GeneID, jungreis_15$GeneID)
Y_30 <- intersect(subopt_Y$GeneID, jungreis_30$GeneID)
early_15 <- intersect(subopt_early$GeneID, jungreis_15$GeneID)
early_30 <- intersect(subopt_early$GeneID, jungreis_30$GeneID)

# write
#write.table(subopt_Y, "genes_hairpin.csv",
            #row.names=F, col.names=F, quote=F)
#write.table(subopt_early, "genes_early_hairpin.csv",
            #row.names=F, col.names=F, quote=F)

write.table(subopt_Y$GeneID, "genes_hairpin.csv",
            row.names=F, col.names=F, quote=F)
write.table(subopt_early$GeneID, "genes_early_hairpin.csv",
            row.names=F, col.names=F, quote=F)

write.table(Y_15, "genes_hairpin_over_15_codon_RT.csv",
            row.names=F, col.names=F, quote=F)
write.table(Y_30, "genes_hairpin_over_30_codon_RT.csv",
            row.names=F, col.names=F, quote=F)
write.table(early_15, "genes_early_hairpin_over_15_codon_RT.csv",
            row.names=F, col.names=F, quote=F)
write.table(early_30, "genes_early_hairpin_over_30_codon_RT.csv",
            row.names=F, col.names=F, quote=F)
```
### Venn diagrams with venny4py

```Zsh
pip install venny4py
```

```python 3.12.4, 20241125

import os
# Change working directory
os.chdir("/Users/alejandraescos/Documents/drifter_dfr/0004_tables_fig/table_fig")

# Verify the new working directory
print(os.getcwd())

import pandas as pd
set_A = pd.read_csv("genes_early_hairpin_60.csv")
set_B = pd.read_csv("genes_early_hairpin.csv")
set_C = pd.read_csv("genes_hairpin_60.csv")
set_D = pd.read_csv("genes_hairpin.csv")
set_E = pd.read_csv("genes_Ioannis_hairpin.csv")
set_F = pd.read_csv("jungreis_15.csv")
set_G = pd.read_csv("jungreis_30.csv")
set_H = pd.read_csv("jungreis.csv")


# Convert the DataFrame column to a Python list
set_A_python_list = set_A.iloc[:, 0].tolist()
set_B_python_list = set_B.iloc[:, 0].tolist()
set_C_python_list = set_C.iloc[:, 0].tolist()
set_D_python_list = set_D.iloc[:, 0].tolist()
set_E_python_list = set_E.iloc[:, 0].tolist()
set_F_python_list = set_F.iloc[:, 0].tolist()
set_G_python_list = set_G.iloc[:, 0].tolist()
set_H_python_list = set_H.iloc[:, 0].tolist()

#dict of sets
from venny4py.venny4py import *

# Define the sets
sets = {
    'Set1_Ioannis': set(set_E_python_list),
    'Set2_AE': set(set_D_python_list),
    'Set3_Jungreis': set(set_H_python_list)
}

# Generate and display the Venn diagram
venny4py(sets=sets)
```

