import sympy as sp

print('Single integral computed by SymPy integrate(f, (x, a, b))')
print('Example 1-01')
print('Integral of 2xe^-x from x=1 to x=5')

x = sp.Symbol('x')
f = 2 * x * sp.exp(-x)
a = 1.
b = 5.
integral = sp.integrate(f, (x, a, b))
print('Result is ', integral)
