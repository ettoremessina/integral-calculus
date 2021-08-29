import sympy as sp

print('Single integral computed by sympy integrate(f, (x, a, b))')
print('Integral of 2xe^-x from 1 to 5')

x = sp.Symbol('x')
f = 2 * x * sp.exp(-x)
a = 1.
b = 5.
integral = sp.integrate(f, (x, a, b))
print('Result is ', integral)
