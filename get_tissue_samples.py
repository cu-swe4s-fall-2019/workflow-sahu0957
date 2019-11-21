import argparse
import sys
import os


def linear_search(key, L):
    # Search from beginning to end for a match. Return index
    # when the first match is found
    for i in range(len(L)):
        if key == L[i]:
            return i
    return -1


def fetch_metadata(group_type, sample_attributes):
    meta_header = None
    target_group = []
    keys_and_values = {}
    f = open(sample_attributes)
    for l in f:
        sample_line = l.rstrip().split('\t')
        if meta_header is None:
            # Take the first line as the header
            meta_header = sample_line
            target_idx = linear_search(group_type, meta_header)
            if target_idx == -1:
                print('Group type not found! Exiting...')
                sys.exit(1)
            continue
        # Sample names are in the first column
        sample_idx = 0
        # Find the group we're looking for
        # The key will be column with the group type e.g. Blood
        key = sample_line[target_idx]
        # The value will be whatever samples can be found that match
        # the key e.g. GTEX-XYZ
        value = sample_line[sample_idx]
        search = None

        # Check to see if we already have the sample in the dictionary already
        if key in keys_and_values.keys():
            search = keys_and_values[key]

        # If we have the key already, it's not necessary to add.
        # Otherwise, populate our growing array
        if (search is None):
            keys_and_values[key] = [value]
            target_group.append(key)
        else:
            # This isn't necessary, but I can use it for bugfinding
            search.append(value)
    f.close()
    return keys_and_values, target_group


def main():
    parser = argparse.ArgumentParser(
        description='fetch sample information from a file')

    # require file name as one of the inputs
    parser.add_argument('--output_file',
                        type=str,
                        help='path to save output file',
                        required=True)

    # require group type as one of the inputs
    parser.add_argument('--group_type',
                        type=str,
                        help='The group type to search',
                        required=True)

    # require meta file as one of the inputs
    parser.add_argument('--sample_attributes',
                        type=str,
                        help='Path to metadata file',
                        required=True)

    args = parser.parse_args()

    samples_set, target_group = fetch_metadata(args.group_type,
                                               args.sample_attributes)

    output = open(args.output_file, 'w')
    for i in range(len(target_group)):
        output.write(target_group[i] + ': ')
        for j in range(len(samples_set[target_group[i]])):
            output.write(samples_set[target_group[i]][j])
            if j != len(samples_set[target_group[i]]) - 1:
                output.write(' ')
            # If we're not at the last value, put in a new line
        if i != len(target_group) - 1:
            output.write('\n')
    output.close()

    sys.exit(0)


if __name__ == '__main__':
    main()
