drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

raw_data: Original raw data
data: From ensemble download protein and dna FASTA sequences
lab_book: 0000_lab_book_phylogenetics
date: 20250426 and 20250414

step1: parse protein sequence original data
date: 16042025
data: 0001_*_longest_isoform.fa
lab_book: 0001_lab_book_phylogenetics
zsh: python 3.12.4

step2: Perform BUSCO from orthoBD, to find all protein orthologs
date: 16042025
data: 0002_*_longest_isoform_busco folders
lab_book: 0002_lab_book_phylogenetics
zsh: zsh 5.9 (arm64-apple-darwin24.0)

step3: With BUSCO file, now perform BUSCO phylogenetics to generate protein alignment
matrix
date: 16042025
data: SUPERMATRIX.fasta
lab_book: 0003_lab_book_phylogenetics
zsh: zsh 5.9 (arm64-apple-darwin24.0)

step4: 
date: 16042025
data: 0002_*_longest_isoform_busco folders
lab_book: 0003_lab_book_phylogenetics
zsh: zsh 5.9 (arm64-apple-darwin24.0)