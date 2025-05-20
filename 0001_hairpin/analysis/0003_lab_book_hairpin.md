drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

Basic structure:
1.  DATA-ORIGIN:
2.  DATA-DATE:
02042025
3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
Use getfasta program to extract the sequence of the 3'UTR using:
https://bedtools.readthedocs.io/en/latest/content/tools/getfasta.html

6.  METHODS/WORKFLOWS

```zsh 5.9 (arm64-apple-darwin24.0)
# brew tap homebrew/science # Install from homebrew
# brew install bedtools

bedtools getfasta -fi 0001_dmle.fa -bed 0002_dmle_3UTR.gtf -name > 0003_dmle_3UTR.fa
```