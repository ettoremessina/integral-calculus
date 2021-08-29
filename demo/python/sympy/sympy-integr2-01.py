import sympy as sp

print('Double integral computed by SymPy integrate(f, (x, xa(y), xb(y)), (y, ya, yb)')
print('Integral of x y e^-x e^-y from y=0 to y=4 and from x=y-1 to x=y+1')

x, y = sp.symbols('x y')
f = x * y * sp.exp(-x) * sp.exp(-y)
ya = 0.
yb = 4.
xa = y-1
xb = y+1

integral = sp.integrate(f, (x, xa, xb), (y, ya, yb))
integral = integral.evalf()
print('Result is ', integral)
