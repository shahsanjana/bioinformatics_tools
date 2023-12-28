#!/usr/bin/env bash

# index_all.sh

for INFILE in "$@"
do
   samtools index $INFILE
done

#run with nohup ./samtoolsindex.sh  *.bam &
