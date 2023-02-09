import numpy as np
import matplotlib.pyplot as plt
import math

t = np.arange(-2*np.pi, 2*np.pi, 0.1)

cost = np.ones_like(t)
sign = -1
for n in range(2, 10, 2):
    cost += sign * (t**n) / math.factorial(n)
    sign *= -1

plt.plot(t, cost, label='cos t')
plt.legend(loc='upper left')
plt.grid()
plt.show()
