drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

raw_data: Original raw data
data: From ensemble download protein and dna FASTA sequences
lab_book: 0008_lab_book_phylogenetics
date: 26042025 and 14042025

step1: Parse protein sequence original data
date: 02052025
data: 0001_*_longest_isoform.fa
lab_book: 0009_lab_book_phylogenetics
zsh: python 3.12.4

step2: Perform BUSCO from orthoBD, to find all protein orthologs
date: 05052025
data: 0002_BUSCO_results
lab_book: 0010_lab_book_phylogenetics
zsh: zsh 5.9 (arm64-apple-darwin24.0)

step3: With BUSCO file, now perform BUSCO phylogenetics to generate protein alignment
matrix
date: 08052025
data: 0003_busco_phylogenomics/SUPERMATRIX.fasta
lab_book: 0011_lab_book_phylogenetics
zsh: zsh 5.9 (arm64-apple-darwin24.0)

step4: IQ-tree2 to generate the Newick tree
date: 13052025
data: 0005_seqfile_newicktree.txt
lab_book: 0012_lab_book_phylogenetics
zsh: zsh 5.9 (arm64-apple-darwin24.0)

step5: Soft masking fo DNA sequences in preparation of CACTUS progressive
date: 13052025
data: 0002_*_longest_isoform_busco folders
lab_book: 0013_lab_book_phylogenetics
zsh: zsh 5.9 (arm64-apple-darwin24.0)

step6: CACTUS progressive pipeline
date: 18052025
data: 0005_seqfile.txt
lab_book: 0014_lab_book_phylogenetics
zsh: zsh 5.9 (arm64-apple-darwin24.0)