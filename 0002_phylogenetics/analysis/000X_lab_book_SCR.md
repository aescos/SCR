drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

Basic structure:
1.  DATA-ORIGIN:
2.  DATA-DATE:
3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
6.  METHODS/WORKFLOWS

................................................................................

Pipeline: data (protein sequences/species) --> parse fasta --> BUSCO --> BUSCO phylogenetic tree --> keep most optimized iqtree --> mask DNA sequence --> CACTUS

................................................................................

# AIM1
## Data protein sequences/species

I downloaded drosophila protein sequences:
https://metazoa.ensembl.org/info/data/ftp/index.html

- DATA-ORIGIN:
ensembl
- DATA-DATE:
14APR2025
- Path:
/Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/raw_data

Species downloaded:

**🧬 Why No Duplicates in BUSCO?**
1. BUSCO looks for single-copy orthologs
BUSCO is based on curated sets of Benchmarking Universal Single-Copy Orthologs, meaning: Each BUSCO gene is expected to appear once in each genome/proteome. If it finds duplicates, it marks that BUSCO gene as duplicated, not "complete."

2. In phylogenomics mode, duplicates are excluded
When you use BUSCO for building a phylogenetic tree: It only uses shared single-copy BUSCOs across all species. If a gene is duplicated in one species, it won’t be included in the alignment. So, more duplicates = fewer shared BUSCOs = weaker tree.

💡 The more clean, single-copy BUSCOs you have, the better the final alignment coverage and species tree quality.

**🧬 Why Choose the Longest Isoform?**
1. BUSCO is based on single-copy orthologs
Keeping the longest isoform increases the chance of matching a complete, full-length BUSCO gene. Shorter isoforms (or just picking the first one) may be incomplete, causing: false negatives ("missing") duplications if multiple isoforms match the same BUSCO


I generated the script "0001_parse_fasta.py" to keep only the longest proteins from the same gene in each of the files and they are all named as "0001_{name1_name2}_longest_isoform.fa".
For Lucilia_cuprina and Glossina_morsitans I did it by hand as the script wasnt able to name in the same way.
................................................................................
# AIM2
Use BUSCO

https://busco.ezlab.org/busco_userguide.html#busco-pipelines
https://github.com/jamiemcg/BUSCO_phylogenomics
 
**DOCKER instalation**
Docker version 28.0.4, build b8034c0

This grabs a pre-built Docker image with BUSCO, AUGUSTUS, MAFFT, etc. all set up:
```zsh
docker pull ezlabgva/busco:v5.4.7_cv1
```

**BUSCO instalation**
```zsh
conda install -c conda-forge -c bioconda busco=5.8.2
```

Create a file called 0001_busco_phylogeny.cfg in BBedit like this:
................................................................................
[genomes]
Dmel = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_melanogaster_longest_isoform.fa
drosophila_mauritiana = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_mauritiana_longest_isoform.fa
drosophila_simulans = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_simulans_longest_isoform.fa
drosophila_sechellia = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_sechellia.dsec_longest_isoform.fa
drosophila_erecta = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_erecta_longest_isoform.fa
drosophila_santomea = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_santomea_longest_isoform.fa
drosophila_yakuba = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_yakuba_longest_isoform.fa
drosophila_teissieri = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_teissieri_longest_isoform.fa
drosophila_eugracilis = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_eugracilis_longest_isoform.fa
drosophila_biarmipes = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_biarmipes_longest_isoform.fa
drosophila_subpulchrella = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_subpulchrella_longest_isoform.fa
drosophila_suzukii = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_suzukii_longest_isoform.fa
drosophila_takahashii = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_takahashii_longest_isoform.fa
drosophila_elegans = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_elegans_longest_isoform.fa
drosophila_gunungcola = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_gunungcola_longest_isoform.fa
drosophila_rhopaloa = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_rhopaloa_longest_isoform.fa
drosophila_ananassae = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_ananassae_longest_isoform.fa
drosophila_guanche = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_guanche_longest_isoform.fa
drosophila_subobscura = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_subobscura_longest_isoform.fa
drosophila_obscura = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_obscura_longest_isoform.fa
drosophila_miranda = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_miranda_longest_isoform.fa
drosophila_persimilis = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_persimilis_longest_isoform.fa
drosophila_pseudoobscura = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_pseudoobscura_longest_isoform.fa
drosophila_willistoni = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_willistoni_longest_isoform.fa
drosophila_albomicans = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_albomicans_longest_isoform.fa
drosophila_innubila = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_innubila_longest_isoform.fa
drosophila_arizonae = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_arizonae_longest_isoform.fa
drosophila_mojavensis = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_mojavensis_longest_isoform.fa
drosophila_navojoa = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_navojoa_longest_isoform.fa
drosophila_hydei = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_hydei_longest_isoform.fa
drosophila_virilis = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_virilis_longest_isoform.fa
drosophila_grimshawi = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_grimshawi_longest_isoform.fa
drosophila_busckii = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Drosophila_busckii_longest_isoform.fa
Lucilia_cuprina = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Lucilia_cuprina_longest_isoform.fa
Glossina_morsitans = /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0001_Glossina_morsitans_longest_isoform.fa

[parameters]
lineage_dataset = diptera_odb10
mode = proteins
................................................................................

I then generated an script in bash "0002_run_busco_loop.sh" with the following instructions:

Save the following script:
```zsh
#!/bin/bash
# Change to your working directory (if not already there)
cd /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data

# Loop over each file matching "*longest_isoform.fa"
for file in *longest_isoform.fa; do
    # Get the base filename (remove the extension)
    base_name=$(basename "$file" .fa)
    
    # Construct an output folder name, e.g., "filename_busco"
    output_folder="${base_name}_busco"
    
    # Print information for the current file
    echo "Processing $file, output will be saved in $output_folder"
    
    # Run BUSCO using Docker on the current file
    docker run --rm \
      -v "$PWD":/data \
      -w /data \
      ezlabgva/busco:v5.4.7_cv1 \
      busco -i "$file" -o "$output_folder" -m proteins -l diptera_odb10 -f
done
```
Make it executable

