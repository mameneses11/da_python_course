import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

plt.plot(x, y)
plt.xlabel('X Label')
plt.ylabel('Y label')
plt.title('Title')

plt.subplot(1,2,1)
plt.plot(x,y,'r')
plt.subplot(1,2,2)
plt.plot(y,x,'b')

# OO
fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Title')

fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes1.plot(x,y)
axes1.set_title('Larger plot')

axes2.plot(y,x)
axes2.set_title('Smaller plot')

fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])

fig, axes = plt.subplots(nrows = 1, ncols = 2)

axes[0].plot(x,y)
axes[0].set_title('First Plot')

axes[1].plot(x,y)
axes[1].set_title('Second Plot')

plt.tight_layout()

fig = plt.subplots(nrows = 2, ncols = 1, figsize = (8,2), dpi= 100)

axes[0].plot(x,y)
axes[1].plot(y,x)

plt.tight_layout()

fig = plt.figure()

ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2, label = 'X Squared')
ax.plot(x,x**3, label = 'X Cubed')

ax.legend(loc = 0)

# fig.savefig('my_figure.png', dpi = 200)

fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x,y, color = 'purple', lw = 3, ls = '--', marker = '*', markersize = 10, markerfacecolor = 'yellow', markeredgewidth = 3, markeredgecolor = 'green') # RGB Hex Code
