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

def process_fasta(input_path: Path, output_fa: Path, max_len: int):
    # 1) load all sequences into memory, trimming headers
    seqs = {}
    with input_path.open() as in_h:
        current_id = None
        current_seq = []
        for line in in_h:
            if line.startswith('>'):
                # flush previous
                if current_id is not None:
                    seqs[current_id] = ''.join(current_seq)
                # new header, trimmed
                raw = line[1:].rstrip('\n')
                header = raw[:max_len]
                current_id = header
                current_seq = []
            else:
                current_seq.append(line.strip())
        # last one
        if current_id is not None:
            seqs[current_id] = ''.join(current_seq)

    # 2) compute pad length
    max_seq_len = max(len(s) for s in seqs.values())

    # 3) write trimmed + padded FASTA
    with output_fa.open('w') as out_h:
        for hdr, seq in seqs.items():
            padded = seq.ljust(max_seq_len, '-')
            out_h.write(f'>{hdr}\n')
            # wrap at 80 chars
            for i in range(0, len(padded), 80):
                out_h.write(padded[i:i+80] + '\n')

    # 4) convert to Stockholm
    sto_path = output_fa.with_suffix('.sto')
    with sto_path.open('w') as sto_h:
        subprocess.run(
            ['esl-reformat', 'stockholm', str(output_fa)],
            stdout=sto_h,
            check=True
        )

def main():
    p = argparse.ArgumentParser(
        description="Batch-trim, pad, and Stockholm-reformat FASTA files."
    )
    p.add_argument('-i','--input-dir',  required=True,
                   help="Directory of input FASTA files")
    p.add_argument('-o','--output-dir', required=True,
                   help="Where to write processed FASTA + .sto")
    p.add_argument('-l','--length', type=int, default=32,
                   help="Max header length (excluding '>')")
    p.add_argument('-e','--ext', default='.fa',
                   help="FASTA extension to process (default: .fa)")
    args = p.parse_args()

    indir  = Path(args.input_dir)
    outdir = Path(args.output_dir)
    if not indir.is_dir():
        print(f"ERROR: input-dir not found: {indir}", file=sys.stderr)
        sys.exit(1)
    outdir.mkdir(parents=True, exist_ok=True)

    # collect files
    files = sorted(indir.glob(f'*{args.ext}'))
    if not files:
        print(f"No *{args.ext} files in {indir}", file=sys.stderr)
        sys.exit(1)

    for f in files:
        out_fa = outdir / f.name
        print(f"→ {f.name}  ⇒  {out_fa.name} + {out_fa.with_suffix('.sto').name}")
        try:
            process_fasta(f, out_fa, args.length)
        except subprocess.CalledProcessError as e:
            print(f"  ✗ error on {f.name}: {e}", file=sys.stderr)

if __name__ == '__main__':
    main()

