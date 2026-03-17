import numpy as np
import matplotlib.pyplot as plt

F = float(input("Sila (N): "))
m = float(input("Masa (kg): "))

a = F / m

t = np.linspace(0, 10, 100)

v = a * t
x = 0.5 * a * t**2

plt.figure()
plt.plot(t, x)
plt.xlabel("t (s)")
plt.ylabel("x (m)")
plt.title("x-t graf")

plt.figure()
plt.plot(t, v)
plt.xlabel("t (s)")
plt.ylabel("v (m/s)")
plt.title("v-t graf")

plt.figure()
plt.plot(t, [a]*len(t))
plt.xlabel("t (s)")
plt.ylabel("a (m/s^2)")
plt.title("a-t graf")

plt.show()