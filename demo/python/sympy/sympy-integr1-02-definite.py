import sympy as sp

print('Single integral computed by SymPy definite integrate')
print('Example 1-02 definite')
print('Integral of 2xe^-x from x=1 to x-->+inf')

x = sp.Symbol('x')
f = 2 * x * sp.exp(-x)
a = 1.
b = sp.oo
integral = sp.integrate(f, (x, a, b))
integral = integral.evalf()
print('Numeric result is ', integral)
