import sympy as sp

print('Compute length of an arc of planar curve by SymPy definite integrate')
print('Example 1-05 arclength')
print('Length of arc of curve y=x^2 * e^(-x) from x=-1 to x=1')

x = sp.Symbol('x')
f = x**2 * sp.exp(-x)
dy_dx = sp.diff(f, x)
print('Symbolic derivative is ', dy_dx)
integrand = sp.sqrt(1 + dy_dx ** 2)
a = -1.
b = 1.
integral = sp.integrate(integrand, (x, a, b))
integral = integral.evalf()
print('Result is ', integral)
