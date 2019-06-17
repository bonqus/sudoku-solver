import numpy as np

# Recursive backtracking sudoku solver


class Sudoku():
    def __init__(self, sudoku):
        self.sudoku = sudoku

    def __getitem__(self, key):
        return self.sudoku[key]

    def __setitem__(self, key, value):
        self.sudoku[key] = value

    # def __repr__(self):
    #     out = ""
    #     for row in self.sudoku:
    #         for val in row:
    #             if (val != 0):
    #                 out = out + str(val)
    #             else:
    #                 out = out + " "
    #             if val
    #         out += "\n"
    #     return out

    # def __iter__(self):
    #     for i in range(9):
    #         for j in range(9):
    #             yield i, j


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
        else:
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


class SudokuSolver ():
    def __init__(self, sudoku):
        self.sudoku = sudoku

    def solve(self, sudoku, x, y):
        if self.sudoku[x, y] != 0:
            if x < 8:
                return self.solve(sudoku, x+1, y)
            elif y < 8:
                return self.solve(sudoku, 0, y+1)
            else:
                return sudoku
        while sudoku[x, y] < 9:
            sudoku[x, y] += 1
            if self.constraints(sudoku, x, y):
                tmp = None
                if x < 8:
                    tmp = self.solve(sudoku, x+1, y)
                elif y < 8:
                    tmp = self.solve(sudoku, 0, y+1)
                if tmp is not None:
                    return tmp
        sudoku[x, y] = 0
        return None

    def pretty_print(self):
        print(self.sudoku)

    def constraints(self, sudoku, x, y):
        return (self.row(sudoku, x) and self.column(sudoku, y) and
                self.box(sudoku, x, y))

    def row(self, sudoku, row):
        return SudokuSolver.unique(sudoku[row, :])

    def column(self, sudoku, column):
        return SudokuSolver.unique(sudoku[:, column])

    def box(self, sudoku, x, y):
        return SudokuSolver.unique(sudoku[x//3*3:x//3*3+3, y//3*3:y//3*3+3].flatten())

    def unique(collection):
        mem = []
        for number in collection:
            if number not in mem:
                mem.append(number)
            elif number != 0:
                return False
        return True


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
    s = np.array([
        [0, 3, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]])
    print(sudokusolve(s))
    # print(sudoku)
    # print(SudokuSolver(sudoku).solve(sudoku, 0, 0))
