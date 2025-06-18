Basic structure:
1.  DATA-ORIGIN:
2.  DATA-DATE:
3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
6.  METHODS/WORKFLOWS

drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

### Test sequence conservation with esl-alistat

1.  DATA-ORIGIN:
path(/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation)

2.  DATA-DATE:
20250527

3.  DATA-VERSION:
0020_fa_chunks_trimmed_by_stop

4.  DOWLOADED-SCRIPT:

Clean up duplicate Stockholm headers so downstream tools (e.g. esl-alistat) won’t complain.

```
cd /Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/data/0020_fa_chunks_trimmed_by_stop
mkdir -p 0021_fa_chunks_60nt_stats

for f in *.sto; do
  awk '
    NR==1 { print; next }
    $0 == "# STOCKHOLM 1.0" && NR==2 { next }
    { print }
  ' "$f" > 0021_fa_chunks_60nt_stats/"$f"
done
```
It performed the statistics of the sequence conservation
```
for a in 0020_fa_chunks_trimmed_by_stop/*.sto; do
  base=$(basename "$a" .sto)
  esl-alistat "$a" > 0020_fa_chunks_trimmed_by_stop/"$base".txt
done
```
it give this error:
   two # STOCKHOLM 1.0 headers in a row?
   while reading Stockholm file 0022_fa_chunks_60nt_stats/FBgn0038897_3R_21742688_21743987.sto
   at or near line 2
So I just go to that file, eliminate the extra header and re-run.

5.  SOFTWARE-VERSION:
Easel 0.46
esl-alistat :: show summary statistics for a multiple sequence alignment file
