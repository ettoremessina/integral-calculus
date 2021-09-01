import scipy.integrate as spi
import numpy as np

print('Triple integral computed by SciPy tplquad')
print('Example 3-01 tplquad')
print('Integral of x + yz^2 from z=1 to z=2, y=z+1 to y=z+2 and from x=y+x to x=2(y+z)')

integrand = lambda x, y, z : x + y * z ** 2
za = 1.
zb = 2.
ya=lambda z: z + 1
yb=lambda z: z + 2
xa=lambda z, y : y + z
xb=lambda z, y : 2 * (y + z)

result, error = spi.tplquad(integrand, za, zb, ya, yb, xa, xb)
print('Result is ', result, 'with error ', error)
