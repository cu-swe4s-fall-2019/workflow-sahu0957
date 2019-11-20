test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest

. ssshtest

GENE_READS=GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz
GENE=LDLR
OUTFILE='test.txt'

run bad_gene_file python get_gene_counts.py \
        --gene_reads 'foo.txt' \
        --gene $GENE \
        --output_file $OUTFILE
assert_exit_code 1

run good_gene_file python get_gene_counts.py \
        --gene_reads $GENE_READS \
        --gene $GENE \
        --output_file $OUTFILE
assert_exit_code 0

rm -f $OUTFILE
