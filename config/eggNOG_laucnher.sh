#!/bin/bash

#SBATCH --job-name=EggNOG_foram

python /home/richard.wissels/eggNOG/eggnog-mapper/emapper.py -i /home/richard.wissels/Foram-assembly/results/meta_orfs.fa --output /home/richard.wissels/Foram-assembly/results/EggNOG_out -m diamond --cpu 16
