Basic structure:
1.  DATA-ORIGIN:
2.  DATA-DATE:
3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
6.  METHODS/WORKFLOWS

drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

### Trim sctockholm file


1.  DATA-ORIGIN:
path(/Users/alejandraescos/Documents/github/SCR/0002_phylogenetics/data)

2.  DATA-DATE:
20250512

3.  DATA-VERSION:
SUPERMATRIX.fasta

4.  DOWLOADED-SCRIPT:

```
python3 /Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/script/0020_extract_hairpin_windows.py \
  -i /Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/data/fa_chunks_trimmed \
  -o /Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/data/fa_chunks_trimmed_by_stop \
  -r 0005_Drosophila_melanogaster_dna \
  -L 60


```

```

```


5.  SOFTWARE-VERSION:

***ChatGPT***



3. Assess secondary-structure conservation
A. Using RNAz
Install: part of the Vienna-RNA package + RNAz.

Run on each MAF:

```
rnazWindow.pl --maf maf/${name}.maf --window 120 --slide 40 \
  | rnazCompute.pl > rnaz/${name}.rnaz
This splits the UTR alignment into overlapping windows (120 nt wide, 40 nt slide).

RNAz assigns a p-value and “RNA class” probability for each window.

Parse results to find windows with P > 0.5 (likely conserved structures) and map back to coordinates.

B. Using EvoFold (alternative)
EvoFold from UCSC also detects conserved RNA structures in MAF blocks; you’d need the phyloP tree model for Drosophila.
```