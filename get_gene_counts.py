import gzip
import argparse
import sys
import os


def fetch_gene_counts(gene, count_file, output_file):
    output = open(output_file, 'w')
    version = None
    dim = None
    gene_name = gene
    data_file_name = count_file
    data_header = None
    gene_name_col = 1

    if os.path.exists(data_file_name) is True:
        pass
    else:
        print("gene file does not exist! exiting...")
        sys.exit(1)

    # Read gzip read count file. Remove the headers
    for l in gzip.open(data_file_name, 'rt'):
        if version is None:
            version = l
            continue

        if dim is None:
            dim = [int(x) for x in l.strip().split()]
            continue

        if data_header is None:
            data_header = []
            data_header = l.rstrip().split('\t')
            continue

        A = l.rstrip().split('\t')

        if A[gene_name_col] == gene_name:
            for i in range(gene_name_col + 1, len(data_header)):
                output.write(data_header[i] + ':' + A[i])
                if i != len(data_header) - 1:
                    output.write('\n')
            output.close()

    if os.path.exists(output_file) is False:
        print("gene name not found!")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
            description="fetch gene count data from a file")
    parser.add_argument("--gene_reads",
                        help="path to file containing gene reads", type=str)
    parser.add_argument("--gene", help="name of gene of interest", type=str)
    parser.add_argument("--output_file",
                        help="path to save output file",
                        type=str)
    args = parser.parse_args()

    fetch_gene_counts(args.gene, args.gene_reads, args.output_file)


if __name__ == '__main__':
    main()
