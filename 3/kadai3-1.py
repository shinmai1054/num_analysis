import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)

fx1 = x
fx2 = x ** 2
fx3 = x ** 3

plt.plot(x, fx1, label="1. x")
plt.plot(x, fx2, label="2. x**2")
plt.plot(x, fx3, label="3. x**3")
plt.legend(loc='upper left')
plt.show()
