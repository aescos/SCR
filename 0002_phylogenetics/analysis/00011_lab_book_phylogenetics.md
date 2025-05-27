Basic structure:
1.  DATA-ORIGIN:
2.  DATA-DATE:
3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
6.  METHODS/WORKFLOWS

drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

### With BUSCO file, now perform BUSCO phylogenetics to generate protein alignment
You can install the BUSCO_Phylogenomics package with Conda from the Bioconda channel
https://github.com/jamiemcg/BUSCO_phylogenomics

1.  DATA-ORIGIN:
path(/Users/alejandraescos/Documents/github/SCR/0002_phylogenetics/data)

2.  DATA-DATE:
20250508

3.  DATA-VERSION:
SUPERMATRIX.fasta

4.  DOWLOADED-SCRIPT:
```zsh
conda create -n BUSCO_phylogenomics -c bioconda busco_phylogenomics
conda activate BUSCO_phylogenomics
cd /Users/alejandraescos/BUSCO_phylogenomics
ln -s /Users/alejandraescos/Documents/github/SCR/0002_phylogenetics/data/0002_BUSCO_results ./BUSCO_results

python BUSCO_phylogenomics.py -i BUSCO_results -o 0003_busco_phylogenomics -t 10 --supermatrix_only
```

5.  SOFTWARE-VERSION:
BUSCO_phylogenomics