from particle import Particle
import numpy as np
import matplotlib.pyplot as plt


p=Particle(10, 60)

dt_values = np.linspace(0.001, 0.1, 50)                 # različiti delta t
errors = []

ana = p.analytical_range()

for dt in dt_values:
    num = p.range(dt=dt)
    rel_error = abs(num - ana) / ana
    errors.append(rel_error)

p.plot_trajectory()

plt.plot(dt_values, errors)
plt.xlabel("Δt")
plt.ylabel("Relativna pogreška")
plt.title("Ovisnost pogreške o vremenskom koraku")
plt.grid()
plt.show()