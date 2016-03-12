# -*- coding: utf-8 -*-
# Desafio 3
# Hallar errores en la implementacion del método de la secante utilizando pdb
"""
Los errores eran:
1) Tolerancia numérica era gigante
2) Se regresaba f2 en vez de x2
3) Formula de la secante estaba escrita al revés.
"""
from matplotlib import pyplot as plt
import numpy as np

def mi_funcion(x):
    return 2**x - x**2

def metodo_biseccion(f, x_left, x_right):
    tol = 1E-6 # Numerical tolerance to stop the algoritm
    f_middle = 1 # Start with some value
    while np.abs(f_middle)>tol:
        f_left = f(x_left)
        f_right = f(x_right)
        x_middle = 0.5 * (x_left + x_right)
        f_middle = f(x_middle)
        print x_left, x_middle, x_right
        if f_left*f_middle > 0:
            x_left = x_middle
        else
            x_right = x_middle
    return x_middle

x_zero = metodo_biseccion(mi_funcion, -3, 0)

# Plot (no contiene errores, solo para ayudarlos)
x = np.linspace(-5,5,101)
plt.plot(x, mi_funcion(x), 'b', label="$2^x-x^2$")
plt.plot([-0.766664695851], [0.0], 'ko', label=u"Solución deseada")
plt.plot(x_zero, mi_funcion(x_zero), 'rs', label=u"Solución implementada")
plt.grid('on')
plt.legend(loc="upper left", numpoints=1)
plt.show()
