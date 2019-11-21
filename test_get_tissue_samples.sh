test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest

. ssshtest

METADATA=GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt
GROUP='SMTS'
OUTFILE='test_meta.txt'

run standard_test_file python get_tissue_samples.py \
        --group_type $GROUP \
        --sample_attributes $METADATA \
        --output_file $OUTFILE
assert_exit_code 0

run bad_group python get_tissue_samples.py \
        --group_type 'foo' \
        --sample_attributes $METADATA \
        --output_file $OUTFILE
assert_exit_code 1

rm -f $OUTFILE
