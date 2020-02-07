#!/bin/python
from __future__ import print_function
import sys, getopt
from Bio import SeqIO


def main(argv):
    inputfile = ''
    outputfile = 'length_filter_out.fa'
    minlength = 250
    try:
        opts, args = getopt.getopt(argv,"hi:o:l:",["ifile=","ofile=","minlength="])
    except getopt.GetoptError as err:
        print(err)
        print ('length_filter.py -i <inputfile> -o <outputfile> -l <minlength>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('length_filter.py -i <inputfile> -o <outputfile> -l <minlength>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ('-l', "--minlength"):
            minlength = int(arg)
    print("Starting seq_reading on:", datetime.datetime.now())
    myList = []
    for seq_record in SeqIO.parse(inputfile, "fasta"):
        myList.append([seq_record.id, str(seq_record.seq), len(seq_record)])
    print("\nall sequences are loaded on:",datetime.datetime.now(),"\n\nStarting sorting on sequence length" )
    myList.sort(key=lambda x: x[2])
    print("\nSorting completed on:",datetime.datetime.now(),"\n\nstart filter on length")
    outFile = open(outputfile, 'w')
    for i in range(len(myList),0,-1):
        if len(myList[i-1][1]) > minlength:
            outFile.write(">", myList[i-1][0], sep='')
            outFile.write(myList[i-1][1])
    outFile.close()
    print("Finished on:", datetime.datetime.now())

if __name__ == "__main__":
    main(sys.argv[1:])
