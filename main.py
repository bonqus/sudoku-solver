import argparse

import numpy as np

from prettyprint import print_sudoku
from solver import solve_sudoku

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Solves sudoku(s) to standard output.')
    parser.add_argument('sudoku', nargs='+', help='path to sudoku')
    args = parser.parse_args()

    if args.sudoku is not None:
        for f in args.sudoku:
            sudoku = np.loadtxt(f, delimiter=',')
            sudoku_solved = solve_sudoku(sudoku)
            print_sudoku(sudoku_solved)
