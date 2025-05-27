Basic structure:
1.  DATA-ORIGIN:
2.  DATA-DATE:
3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
6.  METHODS/WORKFLOWS

drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

### IQ-tree2 to generate the Newick tree
software package for phylogenetic inference using maximum likelihood
https://doi.org/10.1093/molbev/msaa015

1.  DATA-ORIGIN:
path(/Users/alejandraescos/Documents/github/SCR/0002_phylogenetics/data)

2.  DATA-DATE:
20250508

3.  DATA-VERSION:
SUPERMATRIX.fasta

4.  DOWLOADED-SCRIPT:

I have now a concatenated file of all the protein sequences and I will generate the tree from this file with iqtree2 using PDC Dardel.

-m MFP+MERGE
Tells IQ-TREE to run *ModelFinder Plus (MFP) to automatically select the best substitution model and to search for an optimal partitioning scheme by merging similar partitions*.

MFP finds the best model per partition.

+MERGE then tests whether some partitions can be combined to reduce over-parameterization.

```pdc darcel
#!/bin/bash -l
#
# SBATCH directives
#
# (1) Account to charge
#SBATCH -A naiss2025-22-683   # ← replace with your project/allocation
#
# (2) Job name
#SBATCH -J iqtree_supermatrix
#
# (3) Partition (queue)
#SBATCH -p main
#
# (5) Resources: here we use 1 node, 1 task, and 10 threads
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#
# (6) Output files
#SBATCH -o supermatrix.%j.out
#SBATCH -e supermatrix.%j.err

# ============ Your commands start here ============

# Load the IQ‐TREE2 module that PDC provides
ml load PDC iqtree

# Move into the directory where your SUPERMATRIX.fasta lives
cd /cfs/klemming/home/a/aescos/Private

# Run IQ‐TREE2 with 10 threads, ModelFinder+MERGE, and prefix “supermatrix”
srun iqtree2 \
     -s SUPERMATRIX.fasta \
     -m MFP+MERGE \
     -nt $SLURM_CPUS_PER_TASK \
     -pre supermatrix
```

I regenerated the tree to binazire the tree:

```
#!/bin/bash -l
#
# SBATCH directives
#
# (1) Account to charge
#SBATCH -A naiss2025-22-683   # ← replace with your project/allocation
#
# (2) Job name
#SBATCH -J iqtree_supermatrix
#
# (3) Partition (queue)
#SBATCH -p main
#
# (4) Wall-time (HH:MM:SS)
#SBATCH -t 24:00:00
#
# (5) Resources: here we use 1 node, 1 task, and 10 threads
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=128
#
# (6) Output files
#SBATCH -o supermatrix.%j.out
#SBATCH -e supermatrix.%j.err

# ============ Your commands start here ============

# Load the IQ‐TREE2 module that PDC provides
ml load PDC iqtree

# Move into the directory where your SUPERMATRIX.fasta lives
cd /cfs/klemming/home/a/aescos/Private

# Run IQ‐TREE2 with 10 threads, ModelFinder+MERGE, and prefix “supermatrix”
srun iqtree2 \
  -s SUPERMATRIX.fasta \
  -m Q.insect+F+R6 \
  -te supermatrix.treefile \
  -pre supermatrix_rerooted \
  -nt AUTO \
  -root 0005_Drosophila_navojoa_dna_masked.fa
  -nt 128 \


```
5.  SOFTWARE-VERSION:
iqtree2

# Tree figure:

I used this website: https://itol.embl.de/upload.cgi

I used the binarize tree and I am pasting here the Newick tree with name changes for the figure:

(((((((Drosophila albomicans:0.0758240608,Drosophila innubila:0.0557615052):0.0301554653,(((((Drosophila ananassae:0.0837451666,((((Drosophila biarmipes:0.0170451030,(Drosophila subpulchrella:0.0060791864,Drosophila suzukii:0.0066706860):0.0068783394):0.0109883112,Drosophila takahashii:0.0283761660):0.0071547804,(((Drosophila erecta:0.0153890384,((Drosophila santomea:0.0035137369,Drosophila yakuba:0.0034037254):0.0042358216,Drosophila teissieri:0.0068003976):0.0072714626):0.0037786133,((Drosophila mauritiana:0.0028131641,(Drosophila sechellia:0.0101728771,Drosophila simulans:0.0036462690):0.0005110066):0.0053779615,Drosophila melanogaster:0.0089476739):0.0126533231):0.0252365681,Drosophila eugracilis:0.0364744914):0.0033432574):0.0063635940,((Drosophila elegans:0.0075533524,Drosophila gunungcola:0.0063060008):0.0201382695,Drosophila rhopaloa:0.0233302648):0.0105435704):0.0357262429):0.0409156524,(((Drosophila guanche:0.0090964132,Drosophila subobscura:0.0059282294):0.0220668406,Drosophila obscura:0.0204738034):0.0074959085,(Drosophila miranda:0.0051365088,(Drosophila persimilis:0.0022564528,Drosophila pseudoobscura:0.0024653180):0.0024247433):0.0204851899):0.0724357187):0.0372526133,Drosophila willistoni:0.1442363533):0.0269727612,(Glossina morsitans:0.3035041964,Lucilia cuprina:0.1786865794):0.4181403355):0.0492503266,Drosophila busckii:0.1488476896):0.0217950811):0.0168439115,Drosophila grimshawi:0.0917331690):0.0198110569,Drosophila virilis:0.0465578546):0.0428756437,Drosophila hydei:0.0272303923):0.0288043025,(Drosophila arizonae:0.0077579033,Drosophila mojavensis:0.0043116407):0.0064720800):0.00726748,Drosophila navojoa:0.00726748);
