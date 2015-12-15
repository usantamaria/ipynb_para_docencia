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

def metodo_bisecci(f, x0, x1):
    tol = 1E-6 # Numerical tolerance to stop the algoritm
    f2 = 1 # Start with some value
    while np.abs(f2)>tol:
        f0 = f(x0)
        f1 = f(x1)
        x2 = x1 - (x1-x0)/(f1-f0)*f1
        f2 = f(x2)
        x0, x1 = x1, x2
    return x2

x_zero = metodo_secante(mi_funcion, -3, 0)

# Plot (no contiene errores, solo para ayudarlos)
x = np.linspace(-5,5,101)
plt.plot(x, mi_funcion(x), 'b', label="$2^x-x^2$")
plt.plot([-0.766664695851], [0.0], 'ko', label=u"Solución deseada")
plt.plot(x_zero, mi_funcion(x_zero), 'rs', label=u"Solución implementada")
plt.grid('on')
plt.legend(loc="upper left", numpoints=1)
plt.show()
