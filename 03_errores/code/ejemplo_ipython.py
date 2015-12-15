# -*- coding: utf-8 -*-
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

from IPython import embed

from helper import color

def get_surface_data():
    Y = np.arange(-5, 5, 0.25)
    X = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    print color("Estamos en la función: get_surface_data()")
    print color("\tExplora que variables existe (%who) y cambia sus valores")
    print color("\tPara salir de IPython utiliza Ctr-D.")
    embed()
    Z[R>3.0] = 0
    return X, Y, Z

def get_points():
    N = 10
    x = -5 + 10*np.random.rand(N)
    y = -5 + 10*np.random.rand(N)
    z = 1 + np.random.rand(N)
    print color("Estamos en la función: get_points()")
    print color("\tExplora los valores de las variables (%whos)")
    print color("\tPara salir de IPython utiliza Ctr-D.")
    embed()
    return x, y, z

def plot_surface_data(X,Y,Z):
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, alpha=0.5, cmap=cm.coolwarm)
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surf, shrink=0.5, aspect=5)
    print color("Estamos en la función: plot_surface_data()")
    print color("\t¿Todavía existe la variable R? ¿Que le pasó?")
    print color("\tPara salir de IPython utiliza Ctr-D.")
    embed()
    return

def plot_points(x,y,z):
    ax.scatter(x, y, z, s=40)
    ax.set_ylabel("eje y")
    print color("Estamos en la función: plot_points()")
    print color("\t¿Que pasó con X, Y y Z? ¿Porque las variables están en minúsculas?")
    print color("\tPara salir de IPython utiliza Ctr-D.")
    embed()
    return

# Helping mat281 students
print color("Este es un programa muy sencillo para mostrar las capacidades de IPython.embed")
print color("Los mensajes de ayuda de este ejemplo estarán en verde.")
print color("Para salir de IPython utiliza Ctr-D.")
print color("El programa continuará su ejecución normalmente.")
print color("")

# Get the data
X,Y,Z = get_surface_data()
x,y,z = get_points()

print color("Estamos en el contexto principal (fuera de toda función)")
print color("\tExplora que variables existe (%who) y cambia sus valores")
print color("\tPara salir de IPython utiliza Ctr-D.")
embed()

# Do the plots
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plot_surface_data(X,Y,Z)
plot_points(x,y,z)
plt.show()
