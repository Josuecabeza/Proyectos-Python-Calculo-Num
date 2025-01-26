import math

# Definir la función que queremos integrar
def f(x):
    return math.sin(x)  # Ejemplo: función seno

# Método de Trapecio
def metodo_trapecio(f, a, b, n):
    h = (b - a) / n
    suma = (f(a) + f(b)) / 2
    for i in range(1, n):
        suma += f(a + i * h)
    integral_aproximada = h * suma
    return integral_aproximada

# Función exacta de la integral (en este caso, la integral de sin(x) de a a b)
def integral_exacta(a, b):
    return -math.cos(b) + math.cos(a)  # Integral de sin(x) es -cos(x)

# Parámetros de entrada
a = 0  # Límite inferior
b = math.pi  # Límite superior
n = 10  # Número de subdivisiones (puedes cambiar este valor)

# Calcular la integral aproximada y exacta
aproximacion = metodo_trapecio(f, a, b, n)
exacta = integral_exacta(a, b)

# Calcular el error
error = abs(aproximacion - exacta)

# Mostrar resultados con 6 decimales
print(f'Integral aproximada: {aproximacion:.6f}')
print(f'Valor exacto: {exacta:.6f}')
print(f'Error absoluto: {error:.6f}')