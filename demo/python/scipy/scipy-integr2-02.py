import scipy.integrate as spi
import numpy as np

print('Double integral computed by SciPy nquad')
print('Example 01')
print('Integral of xye^-xy from y=1 to x-->+inf and from x=1 to x-->+inf')

integrand = lambda x, y : 2 * x * y * np.exp(-x * y)
ya = 1.
yb = 5.

result, error = spi.nquad(integrand, [[1, np.inf],[1, np.inf]])
print('Result is ', result, 'with error ', error)
