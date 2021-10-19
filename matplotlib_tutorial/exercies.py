import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 100)
y = x * 2
z = x ** 2

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])

ax.plot(x, y)

# fig.savefig('first_image.png', dpi = 200)

fig = plt.figure()

ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([0.2, 0.5, 0.2, 0.2])

# fig.savefig('second_image.png', dpi = 200)

ax1.plot(x, y)
ax2.plot(x, y)

# fig.savefig('third_image.png', dpi = 200)

fig = plt.figure()

ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([0.2, 0.5, 0.4, 0.4])

# fig.savefig('fourth_image.png', dpi = 200)

ax1.plot(x, z)
ax2.plot(x, y)

ax1.set_xlabel('X')
ax1.set_ylabel('Z')
ax1.set_xlim([0, 100])
ax1.set_ylim([0, 10000])

ax2.set_title('zoom')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_xlim([20, 22])
ax2.set_ylim([30, 50])

# fig.savefig('fifth_image.png', dpi = 200)

fig, axes = plt.subplots(nrows = 1, ncols = 2)

# fig.savefig('sixth_image.png', dpi = 200)

axes[0].plot(x, y, color = 'green', lw = 3, ls = '--')
axes[1].plot(x, z, color = 'red', lw = 5, ls = '-.')

# fig.savefig('seventh_image.png', dpi = 200)

fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize = (15, 2))

axes[0].plot(x, y, color = 'green', lw = 3, ls = '--')
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')

axes[1].plot(x, z, color = 'red', lw = 5, ls = '-.')
axes[1].set_xlabel('X')
axes[1].set_ylabel('Z')

fig.savefig('eighth_image.png', dpi = 200)
