drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

step15: Have an index of locations of interest from the hairpin prediction
date: 20250521
data: 0007_subopt_Y_minMFE.bed
lab_book: 0015_lab_book_hairpinConservation
zsh: python 3.12.4

step16: +/- 33 from the stop codon, depending on strand location to the index of location
date: 20250521
data: 0015_dmle_selected_three_prime_utr.bed
lab_book: 0016_lab_book_hairpinConservation
zsh: python 3.12.4

step17: Obtain maf_chunks from HAL file
date: 20250526
data: 0016_dmle_selected_three_prime_utr_extend.bed
lab_book: 0017_lab_book_hairpinConservation
zsh: python 3.12.4

step18: Obtain fasta_chunks taking into account if + or - strand
date: 20250526
data: 0016_dmle_selected_three_prime_utr_extend.bed
lab_book: 0018_lab_book_hairpinConservation
zsh: python 3.12.4

step19: Generate stockholm file with trimmed headers and pads sequences
date: 20250526
data: 0018_fa_chunks folder
lab_book: 0019_lab_book_hairpinConservation
zsh: python 3.12.4

step20: Extract the 60‐nt windows right after the first stop codon from those .sto
date: 20250527
data: 0019_fa_chunks_trimmed
lab_book: 0020_lab_book_hairpinConservation
zsh: python 3.12.4

step21: Test sequence conservation with esl-alistat
date: 20250527
data: 0020_fa_chunks_trimmed_by_stop
lab_book: 0021_lab_book_hairpinConservation
zsh: Easel 0.46