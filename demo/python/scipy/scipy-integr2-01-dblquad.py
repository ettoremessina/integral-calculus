import scipy.integrate as spi
import numpy as np

print('Double integral computed by SciPy dblquad')
print('Example 2-01 dblquad')
print('Integral of 2xye^-xy from y=1 to y=5 and from x=y-1 to x=y+1')

integrand = lambda x, y : 2 * x * y * np.exp(-x * y)
ya = 1.
yb = 5.

result, error = spi.dblquad(integrand, ya, yb, lambda y: y-1, lambda y: y+1)
print('Result is ', result, 'with error ', error)