```zsh
chmod +x 0002_run_busco_loop.sh
```
run it
```zsh
./0002_run_busco_loop.sh
```

Generate graphs from BUSCO::::::
................................................................................
#AIM3
You can install the BUSCO_Phylogenomics package with Conda from the Bioconda channel
https://github.com/jamiemcg/BUSCO_phylogenomics

```zsh
conda create -n BUSCO_phylogenomics -c bioconda busco_phylogenomics
conda activate BUSCO_phylogenomics
cd /Users/alejandraescos/BUSCO_phylogenomics
ln -s /Users/alejandraescos/Documents/github/SCR/0002_phylogenetics/data/0002_BUSCO_results ./BUSCO_results

python BUSCO_phylogenomics.py -i BUSCO_results -o 0003_busco_phylogenomics -t 10 --supermatrix_only
```

I have now a concatenated file of all the protein sequences and I will generate the tree from this file with iqtree2 using PDC dardel.

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
-m MFP+MERGE
Tells IQ-TREE to run ModelFinder Plus (MFP) to automatically select the best substitution model and to search for an optimal partitioning scheme by merging similar partitions.

MFP finds the best model per partition.

+MERGE then tests whether some partitions can be combined to reduce over-parameterization.


... perform the graph from busco
................................................................................

#AIM4
Perform full alignment with CACTUS

https://github.com/ComparativeGenomicsToolkit/cactus/blob/master/README.md

Installing CACTUS to use their align genomes from different species. For this first I downloaded Docker, which creates a stable enviroment. And because I have silicon chip in my macbook pro (M3), they recomended instaling rosetta2, which I also did.

Documentation to how to proceed is in:
https://github.com/ComparativeGenomicsToolkit/cactus/blob/master/doc/progressive.md

I need to download full sequences and change the name to the same one I have in the qtree

Progressive Cactus’s own documentation is clear: your input genomes should be soft-masked with RepeatMasker prior to alignment. 

First install
```
# 1) Tap the Bioinformatics repository
brew tap brewsci/bio

# 2) Install GenomeTools
brew install genometools

brew install brewsci/bio/repeatmasker

# 3) Install RepeatModeler (and it will pull in RepeatMasker too)
brew install repeatmasker
```
Run repeatmasker in all the *.fa
```
c# Create a folder for RM’s auxiliary output
mkdir -p repeatmasker_out

# Loop over all FASTA files (*.fa)
for f in *.fa; do
  base=${f%.fa}   # strip the .fa extension

  echo "Masking $f → ${base}_masked.fa"

  # Run RepeatMasker on this file
  RepeatMasker \
    -pa 10 \
    -species "Drosophila melanogaster" \
    -xsmall \
    -dir repeatmasker_out \
    "$f"

  # Rename the masked output back into current dir
  mv repeatmasker_out/"${base}.fa.masked" "${base}_masked.fa"
done
```
Now that they are all softmasked, prepare the file to look like:

Biznarize your tree: Select only drosophila melanogaster first
```
pip install ete3 && python3 - '<<PYCODE' from ete3 import Tree t '=' 'Tree(ALL.tree,' 'format=1)' 't.resolve_polytomy(recur
sive=True)' with 'open(ALL.binary.tree,w)' as out: 'out.write(t.write(format=1)' + "\\n)" PYCODE
```

```
python3 - << 'PYCODE'
from ete3 import Tree

# Load your original Newick (ALL.tree must end with a semicolon)
t = Tree("ALL.tree", format=1)

# Resolve all polytomies into binary splits
t.resolve_polytomy(recursive=True)

# Write out the binary tree
with open("ALL.binary.tree", "w") as out:
    out.write(t.write(format=1) + "\n")
PYCODE
```

```
# 1. Put the binary tree on line 1
cat ALL.binary.tree > cactus_seqfile.txt

# 2. Append exactly one mapping per FASTA, using /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0004_cactus/<filename>.fa
for f in 0002_*.fa; do
  tip="${f%.fa}"
  echo -e "${tip}\t/Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0004_cactus/${f}"
done >> cactus_seqfile.txt

```
Where you should be located to run the work
```
mkdir -p ~/my_cactus_project/jobStore
cd ~/my_cactus_project

```
Turn on docker desktop and activate cactus from docker

```
docker pull quay.io/comparative-genomics-toolkit/cactus:v2.9.8

```


Run

```
docker run --rm -it \
  -v $PWD:/Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0004_cactus \
  quay.io/comparative-genomics-toolkit/cactus:v2.9.8 \
  cactus \
    /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/jobStore \
    /Users/alejandraescos/Documents/github/SCR/2025_drosophila_vvl_paper/data/0004_cactus/0003_ALL.txt \
    /data/cactus_fly.hal

```


### ChatGPT instructions:
✅ Overview of Your Goal
You want to:

Use Drosophila melanogaster as a reference

Run BUSCO on multiple species' protein files

Extract shared single-copy orthologs

Align them and build a species tree

Use that tree as input for Cactus

🗂 What You’ll Need
Protein FASTA files (*.faa, *.pep, or similar) for:

D. melanogaster

Your list of other species (can be 5, 10, 20+)

A BUSCO lineage dataset, ideally one covering Drosophila:

Best choice: diptera_odb10

Alternative: insecta_odb10

BUSCO v5+ installed, along with:

MAFFT

trimAl

IQ-TREE or FastTree (IQ-TREE preferred)