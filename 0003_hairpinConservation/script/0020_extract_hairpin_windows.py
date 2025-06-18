#!/usr/bin/env python3
"""
extract_hairpin_windows.py

Batch-process Stockholm (.sto) alignments to extract the first 60 non-gap
reference positions from D. melanogaster, trimming all alignment columns accordingly.

Steps:
 1. Parse header lines and aligned sequences.
 2. Identify the D. melanogaster reference sequence by substring match.
 3. Locate the first 60 non-gap characters in the reference.
 4. Trim alignment to include only those alignment columns.
 5. Write trimmed Stockholm to output directory.
"""

import argparse
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def parse_stockholm(path: Path):
    headers, ids, seqs = [], [], {}
    for line in path.read_text().splitlines():
        if not line or line == '//':
            continue
        if line.startswith('# STOCKHOLM'):
            continue
        elif line.startswith('#'):
            headers.append(line)
        else:
            parts = line.split(None, 1)
            if len(parts) != 2:
                logging.error(f"Could not parse line: {line}")
                continue
            sid, aln = parts
            if sid not in ids:
                ids.append(sid)
                seqs[sid] = aln
            else:
                seqs[sid] += aln
    return headers, ids, seqs


def trim_window(headers, ids, seqs, ref_key, length):
    # Identify reference sequence
    ref_id = next((sid for sid in ids if ref_key in sid), None)
    if ref_id is None:
        logging.error(f'Reference \"{ref_key}\" not found. Skipping.')
        return None

    ref_seq = seqs[ref_id]

    # Find alignment index for the 60th non-gap character
    count = 0
    for i, letter in enumerate(ref_seq):
        if letter != "-":
            count += 1
        if count == 33:
            startpos = i + 1
        if count == length+33:
            endpos = i + 1
            break
    else:
        logging.warning(f"Fewer than {length} non-gap characters found in {ref_id}")
        return None

    # Trim all sequences to alignment positions 0 to i (inclusive)
    trimmed_seqs = {sid: seq[startpos:endpos] for sid, seq in seqs.items()}
    return headers, ids, trimmed_seqs


def write_stockholm(out_path: Path, headers, ids, seqs):
    with out_path.open('w') as out:
        out.write('# STOCKHOLM 1.0\n')
        for h in headers:
            out.write(f'{h}\n')
        for sid in ids:
            out.write(f'{sid}\t{seqs[sid]}\n')
        out.write('//\n')


def main():
    p = argparse.ArgumentParser()
    p.add_argument('-i', '--input-dir', required=True, help='Directory of .sto files')
    p.add_argument('-o', '--output-dir', required=True, help='Output directory')
    p.add_argument('-r', '--ref-key', default='Drosophila_melanogaster', help='Reference ID substring')
    p.add_argument('-L', '--window-length', type=int, default=60, help='Number of ungapped nts to extract')
    args = p.parse_args()

    indir = Path(args.input_dir)
    outdir = Path(args.output_dir)
    outdir.mkdir(parents=True, exist_ok=True)

    for sto in sorted(indir.glob('*.sto')):
        headers, ids, seqs = parse_stockholm(sto)
        res = trim_window(headers, ids, seqs, args.ref_key, args.window_length)
        if not res:
            continue
        h2, ids2, seqs2 = res
        out_sto = outdir / sto.name
        write_stockholm(out_sto, h2, ids2, seqs2)
        logging.info(f'Wrote trimmed alignment: {out_sto.name}')


if __name__ == '__main__':
    main()
