from random import randrange


def ascending_bubble_sort(_matrix: list, col_sum: list):
    # sort for ascending
    for row in range(len(col_sum)):
        for elem in range(0, len(col_sum) - row - 1):
            if col_sum[elem] > col_sum[elem + 1]:
                for index in range(len(_matrix)):
                    temp = _matrix[index][elem]
                    _matrix[index][elem] = _matrix[index][elem + 1]
                    _matrix[index][elem + 1] = temp
                temp = col_sum[elem]
                col_sum[elem] = col_sum[elem + 1]
                col_sum[elem + 1] = temp

        # bubble sort for columns with special params
        for i in range(len(_matrix)):
            for j in range(len(_matrix)):
                for k in range(0, len(_matrix) - j - 1):
                    if _matrix[k][i] > _matrix[k + 1][i] if i % 2 else _matrix[k][i] < _matrix[k + 1][i]:
                        temp = _matrix[k][i]
                        _matrix[k][i] = _matrix[k + 1][i]
                        _matrix[k + 1][i] = temp


def print_matrix(_matrix: list, col_sum: list, status='Unsorted'):
    # print unsort matrix
    print(f'\n{status.capitalize()} matrix:')
    for row in range(len(_matrix)):
        for elem in range(len(_matrix[row])):
            print(f"{_matrix[row][elem]:<7}", end=" ")
        print()
    for res in range(len(col_sum)):
        # print sorted matrix
        print(f'{col_sum[res]:<7}', end=" ")
    print()


if __name__ == '__main__':
    matrix_size = int(input("Enter size of the matrix (MxM): "))
    while matrix_size < 5:
        matrix_size = int(input("Matrix size (M) should be greater or equal 5: "))
    matrix = [[randrange(1, 51) for column in range(matrix_size)] for row in range(matrix_size)]
    matrix_col_sum = list(map(sum, zip(*matrix)))
    print_matrix(matrix, matrix_col_sum)
    ascending_bubble_sort(matrix, matrix_col_sum)
    print_matrix(matrix, matrix_col_sum, 'sorted')
