import sympy as sp

print('Single integral computed by SymPy indefinite integrate')
print('Example 1-01 indefinite integrate')
print('Integral of 2xe^-x from x=1 to x=5')

x = sp.Symbol('x')
f = 2 * x * sp.exp(-x)
primitive = sp.integrate(f, x)
print('Primitive is ', primitive)

primitive_lambda = sp.lambdify(x, primitive)
a = 1.
b = 5.
integral = primitive_lambda(b) - primitive_lambda(a)
print('Result is ', integral)
