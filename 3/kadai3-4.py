
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

plt.style.use('ggplot')
fig, ax = plt.subplots(dpi=150)
ax.set(xlabel="x",ylabel="y")

x = np.arange(-3, 3, 0.01)

step = 1000
b = 2 * step

m = np.inf
mbb = 2

def update(d):
    global b, m, mbb
    plt.cla()
    ax.set_xlim(-3, 3)
    ax.set_ylim(-1, 4.5)
    bb = b/step
    f = bb ** x
    strb = '{:.3f}'.format(bb)
    fp = f * np.log(bb)
    diff = np.max(np.abs(f - fp))
    if diff < m:
        mbb = bb
        m = diff

    ax.plot(x, f, label=r'$' + strb + '^x$', color='r')
    ax.plot(x, fp, label=r'$\frac{d}{dx} ' + strb + '^x$', color='b')
    ax.legend(loc='upper left')

    b += 1
    if b > 4 * step:
        b = 2 * step
        print('optimal_base = {:.3f}'.format(mbb))


ani = animation.FuncAnimation(fig, update, interval=10)
plt.show()
