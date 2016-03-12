def fibonacci(n):
    """
    Debe regresar la lista con los primeros n numeros de fibonacci.
    Para n<1, regresar [].
    Para n=1, regresar [1].
    Para n=2, regresar [1,1].
    Para n=3, regresar [1,1,2].
    Para n=4, regresar [1,1,2,3].
    Y sucesivamente
    """
    a = 1
    b = 1
    fib = [a,b]
    count = 2
    if n<1:
        return []
    if n==1:
        return [1]
    while count < n:
        aux = a
        a = b
        b = aux + b
        count += 1
        fib.append(b)
    return fib

print "fibonacci(-1):", fibonacci(-1) # Deberia ser []
print "fibonacci(0):", fibonacci(0) # Deberia ser []
print "fibonacci(1):", fibonacci(1) # Deberia ser [1]
print "fibonacci(2):", fibonacci(2) # Deberia ser [1,1]
print "fibonacci(3):", fibonacci(3) # Deberia ser [1,1,2]
print "fibonacci(5):", fibonacci(5) # Deberia ser [1,1,2,3,5]
print "fibonacci(10):", fibonacci(10) # Deberia ser ...

"""
ERRORES DETECTADOS:
1) count<=n da uno mas de lo necesario
2) n=1 es asignacion incorrecta. Usar n==1
3) fib.append(aux) es erroneo, queremos agregar b.
"""
