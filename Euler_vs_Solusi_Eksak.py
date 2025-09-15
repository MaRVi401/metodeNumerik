import numpy as np
import matplotlib.pyplot as plt

# Fungsi turunan
def f(x, y):
    return -2 * y

# Parameter
x0 = 0
y0 = 1
h = 0.1
n = 20

# Metode Euler
x_euler = [x0]
y_euler = [y0]
for i in range(n):
    y_next = y_euler[-1] + h * f(x_euler[-1], y_euler[-1])
    x_next = x_euler[-1] + h
    x_euler.append(x_next)
    y_euler.append(y_next)

# Solusi eksak
x_exact = np.linspace(x0, x0 + n*h, 100)
y_exact = np.exp(-2 * x_exact)

# Plot
plt.plot(x_exact, y_exact, label='Solusi Eksak')
plt.plot(x_euler, y_euler, 'o-', label='Metode Euler')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Metode Numerik: Euler vs Solusi Eksak')
plt.legend()
plt.grid()
plt.show()