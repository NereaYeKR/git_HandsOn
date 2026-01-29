#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description='Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
args.seq = args.seq.upper()  # Converts the sequence to uppercase to ensure case insensitivity

if re.search('^[ACGT]+$', args.seq):  # Check if it's DNA
    print('The sequence is DNA')
elif re.search('^[ACGU]+$', args.seq):  # Check if it's RNA
    print('The sequence is RNA')
else: 
    print('The sequence is not DNA or RNA')

# Search for a motif
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end='')
    if re.search(args.motif, args.seq):
        print("Found")
    else:
        print("Not Found")
