# Newton method and secant method for solving equation f(x) = 0

# Start point x0 must satisfy following condition:
# f(x0) * f"(x0) > 0

def f(x):
    return x**3 - 2*x - 3

def df(x):
    return 3*(x**2) - 2

def newton_formula(x):
    return x - (f(x) / df(x))

def secant_formula(x0, x1):
    return x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))

# =====================================================

def newton_method(f, xn, eps):
    count = 0

    while abs(f(xn)) > eps:
        xn = newton_formula(xn)
        count += 1
    
    return xn, count


def secant_method(f, x0, eps):
    count = 0
    x1 = x0 - eps

    while abs(f(x1)) > eps:
        temp = secant_formula(x0, x1)
        x0 = x1
        x1 = temp
        count += 1

    return x1, count

# =====================================================

func = f
start_point = 2
eps = 1e-3
print(newton_method(func, start_point, eps))
print(secant_method(func, start_point, eps))

# Output: (root, count of iterations)