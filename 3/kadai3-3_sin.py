import numpy as np
import matplotlib.pyplot as plt
import math

t = np.arange(-2*np.pi, 2*np.pi, 0.1)

sint = t.copy()
sign = -1
for n in range(3, 10, 2):
    sint += sign * (t**n) / math.factorial(n)
    sign *= -1

plt.plot(t, sint, label='sin t')
plt.legend(loc='upper left')
plt.grid()
plt.show()
