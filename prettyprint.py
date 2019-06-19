def print_sudoku(sudoku):
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


def print_no_solution(f):
    print(f, 'is unsolvable.')
