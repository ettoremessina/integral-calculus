import sympy as sp

print('Single integral computed by SymPy indefinite integral')
print('Example 1-01 indefinite integral')
print('Integral of 2xe^-x from x=1 to x=5')

x = sp.Symbol('x')
f = 2 * x * sp.exp(-x)
integral = sp.Integral(f, x)
primitive = integral.doit()
print('Primitive is ', primitive)

primitive_lambda = sp.lambdify(x, primitive)
a = 1.
b = 5.
integral = primitive_lambda(b) - primitive_lambda(a)
print('Result is ', integral)
