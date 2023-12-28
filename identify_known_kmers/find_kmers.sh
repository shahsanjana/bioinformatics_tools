#!/bin/bash

# Check if the required arguments are provided
if [ $# -ne 3 ]; then
    echo "Usage: $0 <kmers_file> <fasta_file> <output_file>"
    exit 1
fi

# Input parameters
kmers_file="$1"  # File containing k-mers
fasta_file="$2"  # Input FASTA file
output_file="$3" # Output CSV file

# Add column headers
echo Header$'\t'Kmer$'\t'Sequence > "$output_file"

# Read k-mers from the provided file
while IFS= read -r kmer
do
    awk -v kmer="$kmer" '/^>/ {header = $0} $0 ~ kmer {print header "\t" kmer "\t" $0}' "$fasta_file" >> "$output_file"
done < "$kmers_file"
