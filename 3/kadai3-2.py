import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-1, 5, 0.01)

fx1 = 1 ** x
fx2 = 2 ** x
fx3 = 3 ** x

plt.plot(x, fx1, label="1. 1**x")
plt.plot(x, fx2, label="2. 2**x")
plt.plot(x, fx3, label="3. 3**x")
plt.legend(loc='upper left')
plt.grid()
plt.show()
