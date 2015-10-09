from sympy import symbols, Matrix, latex

x1, x2, x3 = symbols('x1 x2 x3')
mu = symbols('mu')

Sigma_11 = Matrix([3])
Sigma_21 = Matrix([[0], [1]])
Sigma_12 = Sigma_21.transpose()
Sigma_22 = Matrix([[1, 1], [1, 2]])

mean = Matrix([[mu], [mu]]) + Sigma_21 * Sigma_11.inv() * (Matrix([x1]) -
                                                           Matrix([mu]))
print latex(mean)

cov = Sigma_22 - Sigma_21 * Sigma_11.inv() * Sigma_12

print latex(cov)
