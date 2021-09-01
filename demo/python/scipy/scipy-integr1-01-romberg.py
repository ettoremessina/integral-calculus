import scipy.integrate as spi
import numpy as np

print('Single integral computed by SciPy romberg')
print('Example 1-01 romberg')
print('Integral of 2xe^-x from x=1 to x=5')

integrand = lambda x : 2 * x * np.exp(-x)
a = 1.
b = 5.

result = spi.romberg(integrand, a, b)
print('Result is ', result)
