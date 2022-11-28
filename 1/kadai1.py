import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 4, 0.001)

x1 = np.sin(np.pi * t)
x2 = np.cos(2 * t + np.pi / 2)
x3 = 1 - np.sin(t)
x4 = np.cos(np.pi * t)
x5 = np.sin(2 * t + np.pi / 2)

plt.plot(t, x1, label="1. sin(pi * t)")
plt.plot(t, x2, label="2. cos(2t + pi/2)")
plt.plot(t, x3, label="3. 1 - sin(t)")
plt.plot(t, x4, label="4. cos(pi * t)")
plt.plot(t, x5, label="5. sin(2t + pi/2)")
plt.legend(loc='upper left')
plt.show()
