import numpy as np
import matplotlib.pyplot as plt
from calculus3 import deriv_raspon

#kubna lol
f = lambda x: x**3
f_ana = lambda x: 3*x**2

x, y_num = deriv_raspon(f, -2 , 2, metoda="three-step")
y_ana = f_ana(x)

plt.figure()
plt.plot(x, y_num, label="numericki")
plt.plot(x, y_ana, label="analiticki", linestyle="dashed")
plt.title("Derivacija f(x)=x^3")
plt.legend()
plt.grid()
plt.show()
 
 #trig
f2 = lambda x: np.sin(x)
f2_der = lambda x: np.cos(x)

x2, y2_num = deriv_raspon(f2, -2*np.pi , 2*np.pi)
y2_ana = f2_der(x2)

plt.figure()
plt.plot(x2, y2_num, label="numericki")
plt.plot(x2, y2_ana, label="analiticki", linestyle="dashed")
plt.title("Derivacija f(x)=sin(x)")
plt.legend()
plt.grid()  
plt.show()