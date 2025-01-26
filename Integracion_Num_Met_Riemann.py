def metodo_riemann(f, a, b, n):
    """
    Método de Riemann para la integración numérica.

    f: función a integrar
    a: límite inferior
    b: límite superior
    n: número de subintervalos
    """
    # Paso 1: calcular el ancho de cada subintervalo
    h = (b - a) / n
    
    # Paso 2: aproximación de la integral (usando sumas de Riemann con puntos izquierdos)
    suma = 0
    for i in range(n):
        suma += f(a + i * h)
    
    integral_aprox = h * suma
    
    return integral_aprox

def error_analitico(f, a, b, integral_exacta, n):
    """
    Calcula el error relativo en la aproximación numérica de la integral.
    
    f: función a integrar
    a: límite inferior
    b: límite superior
    integral_exacta: valor exacto de la integral (si lo sabemos)
    n: número de subintervalos
    """
    integral_aprox = metodo_riemann(f, a, b, n)
    error = abs(integral_exacta - integral_aprox)
    return round(error, 6)

# Ejemplo: función a integrar
def f(x):
    return x**2  # Ejemplo de función f(x) = x^2

# Límite inferior y superior
a = 0
b = 1

# Valor exacto de la integral (para x^2 en [0,1], es 1/3)
integral_exacta = 1/3

# Número de subintervalos
n = 1000

# Calcular la aproximación e imprimir el resultado y el error
integral_aprox = metodo_riemann(f, a, b, n)
error = error_analitico(f, a, b, integral_exacta, n)

print(f"Aproximación de la integral: {integral_aprox:.6f}")
print(f"Error relativo: {error:.6f}")