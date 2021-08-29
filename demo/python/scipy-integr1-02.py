import scipy.integrate as spi
import numpy as np

print('Single integral computed by scipy quad')
print('Example 02')
print('Integral of 2xe^-x from 1 to +inf')

integrand = lambda x : 2 * x * np.exp(-x)
a = 1.
b = np.inf

result, error = spi.quad(integrand, a, b)
print('Result is ', result, 'with error ', error)
