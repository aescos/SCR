drifter,vvl = FBgn0086680
CG6282 = FBgn0035914
Basic structure:
1.  DATA-ORIGIN:
2.  DATA-DATE:
3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
6.  METHODS/WORKFLOWS


1.  DATA-ORIGIN:

2.  DATA-DATE:
15052025

3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:

6.  METHODS/WORKFLOWS

### Hairpin selection and BED format
Detect hair pin and then do different versions of this script for:

60 nt

```R
---
title: "SCR"
author: "Alejandra Escos"
date: "2025-04-02"
output: html_document
---
First always remove all the lists from the R enviroment

- rm: remove
- ls(): Lists all objects from the enviroment

```{r}
rm(list = ls())
```

Code set up for the whole envirment of R

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE, message = FALSE, warning = FALSE)
```

### Table preparation

```{r}
library(dplyr)
library(tidyr)
packageVersion("dplyr")
packageVersion("tidyr")
version # R version
```
```{r}
subopt <- read.delim('/Users/alejandraescos/Documents/github/SCR/0001_hairpin/data/0006__dmle_3UTR_trim_60nt_subopt_select.tsv', header = TRUE)
```

```{r}
subopt_Y <- subopt %>% filter(Hairpin == 'Y')
subopt_Y_minMFE <- subopt_Y %>%
  group_by(GeneID) %>%
  slice_min(order_by = MFE, with_ties = FALSE) %>% # Keeps the single row with minimum value for each group
  ungroup()
```

```{r}
subopt_Y_minMFE <- as.data.frame(subopt_Y_minMFE)
write.table(
  subopt_Y_minMFE,
  file      = "/Users/alejandraescos/Documents/github/SCR/0001_hairpin/data/subopt_Y_minMFE.txt",  # the output filename
  sep       = "\t",                   # tab-separated
  quote     = FALSE,                  # don’t wrap character columns in quotes
  row.names = FALSE,                  # don’t write row numbers
  col.names = TRUE                    # write header
)
```
Then change to BED format the file

```zsh
awk '{ OFS="\t"; print $1, $2, $3, $4, $5, $6 }' 0007_subopt_Y_minMFE.txt > 0007_subopt_Y_minMFE.bed
```
