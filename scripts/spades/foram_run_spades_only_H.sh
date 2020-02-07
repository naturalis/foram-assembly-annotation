#!/bin/bash
# The following two lines are there to identify the name of your job (which you will
# then be able to see in the 'sinfo' listing), and the name for the output produced
# by standard out. Thus, if you leave this unchanged, a file called
# 'REPLACE_THIS_WITH_OUTPUT_FILE_NAME.txt' will be created, and the listing will show
# job 'REPLACE_THIS_WITH_JOB_NAME' (which, in fact, will be truncated: pick a short name)

#SBATCH --job-name=H_asm

/home/jan.macher/Spades/SPAdes-3.12.0-Linux/bin/spades.py -m 500 -t 16 --dataset dataset_only_H.yaml -o /home/richard.wissels/Foram-assembly/results/spades_out

