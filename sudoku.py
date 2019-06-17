import numpy as np

# Recursive backtracking sudoku solver


def sudokusolve(sudoku):
    def next_pair(i):
        return (i // 9, i % 9)

    def state(sudoku, i):
        i += 1
        if i == 81:
            return sudoku
        x, y = next_pair(i)
        if sudoku[x, y] == 0:
            return solve(sudoku, i)
        return state(sudoku, i)

    def solve(sudoku, i):
        x, y = next_pair(i)
        sudoku[x, y] += 1
        if sudoku[x, y] > 9:
            sudoku[x, y] = 0
            return None
        if not constraints(sudoku, x, y):
            return solve(sudoku, i)
        tmp = state(sudoku, i)
        if tmp is None:
            return solve(sudoku, i)
        return sudoku

    def constraints(sudoku, x, y):
        def row(sudoku, row):
            return unique(sudoku[row, :])

        def column(sudoku, column):
            return unique(sudoku[:, column])

        def box(sudoku, x, y):
            return unique(sudoku[x//3*3:x//3*3+3, y//3*3:y//3*3+3].flatten())

        # def unique(collection):
        #     for c in collection:
        #         if (c != 0 and np.count_nonzero(collection == c) > 1):
        #             return False
        #     return True

        # def unique(collection):
        #     for i in range(9):
        #         for j in range(i):
        #             if collection[i] != 0 and collection[i] == collection[j]:
        #                 return False
        #     return True

        # def unique(collection):
        #     collection = collection[collection != 0]
        #     return len(set(collection)) == len(collection)

        def unique(collection):
            mem = []
            for number in collection:
                if number != 0 and number in mem:
                    return False
                mem.append(number)
            return True

        return (row(sudoku, x) and column(sudoku, y) and box(sudoku, x, y))

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
        [0, 0, 0, 0, 8, 0, 0, 7, 9]])
    print(sudokusolve(s))
