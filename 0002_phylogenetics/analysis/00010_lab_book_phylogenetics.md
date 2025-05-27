Basic structure:
1.  DATA-ORIGIN:
2.  DATA-DATE:
3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
6.  METHODS/WORKFLOWS

drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

### Perform BUSCO from orthoBD, to find all protein orthologs
https://busco.ezlab.org/busco_userguide.html#busco-pipelines

1.  DATA-ORIGIN:

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

2.  DATA-DATE:
20250416

3.  DATA-VERSION:


4.  DOWLOADED-SCRIPT:

First pull from docker:
```
docker pull ezlabgva/busco:v5.4.7_cv1
# Location
cd /Users/alejandraescos/Documents/github/SCR/0002_phylogenetics/data/0002_BUSCO_results
```
I then generated an script in bash "0002_run_busco_loop.sh" with the following instructions:

Save the following script: 
```zsh
#!/bin/bash
# Change to your working directory (if not already there)
cd /Users/alejandraescos/Documents/github/SCR/0002_phylogenetics/data

# Loop over each file matching "*longest_isoform.fa"
for file in *longest_isoform.fa; do
    # Get the base filename (remove the extension)
    base_name=$(basename "$file" .fa)
    
    # Construct an output folder name, e.g., "filename_busco"
    output_folder="${base_name}_busco"
    
    # Print information for the current file
    echo "Processing $file, output will be saved in $output_folder"
    
    # Run BUSCO using Docker on the current file
    docker run --rm -v "$PWD":/data -w /data ezlabgva/busco:v5.4.7_cv1 busco -i "$file" -o "$output_folder" -m proteins -l diptera_odb10 -f
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

To generate the graphs be located at:
cd /Users/alejandraescos/Documents/github/SCR/0002_phylogenetics/data/0002_BUSCO_results

```
docker run --rm \
  --platform linux/amd64 \
  -v "$PWD/BUSCO_summaries":/data \
  -v "/Users/alejandraescos/Documents/github/SCR/0002_phylogenetics/scripts":/scripts \
  -w /data \
  ezlabgva/busco:v5.4.7_cv1 \
  python3 /scripts/0002_generate_plot.py \
    --working_directory /data \
    --run_type specific
```
5.  SOFTWARE-VERSION:

zsh 5.9 (arm64-apple-darwin24.0)

**DOCKER instalation**
Docker version 28.0.4, build b8034c0

This grabs a pre-built Docker image with BUSCO, AUGUSTUS, MAFFT, etc. all set up:
```zsh
docker pull ezlabgva/busco:v5.4.7_cv1
```
