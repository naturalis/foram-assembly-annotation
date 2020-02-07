#!/bin/bash

#SBATCH --job-name=foram_contig_matching


/home/richard.wissels/diamond/diamond blastx -d /home/richard.wissels/nr/nr -q /home/richard.wissels/Foram-assembly/data/final.contigs.fa -p 16 -sensitive -o /home/richard.wissels/Foram-assembly/results/matches_nr.m8
