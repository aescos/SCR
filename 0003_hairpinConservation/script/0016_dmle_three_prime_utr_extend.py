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
