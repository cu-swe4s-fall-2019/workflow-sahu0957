test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest

. ssshtest

TISSUE='Brain'
METADATA_FILE='test_metadata.txt'
GENE='LDLR'
OUTFILE='test.png'

run good_box python box.py \
        --tissue $TISSUE \
        --gene $GENE \
	--metadata_file $METADATA_FILE \
        --output_file $OUTFILE
assert_exit_code 0


run bad_meta_box python box.py \
        --tissue $TISSUE \
        --gene $GENE \
	--metadata_file 'foo' \
        --output_file $OUTFILE
assert_exit_code 1

rm -f $OUTFILE
