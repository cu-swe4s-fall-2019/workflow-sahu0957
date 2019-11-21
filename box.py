import argparse
import sys
import os
import matplotlib.pyplot as plt

def boxplot(data, metadata, y_label, plot_title, output_file):
    try:
        plt.subplots(nrows=len(plot_title), figsize=(10, 8))

        for i in range(len(plot_title)):
            plt.subplot(len(plot_title), 1, i+1)
            plt.boxplot(data[i])

            # Hide these grid behind plot objects
            plt.title(plot_title[i])
            plt.ylabel(y_label)

            # set tick labels and export the result
            plt.xticks(range(1, len(metadata) + 1), metadata)

            if i == len(plot_title) - 1:
                plt.xlabel('Gene')

        plt.savefig(output_file)
    
    except TypeError:
        sys.stderr.write('data is the wrong format!')
        sys.exit(1)
    except:
        sys.stderr.write('Unknown error occurred...')
        sys.exit(1)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(
    description='Creates a boxplot for each tissue type')

    parser.add_argument('--output_file',
                        type=str,
                        help='What to name the output plot',
                        required=True)

    parser.add_argument('--gene',
                        type=str,
                        help='Gene of interest',
                        required=True)

    parser.add_argument('--tissue',
                        type=str,
                        help='Tissue of interest',
                        required=True)

    parser.add_argument('--metadata_file',
                        type=str,
                        help='Sample metadata file',
                        required=True)

    args = parser.parse_args()

    samples = {}
    try:
        metadata = open(args.metadata_file)
    except OSError:
        sys.stderr.write('metadata file could not be read!')
        sys.exit(1)
    for l in metadata:
        sample_id = l.split(':')[0]
        sample_genes = l.split(':')[1].split()
        # combine sample_id and genes as a dictionary
        samples[sample_id] = sample_genes
    metadata.close()

    # Allow for multiple tissues and genes as input, turn them into
    # a list
    tissue = args.tissue.split()
    gene = args.gene.split()

    # input_boxlist will be fed into boxplot function
    input_boxlist = []
    for t in tissue:
        counts_and_samples = []
        sample_ids = samples[t]
        # For each gene list, add in the counts to a dictionary
        for g in gene:
            gene_dict = {}
            if not os.path.exists(g + '_counts.txt'):
                continue
            count_file = open(g + '_counts.txt')
            for l in count_file:
                gene_dict[l.split(':')[0]] = int(l.split(':')[1])
            count_file.close()
            count_list = []
            # For each sample, look for where it belongs in the dictionary
            for s in sample_ids:
                if s in gene_dict.keys():
                    count_list.append(gene_dict[sample_id])
            counts_and_samples.append(count_list)
        input_boxlist.append(counts_and_samples)

    # Output a boxplot based on that input
    boxplot(input_boxlist, gene, 'Reads', tissue, args.output_file)
    sys.exit(0)
