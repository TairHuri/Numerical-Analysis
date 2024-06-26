"""
 * Authors: Maor Arnon (ID: 205974553) and Neriya Zudi (ID:207073545)
 * Emails: maorar1@ac.sce.ac.il    neriyazudi@Gmail.com
 * Department of Computer Engineering - Assignment 5 - Numeric Analytics
"""

from sympy import tan
from math import e
import sympy as sp
import math


def PrintMatrix(matrix):
    """
    Matrix Printing Function
    :param matrix: Matrix nxn
    """
    for line in matrix:
        line.append('|')
        line.insert(0,'|')
        print('  '.join(map(str, line)))
        line.remove('|',)
        line.remove('|',)


def Determinant(matrix, mul):
    """
    Recursive function for determinant calculation
    :param matrix: Matrix nxn
    :param mul: The double number
    :return: determinant of matrix
    """
    width = len(matrix)
    # Stop Conditions
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        det = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            # Change the sign of the multiply number
            sign *= -1
            #  Recursive call for determinant calculation
            det = det + mul * Determinant(m, sign * matrix[0][i])
    return det


def MaxNorm(matrix):
    """
    Function for calculating the max-norm of a matrix
    :param matrix: Matrix nxn
    :return:max-norm of a matrix
    """
    max_norm = 0
    for i in range(len(matrix)):
        norm = 0
        for j in range(len(matrix)):
            # Sum of organs per line with absolute value
            norm += abs(matrix[i][j])
        # Maximum row amount
        if norm > max_norm:
            max_norm = norm

    return max_norm


def MultiplyMatrix(matrixA, matrixB):
    """
    Function for multiplying 2 matrices
    :param matrixA: Matrix nxn
    :param matrixB: Matrix nxn
    :return: Multiplication between 2 matrices
    """
    # result matrix initialized as singularity matrix
    result = [[0 for y in range(len(matrixB[0]))] for x in range(len(matrixA))]
    for i in range(len(matrixA)):
        # iterate through columns of Y
        for j in range(len(matrixB[0])):
            # iterate through rows of Y
            for k in range(len(matrixB)):
                result[i][j] += matrixA[i][k] * matrixB[k][j]
    return result


def MakeIMatrix(cols, rows):
    # Initialize a identity matrix
    return [[1 if x == y else 0 for y in range(cols)] for x in range(rows)]


def InverseMatrix(matrix,vector):
    """
    Function for calculating an inverse matrix
    :param matrix:  Matrix nxn
    :return: Inverse matrix
    """
    # Unveri reversible matrix
    if Determinant(matrix, 1) == 0:
        print("Error,Singular Matrix\n")
        return
    # result matrix initialized as singularity matrix
    result = MakeIMatrix(len(matrix), len(matrix))
    # loop for each row
    for i in range(len(matrix[0])):
        # turn the pivot into 1 (make elementary matrix and multiply with the result matrix )
        # pivoting process
        matrix, vector = RowXchange(matrix, vector)
        elementary = MakeIMatrix(len(matrix[0]), len(matrix))
        elementary[i][i] = 1/matrix[i][i]
        result = MultiplyMatrix(elementary, result)
        matrix = MultiplyMatrix(elementary, matrix)
        # make elementary loop to iterate for each row and subtracrt the number below (specific) pivot to zero  (make
        # elementary matrix and multiply with the result matrix )
        for j in range(i+1, len(matrix)):
            elementary = MakeIMatrix(len(matrix[0]), len(matrix))
            elementary[j][i] = -(matrix[j][i])
            matrix = MultiplyMatrix(elementary, matrix)
            result = MultiplyMatrix(elementary, result)


    # after finishing with the lower part of the matrix subtract the numbers above the pivot with elementary for loop
    # (make elementary matrix and multiply with the result matrix )
    for i in range(len(matrix[0])-1, 0, -1):
        for j in range(i-1, -1, -1):
            elementary = MakeIMatrix(len(matrix[0]), len(matrix))
            elementary[j][i] = -(matrix[j][i])
            matrix = MultiplyMatrix(elementary, matrix)
            result = MultiplyMatrix(elementary, result)

    return result


def RowXchange(matrix, vector):
    """
    Function for replacing rows with both a matrix and a vector
    :param matrix: Matrix nxn
    :param vector: Vector n
    :return: Replace rows after a pivoting process
    """

    for i in range(len(matrix)):
        max = abs(matrix[i][i])
        for j in range(i, len(matrix)):
            # The pivot member is the maximum in each column
            if abs(matrix[j][i]) > max:
                temp = matrix[j]
                temp_b = vector[j]
                matrix[j] = matrix[i]
                vector[j] = vector[i]
                matrix[i] = temp
                vector[i] = temp_b
                max = abs(matrix[i][i])

    return [matrix, vector]


