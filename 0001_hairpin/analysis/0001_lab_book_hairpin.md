Basic structure:
1.  DATA-ORIGIN:
2.  DATA-DATE:
3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
6.  METHODS/WORKFLOWS

drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

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

### Download GTF from ensemble of Drosophila melanogaster:

1.  DATA-ORIGIN: 
ensembl

2.  DATA-DATE: 
20250312

3.  DATA-VERSION: 
Drosophila_melanogaster.BDGP6.46.113

4.  DOWLOADED-SCRIPT:
```
# Drosophila melanogaster = dmel

wget "http://ftp.ensemblgenomes.org/pub/metazoa/current/gtf/drosophila_melanogaster/Drosophila_melanogaster.BDGP6.46.60.gtf.gz"
gunzip Drosophila_melanogaster.BDGP6.46.60.gtf.gz
cp Drosophila_melanogaster.BDGP6.46.60.gtf
# manually change the name to 0001_dmle.gtf
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

4. DOWLOADED-SCRIPT
```
# Drosophila melanogaster = Dmel = 
wget "https://ftp.ensembl.org/pub/release-113/fasta/drosophila_melanogaster/dna/Drosophila_melanogaster.BDGP6.46.dna.toplevel.fa.gz"
gunzip Drosophila_melanogaster.BDGP6.46.dna.toplevel.fa.gz
cp Drosophila_melanogaster.BDGP6.46.dna.toplevel.fa
# manually change the name to 0001_dmle.fa
```
5. SOFTWARE-VERSION
zsh 5.9 (arm64-apple-darwin24.0)

6. METHODS/WORKFLOWS

