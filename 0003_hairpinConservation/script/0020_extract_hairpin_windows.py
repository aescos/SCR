#!/usr/bin/env python3
"""
extract_hairpin_windows.py

Batch-process Stockholm (.sto) alignments to extract ungapped 60-nt hairpin windows
immediately after the first in-frame stop codon in D. melanogaster, dropping any alignment
columns where the reference has a gap.

For each .sto file:
 1. Parse header lines, sequences, and SS_cons.
 2. Identify the D. melanogaster reference sequence by substring match.
 3. Build an ungapped index map from reference alignment to ungapped positions.
 4. Locate the first in-frame stop codon in the ungapped reference.
 5. Determine the next 60 ungapped reference positions and their alignment indices.
 6. Extract those columns for all species and the SS_cons line.
 7. Write a trimmed Stockholm to the output directory.

"""
import sys
import argparse
import logging
from pathlib import Path
import subprocess

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

STOP_CODONS = {"TAA", "TAG", "TGA"}


def parse_stockholm(path: Path):
    headers, ids, seqs, ss_cons = [], [], {}, None
    for line in path.read_text().splitlines():
        if not line or line == '//':
            continue
        if line.startswith('#=GC SS_cons'):
            parts = line.split(None, 3)
            ss_cons = parts[3] if len(parts) >= 4 else ''
        elif line.startswith('#'):
            headers.append(line)
        else:
            sid, aln = line.split(None, 1)
            if sid not in ids:
                ids.append(sid)
                seqs[sid] = aln
            else:
                seqs[sid] += aln
    return headers, ids, seqs, ss_cons


def trim_window(headers, ids, seqs, ss_cons, ref_key, length):
    # 1) find reference aligned sequence
    ref_id = next((sid for sid in ids if ref_key in sid), None)
    if ref_id is None:
        logging.error(f'Reference "{ref_key}" not found. Skipping.')
        return None
    aligned_ref = seqs[ref_id]

    # 2) build mapping: ungapped positions -> alignment indices
    map_idx = [i for i, b in enumerate(aligned_ref) if b != '-']
    ungapped = [aligned_ref[i] for i in map_idx]

    # 3) locate first in-frame stop codon in ungapped sequence
    stop_pos = None
    for u in range(0, len(ungapped)-2, 3):
        codon = ''.join(ungapped[u:u+3]).upper()
        if codon in STOP_CODONS:
            stop_pos = u+3
            break
    if stop_pos is None:
        logging.error(f'No in-frame stop codon found for {ref_id}. Skipping.')
        return None

    # 4) select next `length` ungapped positions
    start_idx = stop_pos
    end_idx = stop_pos + length
    if start_idx >= len(map_idx):
        logging.warning(f'Ref sequence shorter than offset {start_idx}, skipping.')
        return None
    if end_idx > len(map_idx):
        logging.warning(f'Only {len(map_idx)-start_idx} ungapped cols available; using available.')
        end_idx = len(map_idx)

    window_map = map_idx[start_idx:end_idx]

    # 5) extract columns for all species and SS_cons
    trimmed_seqs = {
        sid: ''.join(seqs[sid][i] for i in window_map)
        for sid in ids
    }
    trimmed_ss = ''.join(ss_cons[i] for i in window_map) if ss_cons else None
    return headers, ids, trimmed_seqs, trimmed_ss


def write_stockholm(out_path: Path, headers, ids, seqs, ss_cons):
    with out_path.open('w') as out:
        out.write('# STOCKHOLM 1.0\n')
        for h in headers:
            out.write(f'{h}\n')
        for sid in ids:
            out.write(f'{sid}\t{seqs[sid]}\n')
        if ss_cons is not None:
            out.write(f'#=GC SS_cons  {ss_cons}\n')
        out.write('//\n')


def extract_ref_fasta(seqs, ref_key, path: Path):
    ref_id = next(s for s in seqs if ref_key in s)
    seq = seqs[ref_id].replace('-', '')
    with path.open('w') as f:
        f.write(f'>{ref_id}\n')
        f.write(f'{seq}\n')
    return path


def run_subopt(fa_path: Path, out_path: Path, energy=3.0):
    cmd = ['RNAsubopt', '-e', str(energy)]
    with fa_path.open() as inf, out_path.open('w') as outf:
        subprocess.run(cmd, stdin=inf, stdout=outf, check=True)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('-i','--input-dir', required=True, help='Directory of .sto files')
    p.add_argument('-o','--output-dir', required=True, help='Output directory')
    p.add_argument('-r','--ref-key', default='Drosophila_melanogaster', help='Reference ID substring')
    p.add_argument('-L','--window-length', type=int, default=60, help='Number of ungapped nts to extract')
    p.add_argument('--do-subopt', action='store_true', help='Also extract Dmel FASTA and run RNAsubopt')
    args = p.parse_args()

    indir = Path(args.input_dir)
    outdir = Path(args.output_dir)
    outdir.mkdir(parents=True, exist_ok=True)
    fa_dir = outdir / 'ref_fastas'
    if args.do_subopt:
        fa_dir.mkdir(exist_ok=True)

    for sto in sorted(indir.glob('*.sto')):
        headers, ids, seqs, ss_cons = parse_stockholm(sto)
        res = trim_window(headers, ids, seqs, ss_cons, args.ref_key, args.window_length)
        if not res:
            continue
        h2, ids2, seqs2, ss2 = res
        out_sto = outdir / sto.name
        write_stockholm(out_sto, h2, ids2, seqs2, ss2)
        logging.info(f'Wrote window: {out_sto.name}')
        if args.do_subopt:
            fa = fa_dir / sto.with_suffix('.fa').name
            extract_ref_fasta(seqs2, args.ref_key, fa)
            sub = fa_dir / sto.with_suffix('.subopt').name
            run_subopt(fa, sub)
            logging.info(f'Generated subopt: {sub.name}')

if __name__=='__main__':
    main()

