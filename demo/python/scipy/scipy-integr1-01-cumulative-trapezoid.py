import scipy.integrate as spi
import numpy as np

print('Single integral computed by SciPy cumulative_trapezoid')
print('Example 1-01 cumulative_trapezoid')
print('Integral of 2xe^-x from x=1 to x=5')

integrand = lambda x : 2 * x * np.exp(-x)
a = 1.
b = 5.
step = 1e-4

xs = np.arange(a, b, step)
ys = integrand(xs)

result = spi.cumulative_trapezoid(ys, xs)
result = result[-1]
print('Result is ', result)
