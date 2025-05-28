drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

Seqs: Original raw data
data: Drosophila_melanogaster.BDGP6.46.113, ensembl
date: 20250312

step1: duplicate and rename original data
date: 20250401
data: 0001_dmle.fa, 0001_dmle.gtf
lab_book: 0001_lab_book_hairpin
zsh: zsh 5.9 (arm64-apple-darwin24.0)

step2: Annotation filtering of .gtf that takes the location of the earliest 
    (lowest 'start') 3' UTR per gene
date: 20250401
lab_book: 0002_lab_book_hairpin
data: use 0001_dmle.gtf to generate 0002_dmle_3UTR.gtf
python 3.12.4: 0002_gtf_split_atributes.py 

step3: Extract 3'UTR sequences from fasta using bedtools (0003_dmle_3UTR.fa)
date: 20250402
lab_book: 0003_lab_book_hairpin
data: use 0001_dmle.fa and 0002_dmle_3UTR.gtf to generate 0003_dmle_3UTR.fa
bedtools: https://bedtools.readthedocs.io/en/latest/content/tools/getfasta.html
zsh: zsh 5.9 (arm64-apple-darwin24.0)

step4: Trim the 3'UTR fasta file to 60 nt
date: 20250402
lab_book: 0004_lab_book_hairpin
data: use 0003_dmle_3UTR.fa to generate 0004_dmle_3UTR_trim.fa
python: 0004_trim.py

step5: RNAfold prediction of hairpin for al 3UTR sequences
date: 20250402
lab_book: 0005_lab_book_hairpin
data: 0004_dmle_3UTR_trim.fa to generate 0005_dmle_3UTR_trim_hairpin.txt
ViennaRNA-2.7.0 

step6: Filter hairpin conditions
date: 20250402
lab_book: 0006_lab_book_hairpin
data: use 0005_dmle_3UTR_trim_hairpin.txt to 
    generate 0006__dmle_3UTR_trim_60nt_subopt_select.tsv
python 3.12.4: 0006_hairpin_select.py
	# Config
	length_min = 35
	loop_min = 3
	loop_max = 10
	bulge_max = 2
	
step7: Select only Yes using R
