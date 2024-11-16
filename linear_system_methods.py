# Simple iteration method and Gauss-Seidel method 
# for system of linear equations Ax = b

# Bring the system to the following form:

# x1 = x2 + x3 + ... + xn + b1
# x2 = x1 + x3 + ... + xn + b2
# ...
# xn = x1 + x2 + ... + xn-1 + bn

from numpy import dot

def check_convergence(matrix):
    norm = 0
    
    for row in matrix:
        temp = 0
        for elem in row:
            temp += abs(elem)
        norm = max(norm, temp)

    if norm >= 1:
        raise Exception(f"These numerical methods does not converge for your matrix, as its norm is larger than 1")

# =====================================================

def simple_iter(matrix, xn, b, eps):
    new_xn = [0 for _ in range(len(xn))]
    flag = True
    
    for i in range(len(xn)):
        new_xn[i] = dot(xn, matrix[i]) + b[i]
        
        if abs(new_xn[i] - xn[i]) > eps:
            flag = False
    
    if flag:
        return new_xn
    return simple_iter(matrix, new_xn, b, eps)


def gauss_seidel(matrix, xn, b, eps):
    new_xn = [0 for _ in range(len(xn))]
    flag = True

    for i in range(len(xn)):
        helper_xn = [new_xn[j] if j < i else xn[j] for j in range(len(xn))]
        new_xn[i] = dot(helper_xn, matrix[i]) + b[i]

        if abs(new_xn[i] - xn[i]) > eps:
            flag = False
            
    if flag:
        return new_xn
    return gauss_seidel(matrix, new_xn, b, eps)

# =====================================================

A = [[0, -0.125, -0.125],
     [-0.2, 0, -0.1],
     [-0.4, -0.4, 0]]

check_convergence(A)
start_vector = [0, 0, 0]
b = [1, -0.7, 1]
eps = 1e-3

print(simple_iter(A, start_vector, b, eps))
print(gauss_seidel(A, start_vector, b, eps))