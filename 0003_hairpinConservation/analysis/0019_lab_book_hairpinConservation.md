Basic structure:
1.  DATA-ORIGIN:
2.  DATA-DATE:
3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
6.  METHODS/WORKFLOWS

drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

### Generate stockholm file with trimmed headers and pads sequences
**Trim & reformat your raw FASTAs → .sto.**
- Trims FASTA headers to at most 32 characters (so downstream tools with name-length limits won’t choke).

- Pads each alignment so that all sequences in a file are the same length (by adding - to the ends of shorter ones).

- Converts the padded .fa into Stockholm format (.sto) via esl-reformat stockholm.

1.  DATA-ORIGIN:
path(/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation)

2.  DATA-DATE:
20250526

3.  DATA-VERSION:
0018_fa_chunks folder

4.  DOWLOADED-SCRIPT:

```
python3 "/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/script/0019_presto.py" \
  -i "/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/data/0018_fa_chunks" \
  -o "/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/data/0019_fa_chunks_trimmed" \
  -l 32 \
  -e .fa
```

0019_presto.py
```
#!/usr/bin/env python3
"""
trim_fasta_headers_batch.py

Batch-trim FASTA headers, ensure aligned sequences have equal length,
then convert each to Stockholm format using esl-reformat.
"""
import sys
import argparse
import subprocess
from pathlib import Path


def trim_headers(in_handle, out_handle, max_len):
    """
    Trim each FASTA header to max_len characters (excluding '>')
    """
    for line in in_handle:
        if line.startswith('>'):
            header = line[1:].rstrip('\n')
            truncated = header[:max_len]
            out_handle.write(f'>{truncated}\n')
        else:
            out_handle.write(line)


def pad_alignment(fa_path: Path):
    """
    Ensure all sequences in this FASTA have the same length by padding
    shorter ones with '-' at the end.
    """
    # Read all sequences into memory
    seqs = {}
    current_id = None
    current_seq = []
    for line in fa_path.open('r'):
        line = line.rstrip('\n')
        if line.startswith('>'):
            if current_id is not None:
                seqs[current_id] = ''.join(current_seq)
            current_id = line
            current_seq = []
        else:
            current_seq.append(line)
    if current_id is not None:
        seqs[current_id] = ''.join(current_seq)

    # Compute max sequence length
    max_len = max(len(seq) for seq in seqs.values())

    # Rewrite FASTA with padded sequences
    with fa_path.open('w') as out_handle:
        for header, seq in seqs.items():
            padded = seq.ljust(max_len, '-')
            out_handle.write(f'{header}\n')
            # wrap at 80 chars per line for readability
            for i in range(0, len(padded), 80):
                out_handle.write(padded[i:i+80] + '\n')


def trim_and_stockholm(input_path: Path, output_fa: Path, max_len: int):
    """
    1) Trim headers
    2) Pad alignment for equal lengths
    3) Convert to Stockholm (.sto) alongside the .fa
    """
    # 1) Trim
    with input_path.open('r') as in_h, output_fa.open('w') as out_h:
        trim_headers(in_h, out_h, max_len)

    # 2) Pad
    pad_alignment(output_fa)

    # 3) Convert to Stockholm
    sto_path = output_fa.with_suffix('.sto')
    subprocess.run([
        'esl-reformat', 'stockholm', str(output_fa)
    ], stdout=sto_path.open('w'), check=True)


def main():
    parser = argparse.ArgumentParser(
        description="Batch-trim, pad, and Stockholm-reformat FASTA files."
    )
    parser.add_argument(
        '-i', '--input-dir',
        required=True,
        help="Directory containing input FASTA files",
        metavar="DIR"
    )
    parser.add_argument(
        '-o', '--output-dir',
        required=True,
        help="Directory to write processed files",
        metavar="DIR"
    )
    parser.add_argument(
        '-l', '--length',
        type=int,
        default=32,
        help="Maximum header length (excluding '>') [default: 32]"
    )
    parser.add_argument(
        '-e', '--extension',
        default='.fa',
        help="File extension to process (e.g., .fa, .fasta) [default: .fa]"
    )
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    if not input_dir.is_dir():
        print(f"Error: input directory '{input_dir}' not found.", file=sys.stderr)
        sys.exit(1)
    output_dir.mkdir(parents=True, exist_ok=True)

    files = list(input_dir.glob(f'*{args.extension}'))
    if not files:
        print(f"No files with extension '{args.extension}' in {input_dir}.", file=sys.stderr)
        sys.exit(1)

    for input_file in files:
        out_fa = output_dir / input_file.name
        print(f"Processing: {input_file.name} -> {out_fa.name} + {out_fa.with_suffix('.sto').name}")
        try:
            trim_and_stockholm(input_file, out_fa, args.length)
        except subprocess.CalledProcessError as e:
            print(f"Error on {input_file}: {e}", file=sys.stderr)

if __name__ == '__main__':
    main()
```

5.  SOFTWARE-VERSION:
python 3.12.4