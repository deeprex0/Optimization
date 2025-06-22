## reel polynomiale functions ax2 +bx +c
import numpy as np
import matplotlib.pyplot as plt

a = float(input("write a coef: "))
b = float(input("write b coef: "))
c = float(input("write c coef: "))


learningRate = 0.1


xValues = []
xImages = []

x = 0
for i in range(20):
    gradientF = (2 * a * x + b)  
    x = x - learningRate * gradientF
    fx = a * x * x + b * x + c
    xValues.append(round(x,4))
    xImages.append(round(fx,4))




for i in range(19):
  print(f"x{i} = {xValues[i]} --> fx{i} = {xImages[i]}")



    







