import argparse
import time
from os.path import exists

from numpy import loadtxt

import prettyprint as pp
from solver import solve_sudoku

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Solves sudoku(s) and writes to standard output')
    parser.add_argument('sudoku', nargs='+', help='path to sudoku')
    parser.add_argument('-p', '--pretty-print', action='store_true',
                        help='pretty print the sudoku')
    args = parser.parse_args()

    if args.sudoku is not None:
        for f in args.sudoku:
            if not exists(f):
                pp.no_file(f)
                continue
            try:
                sudoku = loadtxt(f, delimiter=',')
                if sudoku.shape != (9, 9):
                    pp.shape_error(f, sudoku.shape)
                    continue
                start = time.time()
                sudoku_solved = solve_sudoku(sudoku)
                end = time.time()
                elapsed = end-start
                if sudoku_solved is None:
                    pp.no_solution(f)
                elif args.pretty_print:
                    pp.sudoku(f, sudoku_solved, elapsed)
                else:
                    print(sudoku_solved)
            except ValueError:
                pp.not_sudoku(f)
            except IsADirectoryError:
                pp.is_directory(f)
