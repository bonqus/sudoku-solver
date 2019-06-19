# Pretty printer module


def sudoku(f, sudoku, elapsed):
    print(f + ': Solved in ', '{:.3g}'.format(elapsed), 's')
    row = ('+' + '-'*7)*3 + '+'
    for i in range(9):
        if i % 3 == 0:
            print(row)
        for j in range(9):
            if j % 3 == 0:
                print('|', end=' ')
            print(int(sudoku[i, j]), end=' ')
        print('|')
    print(('+' + '-'*7)*3 + '+')


def no_solution(f):
    print(f + ': Is unsolvable.')


def no_file(f):
    print(f + ': No such file')


def not_sudoku(f):
    print(f + ': Is not a Sudoku')


def is_directory(f):
    print(f + ': Is a directory, not a Sudoku')


def shape_error(f, shape):
    print(f + ': Has a', shape, 'shape, this solver only supports (9, 9)')
