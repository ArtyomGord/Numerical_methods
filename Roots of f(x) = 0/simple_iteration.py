# Simple iteration method for solving equation f(x) = 0

# Bring equation to the form x = g(x)
# or use g(x) = x - f(x)/alpha
# Iterative formula: x_n+1 = g(x_n)

from numpy import cbrt

def f(x):
    return x**3 - x + 1

def g1(x):
    return cbrt(x-1)

def g2(x):
    return x - (f(x)) / 6.5


def simple_iter(g, xn, eps):
    count = 0

    while abs(xn - g(xn)) > eps:
        count += 1
        xn = g(xn)
    
    return xn, count


start_point = -2
eps = 1e-3
print(simple_iter(g1, start_point, eps))
print(simple_iter(g2, start_point, eps))

# Output: (root, count of iterations)