def GaussJordanElimination(matrix, vector):
    """
    Function for moding a linear equation using gauss's elimination method
    :param matrix: Matrix nxn
    :param vector: Vector n
    :return: Solve Ax=b -> x=A(-1)b
    """
    # Pivoting process
    matrix, vector = RowXchange(matrix, vector)
    # Inverse matrix calculation
    invert = InverseMatrix(matrix,vector)
    return MulMatrixVector(invert, vector)


def MulMatrixVector(InversedMat, b_vector):
    """
    Function for multiplying a vector matrix
    :param InversedMat: Matrix nxn
    :param b_vector: Vector n
    :return: Result vector
    """
    result = []
    # Initialize the x vector
    for i in range(len(b_vector)):
        result.append([])
        result[i].append(0)
    # Multiplication of inverse matrix in the result vector
    for i in range(len(InversedMat)):
        for k in range(len(b_vector)):
            result[i][0] += InversedMat[i][k] * b_vector[k][0]
    return result


def UMatrix(matrix,vector):
    """
    :param matrix: Matrix nxn
    :return:Disassembly into a  U matrix
    """
    # result matrix initialized as singularity matrix
    U = MakeIMatrix(len(matrix), len(matrix))
    # loop for each row
    for i in range(len(matrix[0])):
        # pivoting process
        matrix, vector = RowXchageZero(matrix, vector)
        for j in range(i + 1, len(matrix)):
            elementary = MakeIMatrix(len(matrix[0]), len(matrix))
            # Finding the M(ij) to reset the organs under the pivot
            elementary[j][i] = -(matrix[j][i])/matrix[i][i]
            matrix = MultiplyMatrix(elementary, matrix)
    # U matrix is a doubling of elementary matrices that we used to reset organs under the pivot
    U = MultiplyMatrix(U, matrix)
    return U


def LMatrix(matrix,vector):
    """
       :param matrix: Matrix nxn
       :return:Disassembly into a  L matrix
       """
    # Initialize the result matrix
    L = MakeIMatrix(len(matrix), len(matrix))
    # loop for each row
    for i in range(len(matrix[0])):
        # pivoting process
        matrix, vector = RowXchageZero(matrix, vector)
        for j in range(i + 1, len(matrix)):
            elementary = MakeIMatrix(len(matrix[0]), len(matrix))
            # Finding the M(ij) to reset the organs under the pivot
            elementary[j][i] = -(matrix[j][i])/matrix[i][i]
            # L matrix is a doubling of inverse elementary matrices
            L[j][i] = (matrix[j][i]) / matrix[i][i]
            matrix = MultiplyMatrix(elementary, matrix)

    return L


def RowXchageZero(matrix,vector):
    """
      Function for replacing rows with both a matrix and a vector
      :param matrix: Matrix nxn
      :param vector: Vector n
      :return: Replace rows after a pivoting process
      """

    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            # The pivot member is not zero
            if matrix[i][i] == 0:
                temp = matrix[j]
                temp_b = vector[j]
                matrix[j] = matrix[i]
                vector[j] = vector[i]
                matrix[i] = temp
                vector[i] = temp_b


    return [matrix, vector]



def SolveLU(matrix, vector):
    """
    Function for deconstructing a linear equation by ungrouping LU
    :param matrix: Matrix nxn
    :param vector: Vector n
    :return: Solve Ax=b -> x=U(-1)L(-1)b
    """
    matrixU = UMatrix(matrix)
    matrixL = LMatrix(matrix)
    return MultiplyMatrix(InverseMatrix(matrixU), MultiplyMatrix(InverseMatrix(matrixL), vector))


def Cond(matrix, invert):
    """
    :param matrix: Matrix nxn
    :param invert: Inverted matrix
    :return: CondA = ||A|| * ||A(-1)||
    """
    print("\n|| A ||max = ", MaxNorm(matrix))
    print("\n|| A(-1) ||max = ", MaxNorm(invert))
    return MaxNorm(matrix)*MaxNorm(invert)


