GENES = ["LDLR", "BRCA2", "MYL2"]
TISSUES = ["Brain", "Ovary", "Muscle"]
GROUP = "SMTS"

rule all:
    input:
        'Brain-Ovary-Muscle_LDLR-BRCA2-MYL2.png'

rule tissue_samples:
    input:
        'GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt'
    output:
        expand('{tissue}_samples.txt', tissue=GROUP)
    shell:
        'python get_tissue_samples.py --output_file {output} --group_type {GROUP} --sample_attributes {input}'

rule gene_sample_counts:
    input:
        'GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz'
    output:
        expand('{gene}_counts.txt', gene=GENES)
    shell:
        'for GENE in {GENES}; do ' \
        + 'python get_gene_counts.py --output_file $GENE\_counts.txt --gene $GENE --gene_reads {input}; ' \
        + 'done'

rule box:
    input:
        rules.tissue_samples.output,
        rules.gene_sample_counts.output
    output:
        'Brain-Ovary-Muscle_LDLR-BRCA2-MYL2.png'
    shell:
        'python box.py --output_file {output} --gene \"{GENES}\" --tissue \"{TISSUES}\" --metadata_file {GROUP}_samples.txt'
