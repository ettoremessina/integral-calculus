import sympy as sp

print('Single integral computed by SymPy definite integrate')
print('Example 1-01 definite')
print('Integral of 2xe^-x from x=1 to x=5')

x = sp.Symbol('x')
f = 2 * x * sp.exp(-x)
a = 1.
b = 5.
integral = sp.integrate(f, (x, a, b))
integral = integral.evalf()
print('Result is ', integral)
