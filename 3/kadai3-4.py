
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

plt.style.use('ggplot')
fig, ax = plt.subplots(dpi=150)
ax.set(xlabel="x",ylabel="y")

x = np.arange(-3, 3, 0.01)

step = 400
b = 2 * step

def update(d):
    global b
    plt.cla()
    ax.set_xlim(-3, 3)
    ax.set_ylim(-1, 4.5)
    bb = b/step
    f = bb ** x
    strb = '{:.4f}'.format(bb)
    ax.plot(x, f, label=r'$' + strb + '^x$', color='r')
    ax.plot(x, f * np.log(bb), label=r'$\frac{d}{dx} ' + strb + '^x$', color='b')
    ax.legend(loc='upper left')

    b += 1
    if b >= 3 * step:
        b = 2 * step


ani = animation.FuncAnimation(fig, update, interval=10)
plt.show()
