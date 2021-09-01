import scipy.integrate as spi
import numpy as np

print('Triple integral computed by SciPy nquad')
print('Example 3-01 nquad')
print('Integral of x + yz^2 from z=1 to z=2, y=z+1 to y=z+2 and from x=y+x to x=2(y+z)')

integrand = lambda x, y, z : x + y * z ** 2

bounds_z = lambda : [1., 2.]
bounds_y = lambda z : [z+1, z+2]
bounds_x = lambda z, y : [y+z, 2 * (y+z)]
ya=lambda z: z + 1
yb=lambda z: z + 2
xa=lambda z, y : y + z
xb=lambda z, y : 2 * (y + z)

result, error = spi.nquad(integrand, [bounds_x, bounds_y, bounds_z])
print('Result is ', result, 'with error ', error)
