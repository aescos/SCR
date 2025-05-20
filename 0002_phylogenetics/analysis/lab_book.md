Basic structure:
1.  DATA-ORIGIN:
2.  DATA-DATE:
3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
6.  METHODS/WORKFLOWS
drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

# AIM
The aim of this project is to obtain the conservation of the 3'UTR from the first stop codon readthrough of vvl and CG6282.

Species I am going to use for the conservation of the sequence from FlyBase:

 Drosophila simulans
 Drosophila sechellia
 Drosophila melanogaster
 Drosophila yakuba
 Drosophila erecta
 Drosophila ananassae
 Drosophila pseudoobscura
 Drosophila persimilis
 Drosophila willistoni
 Drosophila mojavensis
 Drosofila virilis
Drosophila grimshawi ### This one did not appear in the blast.

I will add some mosquito species:

Anopheles arabiensis
Anopheles gambiae
anophieles coluzzii
Anopheles marshillii

## Step1: 
The document: vvl sequence gene.docx, was obtained with the following information.

1.  DATA-ORIGIN:
vvl from Drosohpila melanogaster gene sequence
https://flybase.org/decoratedfasta/FBgn0086680

2.  DATA-DATE: 
07APR2025

3.  DATA-VERSION:
FB2025_01 released February 20, 2025

## Step2:
### BLAST alignment
I did blast on the vvl gene sequence and obtained the file BLAST_vvl.txt and added the original vvl sequence (BLAST_vvl.fasta). Then I analysed the first 150 nt of the sequence with AliView habing always the original vvl sequence at the top (BLAST_vvl_150nt.fasta)

4.  DOWLOADED-SCRIPT:
Citation: Larsson, A. (2014). AliView: a fast and lightweight alignment viewer and editor for large data sets. Bioinformatics30(22): 3276-3278. http://dx.doi.org/10.1093/bioinformatics/btu531
https://ormbunkar.se/aliview/

5.  SOFTWARE-VERSION:
AliView: Download the latest stable version: 1.30 (4/Mar/2025) (Mac OS X, Windows, Linux)

6.  METHODS/WORKFLOWS:
I aligned with MUSCLE method

### Ensembl compare CACTUS alighment

1.  DATA-ORIGIN:
ensemble metazoan
2.  DATA-DATE:
10APR2025
3.  DATA-VERSION:
40 pangenome drosopila Cactus
4.  DOWLOADED-SCRIPT:
5.  SOFTWARE-VERSION:
6.  METHODS/WORKFLOWS:
Search for gene (vvl or CG6282), then go to "compare genomics" and select "40 pangenome drosopila Cactus". Finally ask to view the alignments. Here I downloaded in fasta format from locations:

CG6282 = 3L:8604657-8617074
vvl = 3L:6790158-6794941
