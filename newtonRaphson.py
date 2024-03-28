from colors import bcolors
import sympy as sp

def newton_raphson(f, p0, TOL, N):
    x = sp.symbols('x')  # Define symbol for differentiation
    df = sp.diff(f(x), x)  # Calculate the derivative of f with respect to x
    df_func = sp.lambdify(x, df)  # Convert the derivative expression to a callable function

    print("{:<10} {:<15} {:<15} ".format("Iteration", "po", "p1"))
    for i in range(N):
        if df_func(p0) == 0:
            print("Derivative is zero at p0, method cannot continue.")
            return None  # Return None if derivative is zero

        p = p0 - f(p0) / df_func(p0)
        t = abs(p - p0)
        if abs(t) < TOL:  # Check if difference between p and p0 is below tolerance
            return p  # Procedure completed successfully
        print("{:<10} {:<15.9f} {:<15.9f} ".format(i, p0, p))
        p0 = p
    return None


if __name__ == '__main__':
    f = lambda x: x**2 - 5*x + 2
    p0 = 0
    TOL = 0.0000001
    N = 100
    roots = newton_raphson(f, p0, TOL, N)
    if roots is not None:
        print(bcolors.OKBLUE, "\nThe equation f(x) has an approximate root at x = {:<15.9f} ".format(roots), bcolors.ENDC,)
