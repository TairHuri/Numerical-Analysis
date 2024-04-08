"""
Input function f, initial guesses x0 and x1, tolerance TOL, maximum iterations N

For n from 1 to N:
    Calculate the slope using secant method:
        slope = (f(x1) - f(x0)) / (x1 - x0)

    Calculate the change in x using the secant method:
        d = f(x1) / slope

    If the absolute value of d is less than TOL:
        Return x1 as the approximate root

    Update x0 and x1 for the next iteration:
        x0 = x1
        x1 = x1 - d

Return x1 as the current approximation if the maximum iterations are reached

"""

from colors import bcolors


def secant_method(f, x0, x1, TOL, N=50):
    print("{:<10} {:<15} {:<15} {:<15}".format("Iteration", "xo", "x1", "p"))
    for i in range(N):
        if f(x1) - f(x0) == 0:
            print( " method cannot continue.")
            return

        p = x0 - f(x0) * ((x1 - x0) / (f(x1) - f(x0)))

        if abs(p - x1) < TOL:
            return p  # Procedure completed successfully
        print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f}".format(i, x0, x1,p))
        x0 = x1
        x1 = p
    return p


if __name__ == '__main__':
    f = lambda x: x**2 - 5*x +2
    x0 = 80
    x1 = 100
    TOL = 1e-6
    N = 20
    roots = secant_method(f, x0, x1, TOL, N)
    print(bcolors.OKBLUE, f"\n The equation f(x) has an approximate root at x = {roots}", bcolors.ENDC)