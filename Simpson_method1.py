import sympy as sp
from colors import bcolors
from sympy.utilities.lambdify import lambdify

x = sp.symbols('x')

def simpsons_rule(f, a, b, n):
    """
    Simpson's Rule for Numerical Integration

    Parameters:
    f (function): The function to be integrated.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    n (int): The number of subintervals (must be even).

    Returns:
    float: The approximate definite integral of the function over [a, b].
    """
    if n % 2 != 0:
        raise ValueError("Number of subintervals (n) must be even for Simpson's Rule.")

    h = (b - a) / n

    integral = f(a) + f(b)  # Initialize with endpoints

    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x_i)
        else:
            integral += 4 * f(x_i)

    integral *= h / 3

    return integral

def simpsons_error(f, a, b, n):
    """
    Calculate the error estimation for Simpson's Rule.

    Parameters:
    f (function): The function to be integrated.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    n (int): The number of subintervals.

    Returns:
    float: The error estimation.
    """
    h = (b - a) / n
    xsi = 1  # Chosen upper bound

    # Compute the fourth derivative of f
    f4_expr = sp.diff(f, x, 4)
    f4_func = lambdify(x, f4_expr)

    f4 = f4_func(xsi)

    error = (1 / 180) * (h ** 4) * (b - a) * f4
    return error

if __name__ == '__main__':
    f_expr = sp.exp(x ** 2)
    f = lambdify(x, f_expr)

    n = 4
    a = 0
    b = 1

    print(f"Division into n={n} sections")
    integral = simpsons_rule(f, a, b, n)
    print(bcolors.OKBLUE, f"Numerical Integration of definite integral in range [{a},{b}] is {integral}", bcolors.ENDC)

    error = simpsons_error(f_expr, a, b, n)
    print(bcolors.OKBLUE, f"Error estimation for Simpson's Rule: {error}", bcolors.ENDC)