def solveMatrix(matrixA,vectorb):
    detA = Determinant(matrixA, 1)
    print("\nMatrix A: \n")
    PrintMatrix(matrixA)
    print("\nVector b: \n")
    PrintMatrix(vectorb)
    print("\nDET(A) = ", detA)
    if detA != 0:
        print("\nCondA = ", Cond(matrixA, InverseMatrix(matrixA,vectorb)))
        print("\nGaussJordanElimination")
        print("Solve Ax = b \n")
        result = GaussJordanElimination(matrixA, vectorb)
        PrintMatrix(result)
        return result
    else:
        print("Singular Matrix\n")
        print("\nLU Decomposition \n")
        print("Matrix U: \n")
        PrintMatrix(UMatrix(matrixA,vectorb))
        print("\nMatrix L: \n")
        PrintMatrix(LMatrix(matrixA,vectorb))
        print("\nMatrix A=LU: \n")
        result = MultiplyMatrix(LMatrix(matrixA,vectorb),UMatrix(matrixA,vectorb))
        PrintMatrix(result)
        return result


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[90m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    # Background colors:
    GREYBG = '\033[100m'
    REDBG = '\033[101m'
    GREENBG = '\033[102m'
    YELLOWBG = '\033[103m'
    BLUEBG = '\033[104m'
    PINKBG = '\033[105m'
    CYANBG = '\033[106m'


def LinearInterpolation(table_points, point):
    p = []
    result = 0
    flag = 1
    for i in range(len(table_points)):
        p.append(table_points[i][0])
    for i in range(len(p) - 1):
        if i <= point <= i + 1:
            x1 = table_points[i][0]
            x2 = table_points[i + 1][0]
            y1 = table_points[i][1]
            y2 = table_points[i + 1][1]
            result = (((y1 - y2) / (x1 - x2)) * point) + ((y2 * x1) - (y1 * x2)) / (x1 - x2)
            print(bcolors.OKBLUE, "The approximation (interpolation) of the point ", point, " is: ", round(result, 4),
                  bcolors.ENDC)
            flag = 0
    if flag:
        x1 = table_points[0][0]
        x2 = table_points[1][0]
        y1 = table_points[0][1]
        y2 = table_points[1][1]
        m = (y1 - y2) / (x1 - x2)
        result = y1 + m * (point - x1)
        print(bcolors.OKBLUE, "The approximation (extrapolation) of the point ", point, " is: ", round(result, 4),
              bcolors.ENDC)


def PolynomialMethod(table_points, x):
    matrix = [[point[0] ** i for i in range(len(table_points))] for point in table_points] #Makes the initial matrix
    b = [[point[1]] for point in table_points]

    print(bcolors.OKBLUE, "The matrix is- ",bcolors.ENDC)
    PrintMatrix(matrix)
    print(bcolors.OKBLUE, "b vector is- ",bcolors.ENDC)
    print(b)
    print(bcolors.OKBLUE, "The Solotion:",bcolors.ENDC)
    matrixSol = solveMatrix(matrix,b)

    result = sum([matrixSol[i][0] * (x ** i) for i in range(len(matrixSol))])
    print('+'.join([ '('+str(matrixSol[i][0])+') * x ^ ' + str(i) + ' ' for i in range(len(matrixSol))]) , '= ' )
    print(bcolors.OKBLUE, "Result:",bcolors.ENDC)
    print(result)
    return result


def NevAlgorithm(table_points,x):
    tot = 0
    size = len(table_points)
    temp_table = [[point[0],point[1]] for point in table_points]
    for j in range(1,size):
        for i in range(size-1,j-1,-1):
            temp_table[i][1]=((x-temp_table[i-j][0])*temp_table[i][1] - (x-temp_table[i][0])*temp_table[i-1][1] )/ (temp_table[i][0]-temp_table[i-j][0])
    tot = temp_table[size-1][1]
    print(bcolors.OKBLUE, "The approximation (interpolation) of the point ", x, " is: ", round(tot, 4),
          bcolors.ENDC)
    return tot





def LagrangeMethod(table_points, point):
    xp = []
    yp = []
    result = 0
    for i in range(len(table_points)):
        xp.append(table_points[i][0])
        yp.append(table_points[i][1])
    for i in range(len(table_points)):
        lagrange_i = 1
        for j in range(len(table_points)):
            if i != j:
                lagrange_i = lagrange_i * (point-xp[j])/(xp[i]-xp[j])
        result += lagrange_i * yp[i]

    print(bcolors.OKBLUE, "The approximation (interpolation) of the point ", point, " is: ", round(result, 4), bcolors.ENDC)



def MainFunction():
    table_points = [(1, 1), (2, 0), (5, 2)]
    x = 3
    print(bcolors.OKBLUE, "Interpolation & Extrapolation Methods\n", bcolors.ENDC)
    print(bcolors.OKBLUE, "Table Points", table_points, bcolors.ENDC)
    print(bcolors.OKGREEN, "Finding an approximation to the point ", x, bcolors.ENDC)
    choice = int(input(
        "Which method do you want? \n\t1.Linear Method \n\t2.Polynomial Method\n\t3.Lagrange Method\n\t4.Neville Method\n"))
    if choice == 1:
        LinearInterpolation(table_points, x)
    elif choice == 2:
        PolynomialMethod(table_points, x)
    elif choice == 3:
        LagrangeMethod(table_points, x)
    elif choice == 4:
        NevAlgorithm(table_points,x)

    else:
        print(bcolors.FAIL, "Invalid input", bcolors.ENDC)
        return


MainFunction()
