Basic structure:
1.  DATA-ORIGIN:
2.  DATA-DATE:
3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
6.  METHODS/WORKFLOWS

drifter,vvl = FBgn0086680
CG6282 = FBgn0035914

### Mask DNA for preparation for CACTUS pipeline

For softmasking my genomes I have the following libraries:
https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?name=melanogaster%20subgroup
melanogaster subgroup: taxome ID 32351 for the subgroup
Drosophila erecta   
Drosophila mauritiana   
Drosophila melanogaster (fruit fly)   
Drosophila melanogaster x Drosophila mauritiana   
Drosophila melanogaster x Drosophila sechellia   
Drosophila melanogaster x Drosophila simulans   
Drosophila orena   
Drosophila santomea   
Drosophila sechellia   
Drosophila sechellia x Drosophila mauritiana   
Drosophila sechellia x Drosophila simulans   
Drosophila simulans   
Drosophila simulans x Drosophila mauritiana   
Drosophila simulans x Drosophila sechellia   
Drosophila teissieri   
Drosophila yakuba   
Drosophila yakuba mayottensis   
Drosophila yakuba x Drosophila santomea   
Drosophila yakuba x Drosophila teissieri   


1.  DATA-ORIGIN:
path(/Users/alejandraescos/Documents/github/SCR/0002_phylogenetics/data)

2.  DATA-DATE:
20250512

3.  DATA-VERSION:
SUPERMATRIX.fasta

4.  DOWLOADED-SCRIPT:
Run repeatmasker in all the *.fa
```
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_albomicans_gca009650485v2rs.ASM965048v2.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_ananassae_gca017639315v2rs.ASM1763931v2.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_arizonae_gca001654025v1rs.ASM165402v1.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_biarmipes_gca025231255v1rs.RU_DBia_V1.1.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_busckii_gca011750605v1rs.ASM1175060v1.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_elegans_gca000224195v2rs.Dele_2.0.dna.toplevel.fa
RepeatMasker -species "Drosophila erecta" -pa 10 -xsmall Drosophila_erecta_gca003286155v2rs.DereRS2.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_eugracilis_gca018153835v1rs.ASM1815383v1.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_grimshawi_gca018153295v1rs.ASM1815329v1.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_guanche_gca900245975v1rs.DGUA_6.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_gunungcola_gca025200985v1rs.Dgunungcola_SK_2.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_hydei_gca003285905v2rs.DhydRS2.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_innubila_gca004354385v1rs.UK_Dinn_1.0.dna.toplevel.fa
RepeatMasker -species "Drosophila mauritiana" -pa 10 -xsmall Drosophila_mauritiana_gca004382145v1rs.ASM438214v1.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_melanogaster.BDGP6.46.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_miranda_gca003369915v2rs.D.miranda_PacBio2.1.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_mojavensis_gca018153725v1rs.ASM1815372v1.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_navojoa_gca001654015v2rs.UFRJ_Dnav_4.2.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_obscura_gca018151105v1rs.ASM1815110v1.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_persimilis_gca003286085v2rs.DperRS2.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_pseudoobscura_gca009870125v2rs.UCI_Dpse_MV25.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_rhopaloa_gca018152115v1rs.ASM1815211v1.dna.toplevel.fa
RepeatMasker -species "Drosophila santomea" -pa 10 -xsmall Drosophila_santomea_gca016746245v2rs.Prin_Dsan_1.1.dna.toplevel.fa
RepeatMasker -species "Drosophila sechellia" -pa 10 -xsmall Drosophila_sechellia.dsec_caf1.dna.toplevel.fa
RepeatMasker -species "Drosophila simulans" -pa 10 -xsmall Drosophila_simulans.ASM75419v3.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_subobscura_gca008121235v1rs.UCBerk_Dsub_1.0.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_subpulchrella_gca014743375v2rs.RU_Dsub_v1.1.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_suzukii_gca013340165v1rs.LBDM_Dsuz_2.1.pri.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_takahashii_gca018152695v1rs.ASM1815269v1.dna.toplevel.fa
RepeatMasker -species "Drosophila teissieri" -pa 10 -xsmall Drosophila_teissieri_gca016746235v2rs.Prin_Dtei_1.1.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_virilis_gca003285735v2rs.DvirRS2.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_willistoni_gca018902025v2rs.UCI_dwil_1.1.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Drosophila_yakuba_gca016746365v2rs.Prin_Dyak_Tai18E2_2.1.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Glossina_morsitans.GmorY1.dna.toplevel.fa
RepeatMasker -species "Drosophila melanogaster" -pa 10 -xsmall Lucilia_cuprina.ASM118794v1.dna.toplevel.fa

```

5.  SOFTWARE-VERSION:


