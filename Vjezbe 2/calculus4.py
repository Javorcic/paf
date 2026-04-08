import numpy as np

def derivate(f, x, method="three-step", h=1e-5):
    if method=="two-step":
        return (f(x+h) - f(x)) / h
    else: #three-step
        return (f(x+h) - f(x-h)) / (2*h)
    
def derivate_range(f, a, b, n=100, method="three-step", h=1e-5):
    x_values = np.linspace(a, b, n)
    y_values=[derivate(f, x, method, h) for x in x_values]
    return x_values, y_values

def prav_integ(f, a, b, n):
    dx = (b - a) / n
    x = np.linspace(a, b, n+1)

    lower_sum = 0
    upper_sum = 0

    for i in range(n):
        f1 = f(x[i])
        f2 = f(x[i+1])

        lower_sum += min(f1, f2) * dx
        upper_sum += max(f1, f2) * dx

    return lower_sum, upper_sum


def trap_integ(f, a, b, n):
    dx = (b - a) / n
    x = np.linspace(a, b, n+1)

    total = 0
    for i in range(n):
        total += (f(x[i]) + f(x[i+1])) / 2 * dx

    return total