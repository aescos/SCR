drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

Basic structure:
1.  DATA-ORIGIN:
2.  DATA-DATE:
02042025

3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
Installation of RNA Vienna package.

[Download RNA Vienna package]: (https://www.tbi.univie.ac.at/RNA/#download)

```zsh 5.9 (arm64-apple-darwin24.0)
cd /Users/alejandraescos/Downloads

tar -zxvf ViennaRNA-2.7.0.tar.gz
cd ViennaRNA-2.7.0
./configure
make
sudo make install

# password from the computer
# confirm installation
RNAsubopt --help
```

6.  METHODS/WORKFLOWS
RNA Vienna run

```zsh 5.9 (arm64-apple-darwin24.0)

RNAsubopt --stochBT_en=3 < 0004_dmle_3UTR_trim.fa > 0005__dmle_3UTR_trim_60nt_subopt.txt

```
