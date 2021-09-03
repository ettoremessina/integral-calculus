import scipy.integrate as spi
import autograd.numpy as anp   # Thinly-wrapped version of Numpy
import autograd as ag

print('Compute length of an arc of planar parametric curve by SciPy quad')
print('Example 1-04 quad arclength')
print('Length of arc of parametric curve x(t)=cos^3(t) and y(t)=sin^3(t) from x=0 to x=2pi')

x = lambda t : anp.cos(t) ** 3
y = lambda t : anp.sin(t) ** 3
dx_dt = ag.grad(x)
dy_dt = ag.grad(y)

integrand = lambda t : anp.sqrt(dx_dt(t) ** 2 + dy_dt(t) ** 2)
a = 0.
b = 2 * anp.pi

result, error = spi.quad(integrand, a, b)
print('Result is ', result, 'with error ', error)
