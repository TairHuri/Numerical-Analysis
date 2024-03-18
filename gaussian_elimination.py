# @source: https://github.com/lihiSabag/Numerical-Analysis-2023.git

import numpy as np
from colors import bcolors
from Matrix.inverse_matrix import inverse
from matrix_utility import swap_row

def gaussianElimination(mat):
    N = len(mat)
    singular_flag = forward_substitution(mat)
    if singular_flag != -1:

        if mat[singular_flag][N]:
            return "Singular Matrix (Inconsistent System)"
        else:
            return "Singular Matrix (May have infinitely many solutions)"

# if matrix is non-singular:
    forward_substitution_to_diagonal(mat)
    print(np.array(mat))
    # get solution to system using backward substitution
    return backward_substitution(mat)
# The function receives an upper triangular matrix and returns a fully ranked matrix
""""
def forward_substitution(mat):
    N = len(mat)
    for k in range(N):

        # Partial Pivoting: Find the pivot row with the largest absolute value in the current column
        pivot_row = k
        v_max = abs(mat[pivot_row][k])
        for i in range(k + 1, N):
            if abs(mat[i][k]) > v_max:
                v_max = abs(mat[i][k])
                pivot_row = i

        # if a principal diagonal element is zero,it denotes that matrix is singular,
        # and will lead to a division-by-zero later.
        if not mat[k][pivot_row]:
        if not mat[pivot_row][k]:
            return k  # Matrix is singular

        # Swap the current row with the pivot row
        if pivot_row != k:
            swap_row(mat, k, pivot_row)
        # End Partial Pivoting
        for i in range(k + 1, N):

            #  Compute the multiplier
            m = (mat[i][k] / mat[k][k])

            # subtract fth multiple of corresponding kth row element
            for j in range(k + 1, N + 1):
                mat[i][j] -= (mat[k][j] * m)
                if abs(mat[i][j]) < np.finfo(float).eps:
                    mat[i][j] = 0

            # filling lower triangular matrix with zeros
            mat[i][k] = 0
    return -1
"""
def forward_substitution(mat):
    N = len(mat)
    for k in range(N):
        pivot_row = k
        v_max = abs(mat[k][k])  # Setting the maximum value to the diagonal element itself
        for i in range(k + 1, N):
            if abs(mat[i][k]) > v_max:
                v_max = abs(mat[i][k])
                pivot_row = i

        if not mat[pivot_row][k]:  # Checking if the diagonal element is zero
            return k  # Matrix is singular

        # Swap the current row with the pivot row
        if pivot_row != k:
            # Swap entire rows, including the augmented column
            mat[k], mat[pivot_row] = mat[pivot_row], mat[k]
        # End Partial Pivoting
        for i in range(k + 1, N):
            m = (mat[i][k] / mat[k][k])
            for j in range(k + 1, N + 1):
                mat[i][j] -= (mat[k][j] * m)
                if abs(mat[i][j]) < 1e-10:  # Small values are treated as zeros
                    mat[i][j] = 0

            mat[i][k] = 0  # Ensure lower triangular elements are zeroed out
    return -1
# function to calculate the values of the unknowns
def forward_substitution_to_diagonal(mat):
    N = len(mat)
    for k in range(N - 1, -1, -1):
        scalar = mat[k][k]
        for j in range(N + 1):
            mat[k][j] /= scalar

        for i in range(k - 1, -1, -1):
            scalar = mat[i][k]
            for j in range(N + 1):
                mat[i][j] -= mat[k][j] * scalar
def backward_substitution(mat):
    N = len(mat)
    x = np.zeros(N)  # An array to store solution
    # Start calculating from last equation up to the first
    for i in range(N - 1, -1, -1):
        x[i] = mat[i][N]
        # Initialize j to i+1 since matrix is upper triangular
        for j in range(i + 1, N):
            x[i] -= mat[i][j] * x[j]
        x[i] = (x[i] / mat[i][i])
    return x
def norm(mat):
    size = len(mat)
    max_row = 0
    for row in range(size):
        sum_row = 0
        for col in range(size):
            sum_row += abs(mat[row][col])
        if sum_row > max_row:
            max_row = sum_row
    return max_row
if __name__ == '__main__':

    CB = [[1,    2,     3],
          [4, 7, 11]]
    """norm_A = norm(CB)
    print("\nThe norm of the matrix CB is ", norm_A)"""

    """A_b = [
            [1,  -1,   2,  -1,  -8],
            [2,  -2,   3,  -3, -20],
            [1,   1,   1,   0,  -2],
            [1,  -1,   4,   3,   4]]"""
    AB = [
             [1,   2,     3,    4,     5],
             [2,   3,     4,    5,     1],
             [8,   8,     8,    8,     1],
             [24, 15,     22,   1,     8],]

    result = gaussianElimination(CB)
    if isinstance(result, str):
        print(result)
    else:
        print(bcolors.OKBLUE,"\nSolution for the system:")
        for x in result:
            print("{:.6f}".format(x))
    """        
    print("\n")
    result = gaussianElimination(AB)
    if isinstance(result, str):
        print(result)
    else:
        print(bcolors.OKBLUE,"\nSolution for the system:")
        for x in result:
            print("{:.6f}".format(x))
    result = gaussianElimination(CB)
    if isinstance(result, str):
        print(result)
    else:
        print(bcolors.OKBLUE, "\nSolution for the system:")
        for x in result:
            print("{:.6f}".format(x))"""

"""norm_A_inv = norm(A_inverse)"""
"""condA = norm_A * norm_A_inv"""
"""if condA > 99:
    print("Cannot solve, change the conditions")
print(bcolors.OKBLUE, "A:", bcolors.ENDC)
print_matrix(A)
print(bcolors.OKBLUE, "Max Norm of A:", bcolors.ENDC, norm_A, "\n")
print(bcolors.OKBLUE, "max norm of the inverse of A:", bcolors.ENDC, norm_A_inv)"""