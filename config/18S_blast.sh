#!/bin/bash

#SBATCH --job-name=contig_18S_blast

blastn -query /home/richard.wissels/Foram-assembly/data/18S_28S_Foram_Amphisorus.fasta -subject /home/richard.wissels/Foram-assembly/results/megahit_out/k141_224855.fa -out hit.out
