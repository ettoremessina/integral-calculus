import scipy.integrate as spi
import autograd.numpy as anp   # Thinly-wrapped version of Numpy
import autograd as ag

print('Compute length of an arc of planar curve by SciPy quad')
print('Example 1-03 quad arclength')
print('Length of arc of curve y=e^(-x^2) from x=-1 to x=1')

y = lambda x : anp.exp(-x**2)
dy_dx = ag.grad(y)
integrand = lambda x : anp.sqrt(1 + dy_dx(x) ** 2)
a = -1.
b = 1.

result, error = spi.quad(integrand, a, b)
print('Result is ', result, 'with error ', error)
