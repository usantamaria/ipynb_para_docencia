# -*- coding: utf-8 -*-
# Desafio 4
# Hallar errores en la implementacion del método de biseccion utilizando IPython.embed
from matplotlib import pyplot as plt
import numpy as np

def mi_funcion(x):
    return 2**x - x**2

def metodo_biseccion(f, x_left, x_right):
    tol = 1E-6 # Numerical tolerance to stop the algoritm
    f_middle = 1 # Start with some value
    n_steps = 0
    while np.abs(f_middle)>tol:
        f_left = f(x_left)
        f_right = f(x_right)
        x_middle = 0.5 * (x_left - x_right)
        f_middle = f(x_middle)
        if f_left*f_middle > 0:
            x_left = f_middle
        else:
            x_right = f_middle
        n_steps -= 1
    print "Metodo de biseccion tomó %d pasos" %n_steps
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
