import matplotlib.pyplot as plt
import numpy as np

def pravac(x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    l = y1 - k * x1
    return k, l

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

k, l = pravac(x1, y1, x2, y2)

x = np.linspace(-10, 10, 100)
y = k * x + l

plt.plot(x, y, label="pravac")
plt.scatter([x1, x2], [y1, y2], color='red')

plt.xlabel("x")
plt.ylabel("y")
plt.legend()

izbor = input("Prikaži (p) ili spremi (s)? ")

if izbor == "p":
    plt.show()
else:
    ime = input("Ime datoteke: ")
    plt.savefig(ime + ".pdf")