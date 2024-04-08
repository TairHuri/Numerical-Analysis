import math
from sympy import symbols, diff, exp, lambdify
from colors import bcolors


def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    T = f(a) + f(b)
    integral = 0.5 * T  # Initialize with endpoints

    for i in range(1, n):
        x_i = a + i * h
        integral += f(x_i)

    integral *= h

    return integral


def trapezoidal_rule_error(f, a, b, n):
    x = symbols('x')
    f_double_prime = diff(diff(f, x), x)  # Compute the second derivative of f
    f_double_prime_lambda = lambdify(x, f_double_prime)  # Convert f_double_prime to a regular Python function
    h = (b - a) / n
    error_bound = (1 / 12) * h ** 2 * (b - a) * f_double_prime_lambda(1)  # Evaluate the second derivative at x=1
    return error_bound


if __name__ == '__main__':
    x = symbols('x')
    f = exp(x ** 2)
    f_lambda = lambdify(x, f)  # Convert f to a regular Python function
    result = trapezoidal_rule(f_lambda, 0, 1, 2)
    error_estimate = trapezoidal_rule_error(f, 0, 1, 2)

    print(bcolors.OKBLUE, "Approximate integral:", result, bcolors.ENDC)
    print(bcolors.OKGREEN, "Error estimation:", error_estimate, bcolors.ENDC)
