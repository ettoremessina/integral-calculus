import sympy as sp

print('Double integral computed by SymPy definite integrate')
print('Example 2-02 definite')
print('Integral of 2xye^-xy from y=1 to x-->+inf and from x=1 to x-->+inf')

x, y = sp.symbols('x y')
f = 2 * x * y * sp.exp(-x * y)
ya = 1.
yb = sp.oo
xa = 1.
xb = sp.oo

integral = sp.integrate(f, (x, xa, xb), (y, ya, yb))
integral = integral.evalf()
print('Result is ', integral)
