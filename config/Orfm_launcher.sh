#!/bin/bash

#SBATCH --job-name=Foram_meta_orfs

/home/richard.wissels/OrfM/orfm-0.7.1_Linux_x86_64/orfm /home/richard.wissels/Foram-assembly/results/filterd.contigs.fa > /home/richard.wissels/Foram-assembly/results/meta_orfs.fa
