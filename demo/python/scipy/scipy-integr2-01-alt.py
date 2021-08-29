import scipy.integrate as spi
import numpy as np

print('Double integral computed by scipy nquad')
print('Alternative Example 01')
print('Integral of xye^-xy from y=1 to y=5 and from x=y-1 to x=y+1')

integrand = lambda x, y : 2 * x * y * np.exp(-x * y)

bounds_y = lambda : [1., 5.]
bounds_x = lambda y : [y-1, y+1]

result, error = spi.nquad(integrand, [bounds_x, bounds_y])
print('Result is ', result, 'with error ', error)
