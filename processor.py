import sys
import copy


def display_menu(menu='MAIN'):
    if menu == 'MAIN':
        print("\n1. Add matrices\n"
              "2. Multiply matrix by a constant\n"
              "3. Multiply matrices\n"
              "4. Transpose matrix\n"
              "5. Calculate a determinant\n"
              "6. Inverse matrix\n"
              "0. Exit\n")
    elif menu == 'TRANSPOSE':
        print("\n1. Main diagonal\n"
              "2. Side diagonal\n"
              "3. Vertical line\n"
              "4. Horizontal line\n")


def display_matrix(matrix):
    str_arr = matrix
    print('The result is:')
    for j in range(len(matrix)):
        for jj in range(len(matrix[0])):
            str_arr[j][jj] = str(matrix[j][jj])
    for j in range(len(matrix)):
        print(' '.join(matrix[j]))


def make_matrix(n=None, m=None, zeros=0):
    matrix = []
    if n is None or m is None:
        n, m = list(input().split())
    else:
        pass
    n = int(n)
    m = int(m)
    if zeros:
        for k in range(n):
            row = [0 for x in range(m)]
            matrix.append(row)
    else:
        print("Enter matrix:")
        for k in range(n):
            row = list(input().split())
            row = [float(x) for x in row]
            matrix.append(row)
    return matrix


def multiplication_by_constant(matrix, constant):
    for j in range(len(matrix)):
        for jj in range(len(matrix[0])):
            matrix[j][jj] = round(matrix[j][jj] * constant, 3)
    return matrix


def add_matrices(matrix1, matrix2):
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        matrix3 = matrix1
        for j in range(len(matrix1)):
            for jj in range(len(matrix1[0])):
                matrix3[j][jj] = matrix1[j][jj] + matrix2[j][jj]
        return matrix3
    else:
        print("ERROR\n")


def multiply_matrices(matrix1, matrix2):
    matrix3 = make_matrix(len(matrix1), len(matrix2[0]), zeros=1)
    for j in range(len(matrix1)):
        for jj in range(len(matrix2[0])):
            cell = 0
            for i in range(len(matrix1[0])):
                cell += matrix1[j][i] * matrix2[i][jj]
            matrix3[j][jj] = cell
    return matrix3


def transpose_matrix(matrix, action='MAIN_DIAGONAL'):
    if action == 'MAIN_DIAGONAL':
        matrix_transposed = []
        for jj in range(len(matrix[0])):
            row = []
            for j in range(len(matrix)):
                row.append(matrix[j][jj])
            matrix_transposed.append(row)
    elif action == 'SIDE_DIAGONAL':
        matrix_transposed = []
        for jj in range(len(matrix[0])):
            row = []
            for j in range(len(matrix)):
                row.append(matrix[j][jj])
            matrix_transposed.append(row[::-1])
        matrix_transposed = transpose_matrix(transpose_matrix(transpose_matrix(matrix_transposed), 'VERTICAL_LINE'))
    elif action == 'VERTICAL_LINE':
        matrix_transposed = []
        for row in matrix:
            matrix_transposed.append(row[::-1])
    elif action == 'HORIZONTAL_LINE':
        matrix_transposed = transpose_matrix(transpose_matrix(transpose_matrix(matrix), 'VERTICAL_LINE'))
    return matrix_transposed


def get_determinant(mat):
    if len(mat) == 1:
        return mat[0][0]
    elif len(mat[0]) == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    else:
        row = mat[0]
        temp_sum = 0
        for i in range(len(mat)):
            minor_mat = mat[1::]
            minor_mat = transpose_matrix(minor_mat)
            del minor_mat[i]
            minor_mat = transpose_matrix(minor_mat)
            if i % 2 == 1:
                sign = -1
            else:
                sign = 1
            temp_sum += sign * row[i] * get_determinant(minor_mat)
        return temp_sum


def get_cofactors(mat):
    cofactors_mat = copy.deepcopy(mat)
    for j in range(len(mat)):
        for jj in range(len(mat[0])):
            minor_mat = copy.deepcopy(mat)
            del minor_mat[j]
            minor_mat = transpose_matrix(minor_mat)
            del minor_mat[jj]
            minor_mat = transpose_matrix(minor_mat)
            sign = (-1)**(jj+j)
            cofactors_mat[j][jj] = sign * get_determinant(minor_mat)
    return cofactors_mat


while 1:
    display_menu()
    key = input()
    print(f"Your choice: > {key}")
    if key == '1':
        n, m = list(input("Enter size of first matrix: ").split())
        A = make_matrix(n, m)
        n, m = list(input("Enter size of second matrix: ").split())
        B = make_matrix(n, m)
        print("The result is: ")
        display_matrix(add_matrices(A, B))
    elif key == '2':
        n, m = list(input("Enter size of matrix: ").split())
        A = make_matrix(n, m)
        constant = int(input("Enter constant: "))
        print("The result is: ")
        display_matrix(multiplication_by_constant(A, constant))
    elif key == '3':
        n, m = list(input("Enter size of first matrix: ").split())
        A = make_matrix(n, m)
        n, m = list(input("Enter size of second matrix: ").split())
        B = make_matrix(n, m)
        print("The result is: ")
        display_matrix(multiply_matrices(A, B))
    elif key == '4':
        display_menu('TRANSPOSE')
        key_trans = input()
        print(f"Your choice: {key_trans}")
        n, m = list(input("Enter size of matrix: ").split())
        A = make_matrix(n, m)
        if key_trans == '1':
            display_matrix(transpose_matrix(A))
        elif key_trans == '2':
            display_matrix(transpose_matrix(A, 'SIDE_DIAGONAL'))
        elif key_trans == '3':
            display_matrix(transpose_matrix(A, 'VERTICAL_LINE'))
        elif key_trans == '4':
            display_matrix(transpose_matrix(A, 'HORIZONTAL_LINE'))
        else:
            pass
    elif key == '5':
        n, m = list(input("Enter size of matrix: ").split())
        A = make_matrix(n, m)
        print("The result is:\n ", get_determinant(A))
    elif key == '6':
        n, m = list(input("Enter size of matrix: ").split())
        A = make_matrix(n, m)
        cof_mat = get_cofactors(A)
        if get_determinant(A) != 0:
            display_matrix(multiplication_by_constant(transpose_matrix(cof_mat), 1 / get_determinant(A)))
        else:
            print("This matrix doesn't have an inverse.\n")
    elif key == '0':
        sys.exit()
    else:
        pass
