to get list of gene ids from chromosome coordinates file
*** can only input 1000 coordinates at once

https://genome.ucsc.edu/cgi-bin/hgTables
click on define regions and input coordinates.txt file
submit and return to original page

output format: "selected fields from primary and related tables"
output filename: regions.csv
output field separator: csv


make sure these fields are checked on next page:
Select Fields from hg38.knownGene
name	Name of gene
chrom	Reference sequence chromosome or scaffold
txStart	Transcription start position (or end position for minus strand item)
txEnd	Transcription end position (or start position for minus strand item)

hg38.kgXref fields
kgID	Known Gene ID
geneSymbol	Gene Symbol

Linked Tables
kgXref	Link together a Known Gene ID and a gene alias

click on get output to return regions mapping to inputted chromosome coordinates

run script:
python coordinates2gene.py -i unlab_genes_00 -u regions00.csv -o output
