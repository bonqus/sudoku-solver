import argparse

import numpy as np

from solver import solve_sudoku

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solves sudoku and prints it to stndard output')
    parser.add_argument('sudoku', nargs='+', help='path to sudoku')

    args = parser.parse_args()

    if args.sudoku is not None:
        for f in args.sudoku:
            sudoku = np.loadtxt(f, delimiter=',')
            print(solve_sudoku(sudoku))
