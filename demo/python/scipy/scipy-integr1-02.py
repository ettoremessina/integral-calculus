import scipy.integrate as spi
import numpy as np

print('Single integral computed by SciPy quad')
print('Example 1-02')
print('Integral of 2xe^-x from x=1 to x-->+inf')

integrand = lambda x : 2 * x * np.exp(-x)
a = 1.
b = np.inf

result, error = spi.quad(integrand, a, b)
print('Result is ', result, 'with error ', error)
