#!/usr/bin/env Rscript
# Open libraries
rm(list = ls())
library(dplyr)
library(tidyr)
library(gprofiler2)

# Read file
subopt <- read.delim('/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/Ioannis/data/raw_data/3utr_hairpin_60.tsv', header = TRUE)

# Keep the hairpins eith lowest MFE when they are duplicated
subopt_Y <- subopt %>% filter(Hairpin == 'Y')
subopt_Y_minMFE <- subopt_Y %>%
  group_by(Gene_Name) %>%
  slice_min(order_by = MFE, with_ties = FALSE) %>% # Keeps the single row with minimum value for each group
  ungroup()

# Convert the gene names to gene IDs.
gene_list <- subopt_Y_minMFE[[1]]
gene_list <- as.character(gene_list)
gene_convert <- gconvert(query = gene_list,
                         organism = "dmelanogaster",
                         target = "FLYBASE_GENE_ID"
)
gene_convert1 <- gene_convert[, c("input", "target")]
colnames(gene_convert1) <- c("Gene_Name", "GeneID")

# Merge to have GeneID (FBgn* instead of Gene_Name)
subopt_Y_minMFE <- merge(
  subopt_Y_minMFE,
  gene_convert1,
  by       = "Gene_Name",   # column name to match on
  all.x    = TRUE            # keep all rows from df, even if no match in conv2
)
subopt_Y_minMFE <- subopt_Y_minMFE [, c(ncol(subopt_Y_minMFE ), 1:(ncol(subopt_Y_minMFE ) - 1))]

subopt_Y_minMFE <- subopt_Y_minMFE %>%
  select(-Gene_Name, -Hairpin, -MFE)

# Export table
subopt_Y_minMFE <- as.data.frame(subopt_Y_minMFE)
write.table(
  subopt_Y_minMFE,
  file      = "/Users/alejandraescos/Documents/github/SCR/0003_hairpinConservation/Ioannis/data/0007_I_subopt_Y_minMFE.bed",  # the output filename
  sep       = "\t",                   # tab-separated
  quote     = FALSE,                  # don’t wrap character columns in quotes
  row.names = FALSE,                  # don’t write row numbers
  col.names = TRUE                    # write header
)