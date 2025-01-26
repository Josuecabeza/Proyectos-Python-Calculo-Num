def f(x):
    # Definir la función para la cual se busca la raíz
    return x**3 - x - 2  # Ejemplo de función: f(x) = x^3 - x - 2

def biseccion(a, b, tol, max_iter):
    # Verificar si los valores iniciales son válidos
    if f(a) * f(b) > 0:
        print("Los valores iniciales no son válidos. f(a) y f(b) deben tener signos opuestos.")
        return None
    
    iteracion = 0
    error = float('inf')
    c = a  # Inicialización de c, que será la aproximación de la raíz

    print(f"{'Iteración':<10}{'a':<15}{'b':<15}{'c':<15}{'f(c)':<15}{'Error':<15}")
    
    while error > tol and iteracion < max_iter:
        # Calcular el punto medio
        c = (a + b) / 2
        # Evaluar la función en el punto medio
        fc = f(c)
        
        # Calcular el error relativo basado en la diferencia entre los límites
        error = abs(b - a)
        
        # Mostrar la información de la iteración con 5 decimales
        print(f"{iteracion+1:<10}{a:<15.5f}{b:<15.5f}{c:<15.5f}{fc:<15.5f}{error:<15.5f}")
        
        # Actualizar los límites a y b
        if f(a) * fc < 0:
            b = c
        else:
            a = c
        
        iteracion += 1

    # Mostrar el error final con 5 decimales
    print(f"\nError final: {error:.5f}")
    return c

# Parámetros de entrada
a = 1  # Límite inferior
b = 2  # Límite superior
tol = 1e-6  # Tolerancia para el error
max_iter = 100  # Número máximo de iteraciones

# Llamar a la función de bisección
raiz = biseccion(a, b, tol, max_iter)

if raiz is not None:
    print(f"\nLa raíz aproximada es: {raiz:.5f}")