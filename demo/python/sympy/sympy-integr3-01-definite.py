import sympy as sp

print('Double integral computed by SymPy definite integrate')
print('Example 2-03 definite')
print('Integral of xye^-xy from y=1 to y=4 and from x=y-1 to x=y+1')

x, y, z = sp.symbols('x y z')
f = x + y * z ** 2
za = 1.
zb = 2.
ya = z + 1
yb = z + 2
xa = y + z
xb = 2 * (y + z)

integral = sp.integrate(f, (x, xa, xb), (y, ya, yb), (z, za, zb))
integral = integral.evalf()
print('Result is ', integral)
