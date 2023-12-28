#!/usr/bin/env bash

# index_all.sh

for INFILE in "$@"
do
    #samtools index $INFILE
    samtools view -b  -T hg38.fa  $INFILE > ${INFILE}.bam
    echo $INFILE "done" 
done

#run with nohup ./samtoolsindex.sh  *.bam &
