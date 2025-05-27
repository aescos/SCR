#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path
import glob

def load_hairpins(subopt_tsv):
    hp_map = {}
    with open(subopt_tsv) as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            parts = line.rstrip('\n').split('\t')
            gene = parts[0]
            hairpin = parts[1]
            hp_map[gene] = hairpin
    return hp_map

def annotate(sto_path, hairpin, out_path):
    # read all lines
    lines = sto_path.read_text().splitlines(keepends=True)
    # find first sequence line to get alignment length
    aln_len = None
    for L in lines:
        if L.startswith('#') or L.startswith('//') or not L.strip():
            continue
        try:
            seq = L.split()[1]
            aln_len = len(seq)
            break
        except:
            continue
    if aln_len is None:
        print(f"⚠️  {sto_path.name}: no sequence lines found, skipping.", file=sys.stderr)
        return

    # trim or pad hairpin
    if len(hairpin) > aln_len:
        hp_adj = hairpin[:aln_len]
    else:
        hp_adj = hairpin.ljust(aln_len, '.')

    # build output: inject SS_cons before the final //
    out = []
    for L in lines:
        if L.strip() == '//':
            out.append(f"#=GC SS_cons  {hp_adj}\n")
        out.append(L)
    out_path.write_text(''.join(out))

def main():
    p = argparse.ArgumentParser(
        description="Inject per-gene hairpin into each Stockholm alignment"
    )
    p.add_argument('-s','--subopt', required=True,
                   help="0007_subopt_Y_minMFE.txt")
    p.add_argument('-i','--sto-dir', required=True,
                   help="directory of windowed .sto files")
    p.add_argument('-o','--out-dir', required=True,
                   help="where to write *.annot.sto")
    args = p.parse_args()

    hp_map = load_hairpins(args.subopt)
    sto_dir = Path(args.sto_dir)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    for gene, hp in hp_map.items():
        sto_file = sto_dir / f"{gene}.sto"
        if not sto_file.exists():
            print(f"⚠️  Missing {sto_file.name}, skipping", file=sys.stderr)
            continue
    for gene, hp in hp_map.items():
         # look for any file named "<gene>_*.sto"
        pattern = sto_dir / f"{gene}_*.sto"
        matches = glob.glob(str(pattern))
        if not matches:
            print(f"⚠️  No .sto found matching {gene}_*.sto, skipping", file=sys.stderr)
            continue
        sto_file = Path(matches[0])   # pick the first match
            
        out_file = out_dir / f"{gene}.annot.sto"
        annotate(sto_file, hp, out_file)
        print(f"✅  {gene}: wrote {out_file.name}")

if __name__=="__main__":
    main()


