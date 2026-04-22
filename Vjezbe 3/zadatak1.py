import numpy as np
import matplotlib.pyplot as plt
from projectile import Projectile

v0=20.0
theta_deg=45.0
theta=np.radians(theta_deg)

vx0=v0 * np.cos(theta)
vy0=v0 * np.sin(theta)

p= Projectile(
    x0=0.0,
    y0=0.0,
    vx0=vx0,
    vy0=vy0,
    m=1.0,
    k=0.15,
    g=9.81
)

dt_values=[0.5, 0.1, 0.05, 0.01]

plt.figure(figsize=(8, 6))

for dt in dt_values:
    p.plot_trajectory_euler(dt)

plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Eulerova metoda")
plt.legend()
plt.grid()
plt.show()

for dt in dt_values:
    t, x, y, vx, vy = p.simulate_euler(dt)
    print(f"dt={dt:>4}: vrijeme leta={t[-1]:.4f} s, domet={x[-1]:.4f} m")
    