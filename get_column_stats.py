"""Performs various operations

    * main - Returns the mean and standard deviation of desired
             column from file
"""
import sys
import math
import argparse


def list_mean(L):
    """Compute the mean of a list of numbers.

    Parameters
    __________
    L : list of numbers

    Returns
    _______
    mean of numbers
    """
    if L is None:
        raise TypeError('List is of incorrect type.')

    if len(L) == 0:
        raise ZeroDivisionError('Divide by zero. List may be empty.')

    print('here')
    return sum(L) / len(L)


def stdev(L):
    """Compute the standard deviation of a list of numbers.

    Parameters
    __________
    V : list of numbers

    Returns
    _______
    standard deviation of V based on mean
    """
    if L is None:
        raise TypeError('List is of inccorect type.')

    if len(L) == 0:
        raise ZeroDivisionError('Divide by zero.')

    m = list_mean(L)
    return math.sqrt(sum([(m-x)**2 for x in L]) / len(L))


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

    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('File not found.')
        sys.exit(1)
    except Exception:
        print('File could not be opened properly.')
        sys.exit(1)

    V = []

    for L in f:
        try:
            A = [int(x) for x in L.split('\t')]
            V.append(int(A[col_num]))
        except ValueError:
            print('File contains a non integer character!')
            sys.exit(1)
        except IndexError:
            print('Column number is out of range!')
            sys.exit(1)

    try:
        mean = list_mean(V)
        std = stdev(V)
    except TypeError:
        print('Input was of the incorrect type.')
        sys.exit(1)
    except ZeroDivisionError:
        print('Divide by zero! File may be empty.')
        sys.exit(1)

    print('mean:', mean)
    print('stdev:', std)


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
