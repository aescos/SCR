#!/usr/bin/env python3
import os
import glob

def read_fasta(file_path):
    with open(file_path, 'r') as file:
        header = ''
        sequence = ''
        for line in file:
            if line.startswith('>'):
                if header:
                    yield (header, sequence)
                header = line.strip()
                sequence = ''
            else:
                sequence += line.strip()
        if header:
            yield (header, sequence)

def save_trimmed_fasta(input_file, output_file, trim_length):
    with open(output_file, 'w') as out_file:
        for header, sequence in read_fasta(input_file):
            trimmed_sequence = sequence[:trim_length]
            out_file.write(f"{header}\n{trimmed_sequence}\n")

# settings
input_file = '/Users/alejandraescos/Documents/github/SCR/data/0003_dmle_3UTR.fa'
output_file = '/Users/alejandraescos/Documents/github/SCR/data/0004_dmle_3UTR_trim.fa'
trim_length = 60

save_trimmed_fasta(input_file, output_file, trim_length)