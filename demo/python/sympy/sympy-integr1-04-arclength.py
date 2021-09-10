import sympy as sp

print('ompute length of an arc of planar curve by SymPy definite integrate')
print('Example 1-04 arclength')
print('Length of arc of parametric curve x(t)=cos^3(t) and y(t)=sin^3(t) from t=0 to t=2pi')

t = sp.Symbol('t')
x = sp.cos(t) ** 3
y = sp.sin(t) ** 3
dx_dt = sp.diff(x, t)
dy_dt = sp.diff(y, t)
print('Symbolic derivative of x(t) is ', dx_dt)
print('Symbolic derivative of y(t) is ', dy_dt)

integrand = sp.sqrt(dx_dt**2 + dy_dt ** 2)
a = 0.
b = 2 * sp.pi
integral = sp.integrate(integrand, (t, a, b))
integral = integral.evalf()
print('Result is ', integral)
