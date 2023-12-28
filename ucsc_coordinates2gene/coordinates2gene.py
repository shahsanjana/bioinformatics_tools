import argparse
import pandas as pd


def parse_ags():
    parser = argparse.ArgumentParser(description = "map unlabled TxDB IDs to their Gene; must get output from ucsc table browser https://genome.ucsc.edu/cgi-bin/hgTables")
    parser.add_argument('-i', metavar="input file", type=str,required=True, help="(Required)tsv containing chromosome, start coord, end coord, and full coordinaate, (example file: unlab_genes_00)")
    parser.add_argument('-u', metavar="UCSC mapped transcripts", type=str, required=True, help="(Required) output from ucsc table browser with columns: hg38.knownGene.name,hg38.knownGene.chrom,hg38.knownGene.txStart,hg38.knownGene.txEnd,hg38.kgXref.kgID,hg38.kgXref.geneSymbol (example file: regions00.csv) ")
    parser.add_argument('-o', metavar="output file name", type=str,required=True, help="(Required)output file name, (example:mapped_00)")


    args = parser.parse_args()
    return args

def find_gene(input,ucsc):
    #faster
    input=pd.read_csv(input,sep = "\t", header=None)
    #input[0]="chr"+input[0]
    ucsc=pd.read_csv(ucsc, sep = ",")
    my_list=[]

    for yindex, yrow in input.iterrows():
        subsetDF= ucsc[ucsc["hg38.knownGene.chrom"] == yrow[0]]
        for sindex, srow in subsetDF.iterrows():
            if int(srow['hg38.knownGene.txStart'] <= int(yrow[1]) and int(srow['hg38.knownGene.txEnd']) >= int(yrow[2])): 
                my_list.append([yrow[3],srow["hg38.knownGene.chrom"], srow['hg38.kgXref.kgID'], srow["hg38.knownGene.txStart"],srow["hg38.knownGene.txEnd"],srow['hg38.kgXref.geneSymbol']])
    df=pd.DataFrame(my_list, columns = ['chromosome_coordinate', 'hg38.knownGene.chrom', 'hg38.kgXref.kgID', 'hg38.knownGene.txStart','hg38.knownGene.txEnd','hg38.kgXref.geneSymbol'])
    df=df.drop_duplicates()
    return(df)

    
def main():
    inputs=parse_ags()
    return inputs

if __name__ == '__main__':
    map=main()
    df = find_gene(map.i, map.u)
    df.to_csv(map.o+".csv", index=False)
