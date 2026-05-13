import numpy as np
import matplotlib.pyplot as plt

M = np.array([0.052, 0.124, 0.168, 0.236, 0.284, 0.336])
phi = np.array([0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472])

n = len(M)
a = np.sum(phi * M) / np.sum(phi ** 2)
sigma_a = np.sqrt((1 / n) * (np.sum(M ** 2) / np.sum(phi ** 2) - a ** 2))

print("Dt =", a, "Nm/rad")
print("sigma_Dt =", sigma_a, "Nm/rad")

phi_fit = np.linspace(0, max(phi) * 1.05, 200)
M_fit = a * phi_fit

plt.figure()
plt.scatter(phi, M, color="blue", label="Podaci")
plt.plot(phi_fit, M_fit, color="red", label="Pravac: Dt = " + str(round(a, 4)) + " Nm/rad")
plt.xlabel("phi (rad)")
plt.ylabel("M (Nm)")
plt.title("Linearna regresija: M = Dt * phi")
plt.legend()
plt.tight_layout()
plt.savefig("linregress.png", dpi=150)
plt.show()