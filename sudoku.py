import numpy as np


def sudokusolve(sudoku):
    """
    A Sudoku solver.

    A solver that finds one of the posible solutions to a Sudoku,
    by recursively backtracking through possible entry values.

    Parameters
    ----------
    sudoku : numpy.array
        An unsolved Sudoku as a numpy.array, with 0'es as empty/unknown values.

    Returns
    -------
    numpy.array
        A solved soduku as a numpy.array or None if it is unsolvable.

    """

    def next_entry(i):
        return (i // 9, i % 9)

    def state(sudoku, i):
        i += 1
        if i == 81:
            return sudoku
        r, c = next_entry(i)
        if sudoku[r, c] == 0:
            return solve(sudoku, i)
        return state(sudoku, i)

    def solve(sudoku, i):
        r, c = next_entry(i)
        sudoku[r, c] += 1
        if sudoku[r, c] > 9:
            sudoku[r, c] = 0
            return None
        if not rules(sudoku, r, c):
            return solve(sudoku, i)
        tmp = state(sudoku, i)
        if tmp is None:
            return solve(sudoku, i)
        return sudoku

    def rules(sudoku, r, c):
        def row(sudoku, row):
            return unique(sudoku[row, :])

        def column(sudoku, column):
            return unique(sudoku[:, column])

        def box(sudoku, r, c):
            return unique(sudoku[r//3*3:r//3*3+3, c//3*3:c//3*3+3].flatten())

        def unique(collection):
            mem = []
            for number in collection:
                if number != 0 and number in mem:
                    return False
                mem.append(number)
            return True

        return (row(sudoku, r) and column(sudoku, c) and box(sudoku, r, c))

    return state(sudoku, -1)


if __name__ == "__main__":
    s = np.array([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 0]])
    print(sudokusolve(s))
