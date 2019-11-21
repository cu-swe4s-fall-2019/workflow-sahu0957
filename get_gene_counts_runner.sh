GENE_READS=GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz
GENE=LDLR
GROUP=SMTS
OUTFILE='test.txt'

python get_gene_counts.py \
        --gene_reads $GENE_READS \
        --gene $GENE \
        --output_file $OUTFILE
