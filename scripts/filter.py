#!/bin/python


#This script is made to remove ID's from a file that contains every ID of every contig.


def file_opener(of_file):
    with open(of_file, 'r') as f:
        return f.readlines()


def filter(all, matched):
    filterd =  []
    for a in matched:
        if a not in matched:
            filterd.append(a)
    return filterd

def file_writer(data, of_file):
    content = ""
    for line in data:
        content += line + "\n"
    file = open(of_file, "w")
    file.write(content)
    file.close()

def main():
    all_ids = file_opener('/home/richard.wissels/Foram-assembly/data/contig_ids.txt')
    matched_ids = file_opener('/home/richard.wissels/Foram-assembly/results/uniq_1e-43_contig_matches.txt')
    filterd_ids = filter(all_ids, matched_ids)
    file_writer(filterd_ids, '/home/richard.wissels/Foram-assembly/results/non_matched_contig_ids.txt')

main()
