import numpy as np
import matplotlib.pyplot as plt

r = 200
theta = np.linspace(0, 2 * np.pi, 100000)
x = r * np.cos(theta)
y = r * np.sin(theta)
plt.plot(x, y)
plt.xlim(-200, 200)
plt.ylim(-200, 200)
plt.gca().set_aspect('equal')
plt.grid()
plt.show()