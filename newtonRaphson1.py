"""
Input function f, initial guess x0, tolerance TOL, maximum iterations N

For n from 1 to N:
    Calculate the derivative of the function at x0:
        df = derivative of f at x0

    If df ≈ 0:
        Print "Derivative is approximately zero. Algorithm failed."
        Exit

    Calculate the change in x using Newton-Raphson method:
        d = f(x0) / df

    If the absolute value of d is less than TOL:
        Return x0 as the approximate root

    Update x0 for the next iteration:
        x0 = x0 - d

Return x0 as the current approximation if the maximum iterations are reached

"""
from colors import bcolors

def derivative(f, x, h=1e-6):
    return (f(x + h) - f(x)) / h

def newton_raphson(f, p0, TOL, N=50):
    print("{:<10} {:<15} {:<15} ".format("Iteration", "p0", "p1"))
    for i in range(N):
        df_p0 = derivative(f, p0)
        if df_p0 == 0:
            print("Derivative is zero at p0, method cannot continue.")
            return

        p = p0 - f(p0) / df_p0

        if abs(p - p0) < TOL:
            return p  # Procedure completed successfully
        print("{:<10} {:<15.9f} {:<15.9f} ".format(i, p0, p))
        p0 = p
    return p



if __name__ == '__main__':
    f = lambda x: x**3 - 3*x**2
    p0 = -5
    TOL = 1e-6
    N = 100
    roots = newton_raphson(f,p0,TOL,N)
    print(bcolors.OKBLUE,"\nThe equation f(x) has an approximate root at x = {:<15.9f} ".format(roots),bcolors.ENDC,)