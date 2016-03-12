# -*- coding: utf-8 -*-
from helper import color
import math
import pdb

def en_una_funcion(x, y, z):
    print color("Ahora estamos dentro de una función.")
    print color("Aplica el conocimiento de pbd para inspeccionar su comportamiento y entender que realiza.")
    print color("\t1. ¿Qué valores tienen las variables x, y, z?.")
    print color("\t2. ¿Qué contiene tiene la variable what?.")
    print color("\t3. ¿Porqué hay un error si se usa 'x*y' en lugar de 'x*int(y)'.")
    pdb.set_trace()
    what1 = x*int(y)
    what2 = chr(z+bool(y))*3 + chr(int(z+math.sqrt(z)+1))
    return what1 + what2

print color("Este es un programa muy sencillo para mostrar las capacidades de pdb")
print color("Los mensajes de ayuda de este ejemplo estarán en verde.")
print color("Realiza las siguientes acciones en orden.")
print color("\t1.- Presiona n+Enter para ejecutar la siguiente accion del programa")
print color("\t2.- Presiona Enter para volver a ejecutar la última accion")
print color("\t3.- Presiona l+Enter para ver en que parte de la ejecución del programa se encuentra")
print color("\t4.- Ingresa 'p a, b, c, d' (sin comillas) para imprimir los valores de a, b, c y d")
print color("\t5.- Presiona c+Enter para continuar con la ejecución normal del programa")
pdb.set_trace()
a = 10
b = 2.0
c = "waka"

print en_una_funcion(c, b, a**2)
