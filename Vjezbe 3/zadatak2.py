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
dt=0.01

t_e, x_e, y_e, vx_e, vy_e = p.simulate_euler(dt)
t_r, x_r, y_r, vx_r, vy_r = p.simulate_rk4(dt)

plt.figure(figsize=(8, 6))
plt.plot(x_e, y_e, label="Eulerova metoda", linestyle='--')
plt.plot(x_r, y_r, label="RK4", linestyle='-')
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("usporedba Eulerove metode i RK4")
plt.legend()
plt.grid()
plt.show()

print("eul ")
print(f" domet= x_e[-1]:.6f m")
print(f" vrijeme leta={t_e[-1]:.6f} s")

print("rk4 ")
print(f" domet={x_r[-1]:.6f} m")
print(f" vrijeme leta={t_r[-1]:.6f} s")
