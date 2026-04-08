import numpy as np
import matplotlib.pyplot as plt
from calculus4 import prav_integ, trap_integ

#kub
f = lambda x: x**3
a, b = -2, 2

ana = (b**4)/4 - (a**4)/4

n_vals = [5, 10, 20, 50, 100, 200, 500]

lower_vals = []
upper_vals = []
trap_vals = []

for n in n_vals:
    lower, upper = prav_integ(f, a, b, n)
    trap = trap_integ(f, a, b, n)

    lower_vals.append(lower)
    upper_vals.append(upper)
    trap_vals.append(trap)

plt.figure()
plt.plot(n_vals, lower_vals, label="donja suma")
plt.plot(n_vals, upper_vals, label="gornja suma")
plt.plot(n_vals, trap_vals, label="trapezna metoda")
plt.axhline(ana, linestyle="dashed", label="analiticko")

plt.title("Integral f(x)=x^3")
plt.xlabel("broj podjela")
plt.ylabel("vrijednost integrala")
plt.legend()
plt.grid()
plt.show()


# trig
f2 = lambda x: np.sin(x)
a2, b2 = 0, 2*np.pi

analytic2 = -np.cos(b2) + np.cos(a2)

lower_vals = []
upper_vals = []
trap_vals = []

for n in n_vals:
    lower, upper = prav_integ(f2, a2, b2, n)
    trap = trap_integ(f2, a2, b2, n)

    lower_vals.append(lower)
    upper_vals.append(upper)
    trap_vals.append(trap)

plt.figure()
plt.plot(n_vals, lower_vals, label="donja suma")
plt.plot(n_vals, upper_vals, label="gornja suma")
plt.plot(n_vals, trap_vals, label="trapezna metoda")
plt.axhline(analytic2, linestyle="dashed", label="analiticko")

plt.title("Integral f(x)=sin(x)")
plt.xlabel("broj podjela")
plt.ylabel("vrijednost integrala")
plt.legend()
plt.grid()
plt.show()