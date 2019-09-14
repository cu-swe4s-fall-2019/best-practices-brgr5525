"""Performs various operations

    * main - Returns the mean and standard deviation of desired
             column from file
"""
import sys
import math
import argparse


def main(file_name, column_num):
    """Compute the mean and std dev of a column of numbers.

    Parameters
    __________
    file_name : name of file
                Non empty file of tab-separated integers.
    column_num : int
                 Number of column whose mean and stdev is desired.

    Returns
    _______
    none
        Prints the mean and standard dev of desired coulumn.
    """

    col_num = int(column_num)

    f = open(file_name, 'r')

    V = []

    for L in f:
        try:
            A = [int(x) for x in L.split('\t')]
        except ValueError:
            L = L[3:]
            A = [int(x) for x in L.split('\t')]
        V.append(A[col_num])

    mean = sum(V) / len(V)

    stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))

    print('mean:', mean)
    print('stdev:', stdev)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                description='Input file name and column number',
                prog='get_column_stats')

    parser.add_argument('--file_name',
                        type=str,
                        help='Name of the file',
                        required=True)

    parser.add_argument('--col_num',
                        type=str,
                        help='The column number',
                        required=True)

    args = parser.parse_args()
    main(args.file_name, args.col_num)
