## reel polynomiale functions ax2 +bx +c

import numpy as np
import matplotlib.pyplot as plt

a = float(input("write a coef: "))
b = float(input("write b coef: "))
c = float(input("write c coef: "))


learningRate = 0.1

def F(X):
    return (a*X**2 + b*X + c)
X = np.linspace(-10,10,400)
Y = F(X)

x = 0
xs = []
fxs = []
for i in range(30):
    gradientF = (2 * a * x + b)  
    x = x - learningRate * gradientF
    fx = a *x**2 + b * x + c
    xs.append(x)
    fxs.append(fx)

xlim1 = xs[29] - 0.5
xlim2 = xs[29] + 0.5
ylim1 = fxs[29] - 0.5
ylim2 = fxs[29] + 0.5

plt.subplot(1,2,1)
plt.plot(range(30), xs, marker='*')
plt.title('x value over iterations')
plt.xlabel('Iteration')
plt.ylabel('x')

plt.subplot(1,2,2)
plt.plot(X,Y, label='f(x)')
plt.plot(xs, fxs, marker='o', linestyle='--', color='red', label='Descent path')
plt.xlim(xlim1, xlim2)  # Zoom in on x-axis
plt.ylim(ylim1, ylim2)  # Zoom in on y-axis (adjust as needed)
plt.title('Function and Descent Path')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()























