from colors import bcolors

def linearInterpolation(table_points, point):
    p = []
    result = 0
    flag = 1
    for i in range(len(table_points)):
        p.append(table_points[i][0])
    for i in range(len(p) - 1):
        x1 = table_points[i][0]
        x2 = table_points[i + 1][0]
        y1 = table_points[i][1]
        y2 = table_points[i + 1][1]
        if x1 <= point <= x2:
            """
            fix:
            The error in the code lies in the conditional statement if i <= point <= i + 1 within the second loop.
            This condition is not correctly comparing the value of point with the values of i and i + 1, 
            as it typically should in a loop iterating over indices.
            Instead, the condition should check whether the given point (point) lies between two consecutive points in the table, 
            based on their x-values (x1 and x2). Therefore, the condition should compare the given
            point with the x-range within which we want to perform interpolation.

            By adjusting the condition in this manner, we ensure that it properly compares the given 
            point with the range of x-values where we want to conduct interpolation.
            """
            result = (((y1 - y2) / (x1 - x2)) * point) + ((y2 * x1) - (y1 * x2)) / (x1 - x2)
            print(bcolors.OKGREEN, "\nThe approximation (interpolation) of the point ", point, " is: ",bcolors.ENDC, round(result, 4))
            flag = 0
    if flag:
        x1 = table_points[0][0]
        x2 = table_points[1][0]
        y1 = table_points[0][1]
        y2 = table_points[1][1]
        m = (y1 - y2) / (x1 - x2)
        result = y1 + m * (point - x1)
        print(bcolors.OKGREEN, "\nThe approximation (extrapolation) of the point ", point, " is: ",bcolors.ENDC, round(result, 4))


if __name__ == '__main__':

    table_points = [(1, 3), (2, 4), (3, -1)]
    x = 1.5
    print(bcolors.OKBLUE, "----------------- Interpolation & Extrapolation Methods -----------------\n", bcolors.ENDC)
    print(bcolors.OKBLUE, "Table Points: ", bcolors.ENDC, table_points)
    print(bcolors.OKBLUE, "Finding an approximation to the point: ", bcolors.ENDC, x)
    linearInterpolation(table_points, x)
    print(bcolors.OKBLUE, "\n---------------------------------------------------------------------------\n", bcolors.ENDC)
