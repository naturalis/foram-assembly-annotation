#!/bin/bash

#SBATCH --job-name=Foram_ORFfinder

/home/richard.wissels/ORFfinder/ORFfinder -in /home/richard.wissels/Foram-assembly/results/10_longest_contigs.fa -out ORFs.out
