import numpy as np
import matplotlib.pyplot as plt

def jednoliko_gibanje(F, m):
    a = F / m
    t = np.linspace(0, 10, 100)

    v = a * t
    x = 0.5 * a * t**2

    plt.plot(t, x)
    plt.xlabel("t (s)")
    plt.ylabel("x (m)")
    plt.show()