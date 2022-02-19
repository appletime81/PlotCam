import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

# declare vars
h = 50  # height
N = 10000
beta = np.pi
theta1 = np.linspace(0, np.pi, N)
theta2 = np.linspace(np.pi, 2 * np.pi, N)


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
    x1 = list()
    x2 = list()
    y_all_1th_diff = list()
    y_all_2th_diff = list()

    for angle in theta1:
        y1.append(func1(angle))
        # y2.append(func2(angle))

    for i in range(len(y1)):
        if i > 0:
            y_all_1th_diff.append((y1[i] - y1[i - 1]) / (theta1[i] - theta1[i - 1]))
            x1.append(theta1[i])
        else:
            y_all_1th_diff.append(0)
            x1.append(0)

    for i in range(len(y_all_1th_diff)):
        if i > 0:
            y_all_2th_diff.append((y_all_1th_diff[i] - y_all_1th_diff[i - 1]) / (x1[i] - x1[i - 1]))
            x2.append(x1[i])
        else:
            y_all_2th_diff.append(0)
            x2.append(0)

    print(len(y_all_2th_diff))

    plt.plot(x2, y_all_2th_diff)
    # plt.title(r'height = 50mm, $\beta$ = 180$^\circ$')
    # plt.xlabel(r'$\theta$')
    plt.grid()
    # plt.ylabel('mm')
    plt.show()
