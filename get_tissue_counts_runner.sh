METADATA=GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt
GROUP=SMTS
OUTFILE='test_metadata.txt'

python get_tissue_samples.py \
        --sample_attributes $METADATA \
        --group_type $GROUP \
        --output_file $OUTFILE
