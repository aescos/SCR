#!/usr/bin/env python3
import sys
import argparse
import tempfile
from pathlib import Path
from Bio import AlignIO
from Bio.Align import MultipleSeqAlignment

def fix_maf(in_f, out_f):
    """
    Inject a dummy score column into any 's\t' lines so
    Biopython’s MAF parser won’t choke.
    """
    with open(in_f) as inp, open(out_f, 'w') as out:
        for line in inp:
            if line.startswith("s\t"):
                out.write("s " + line[2:])
            else:
                out.write(line)

def find_bad_species(maf_path, length_thresh, gap_thresh):
    """
    Return a set of sequence IDs whose first gap exceeds gap_thresh.
    """
    dic_start = {}
    dic_end   = {}
    first     = None

    for block_num, block in enumerate(AlignIO.parse(str(maf_path), "maf")):
        # reference = first row
        ref = block[0]
        start0 = ref.annotations['start']
        if block_num == 0:
            first = start0
        if start0 > first + length_thresh:
            break

        # record starts/ends
        for rec in block:
            sid = rec.id
            s   = rec.annotations['start']
            e   = s + rec.annotations['size']
            dic_start.setdefault(sid, []).append(s)
            dic_end  .setdefault(sid, []).append(e)

    bad = set()
    for sid, starts in dic_start.items():
        ends = dic_end[sid]
        for idx in range(len(starts)-1):
            if (starts[idx+1] - ends[idx]) > gap_thresh:
                bad.add(sid)
                break
    return bad

def filter_maf(in_maf, out_maf, bad_sids):
    """
    Read all MAF blocks in in_maf, drop any rows whose ID is in bad_sids,
    and write the result to out_maf.
    """
    filtered = []
    for block in AlignIO.parse(str(in_maf), "maf"):
        kept = [rec for rec in block if rec.id not in bad_sids]
        if kept:
            filtered.append(MultipleSeqAlignment(kept))
    with open(out_maf, 'w') as out:
        AlignIO.write(filtered, out, 'maf')

def main():
    p = argparse.ArgumentParser(
        description="Batch-fix MAFs and remove species with large gaps."
    )
    p.add_argument('-i','--input-dir',    required=True,
                   help="Directory containing input MAF files")
    p.add_argument('-o','--output-dir',   required=True,
                   help="Directory to write filtered MAFs")
    p.add_argument('-e','--extension',    default='.maf',
                   help="File extension to process [default: .maf]")
    p.add_argument('-l','--length-thresh',type=int, default=92,
                   help="Reference advance threshold [default: 92]")
    p.add_argument('-g','--gap-thresh',   type=int, default=0,
                   help="Gap-size threshold [default: 5]")
    args = p.parse_args()

    input_dir  = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    if not input_dir.is_dir():
        sys.exit(f"Error: input directory not found: {input_dir!r}")
    output_dir.mkdir(parents=True, exist_ok=True)

    maf_files = sorted(input_dir.glob(f"*{args.extension}"))
    if not maf_files:
        sys.exit(f"No files with extension '{args.extension}' in {input_dir}")

    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        for maf in maf_files:
            fixed = tmpdir / maf.name
            # 1) fix
            fix_maf(str(maf), str(fixed))
            # 2) find species to drop
            bad = find_bad_species(fixed,
                                   args.length_thresh,
                                   args.gap_thresh)
            # 3) write filtered MAF
            out_path = output_dir / maf.name
            filter_maf(fixed, out_path, bad)
            print(f"Filtered {maf.name}: dropped {len(bad)} species")

if __name__ == "__main__":
    main()
