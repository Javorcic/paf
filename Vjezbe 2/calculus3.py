import numpy as np

def deriv(f, x, metoda="three-step", h=0.00001):
    if metoda=="two-step":
        return (f(x+h) - f(x)) / h
    else: #three-step
        return (f(x+h) - f(x-h)) / (2*h)
    
def deriv_raspon(f, a, b, n=100, metoda="three-step", h=0.00001):
    x_vrij = np.linspace(a, b, n)
    y_vrij=[deriv(f, x, metoda, h) for x in x_vrij]
    return x_vrij, y_vrij