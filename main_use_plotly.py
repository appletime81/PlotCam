import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

# declare vars
h = 50  # height
N = 10000
beta = np.pi
theta1 = np.linspace(0, np.pi, N)
theta2 = np.linspace(np.pi, 2 * np.pi, N)
r = 200


def func1(angle):
    fixed_var = (h / (4 + np.pi))
    if 0 <= angle <= (1 / 8) * beta:
        return fixed_var * \
               (np.pi * angle / beta - 0.25 * np.sin(4 * np.pi * angle / beta))
    elif (1 / 8) * beta < angle <= (7 / 8) * beta:
        return fixed_var * \
               (2 + np.pi * angle / beta - 9 * np.sin(4 * np.pi * angle / (3 * beta) + np.pi / 3) / 4)
    elif (7 / 8) * beta < angle <= beta:
        return fixed_var * \
               (4 + np.pi * angle / beta - np.sin(4 * np.pi * angle / beta) / 4)


def func2(angle):
    fixed_var = (h / (4 + np.pi))
    if 0 <= angle <= (1 / 8) * beta:
        return h - fixed_var * \
               (np.pi * angle / beta - 0.25 * np.sin(4 * np.pi * angle / beta))
    elif (1 / 8) * beta < angle <= (7 / 8) * beta:
        return h - fixed_var * \
               (2 + np.pi * angle / beta - 9 * np.sin(4 * np.pi * angle / (3 * beta) + np.pi / 3) / 4)
    elif (7 / 8) * beta < angle <= beta:
        return h - fixed_var * \
               (4 + np.pi * angle / beta - np.sin(4 * np.pi * angle / beta) / 4)


if __name__ == '__main__':
    y1 = list()
    y2 = list()
    x = list()
    theta_all = np.concatenate((theta1, theta2))
    for angle in theta1:
        y1.append(r * np.sin(angle) + func1(angle))
        y2.append(r * np.sin(angle) + func2(angle))

    y_all = y1 + y2

    for angle in y_all:
        x.append(r * np.cos(angle))

    plt.plot(x, y_all)
    plt.title(r'height = 50mm, $\beta$ = 180$^\circ$')
    plt.xlabel(r'$\theta$')
    plt.grid()
    plt.ylabel('mm')
    plt.show()
