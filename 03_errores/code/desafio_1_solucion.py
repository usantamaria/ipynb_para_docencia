import numpy
def promedio_positivo(a):
    pos_mean = a[a>0].mean()
    return pos_mean

N = 100
x = numpy.linspace(-1,1,N) # No cambiar esta linea
y = 0.5 - x**2   # No cambiar esta linea
print promedio_positivo(y)

# Error 1: Def -> def
# Error 2: mean -> mean()
# Error 3: numpy
# Error 4: Orden de lineas (N no estaba definido)
# Error 5:
