# Bisection method for solving equation f(x) = 0

# Dividing interval by half, and choosing
# next interval based on the sign of the function

from numpy import sign

def f(x):
    return x**3 - x + 1


def bisection(a, b, eps):
    xn = a + (b-a)/2
    count = 0

    while abs(f(xn)) > eps:
        if sign(f(a)) == sign(f(xn)):
            a = xn
        elif sign(f(xn)) == sign(f(b)):
            b = xn
        xn = a + (b-a)/2
        count += 1

    return xn, count


interval_start = -2
interval_end = -1
eps = 1e-3

print(bisection(interval_start, interval_end, eps))

# Output: (root, count of iterations)