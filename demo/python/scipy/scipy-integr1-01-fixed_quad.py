import scipy.integrate as spi
import numpy as np

print('Single integral computed by SciPy fixed_quad')
print('Example 1-01 fixed_quad')
print('Integral of 2xe^-x from x=1 to x=5')

integrand = lambda x : 2 * x * np.exp(-x)
a = 1.
b = 5.

result, none = spi.fixed_quad(integrand, a, b, n=5)
print('Result is ', result)
