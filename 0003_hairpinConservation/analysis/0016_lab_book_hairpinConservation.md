Basic structure:
1.  DATA-ORIGIN:
2.  DATA-DATE:
3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
6.  METHODS/WORKFLOWS

drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

### +/- 33 from the stop codon, depending on strand location to the index of location

1.  DATA-ORIGIN:
path(/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation)

2.  DATA-DATE:
20250521

3.  DATA-VERSION:
0015_dmle_selected_three_prime_utr.bed

4.  DOWLOADED-SCRIPT:

Then I extended these nucleotides 33 before the start codon taking into accoun if the 3'UTR is in the + strand or if it is in the - strand.
0016_dmle_three_prime_utr_extend.py:
```
# Input and output file paths
input_bed = "/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/data/0015_dmle_selected_three_prime_utr.bed"
output_bed = "/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/data/0016_dmle_selected_three_prime_utr_extend.bed"

# Process the BED file
with open(input_bed, "r") as infile, open(output_bed, "w") as outfile:
    for line in infile:
        if line.strip() == "":
            continue  # Skip empty lines

        fields = line.strip().split("\t")
        chrom, start, end, name, score, strand = fields

        start = int(start)
        end = int(end)

        if strand == "+":
            start = max(0, start - 33)  # Ensure start doesn't go below 0
        elif strand == "-":
            end = end + 33

        # Write modified line
        outfile.write(f"{chrom}\t{start}\t{end}\t{name}\t{score}\t{strand}\n")
```

5.  SOFTWARE-VERSION:
python 3.12.4
