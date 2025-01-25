import math

# Función para aplicar el método de bisección
def biseccion(func, a, b, tol=1e-6, max_iter=100):
    # Asegurarse de que la función tenga un cambio de signo en el intervalo [a, b]
    if func(a) * func(b) > 0:
        print("El método no puede aplicarse, no hay cambio de signo en el intervalo dado.")
        return None

    iteracion = 0
    while (b - a) / 2 > tol and iteracion < max_iter:
        c = (a + b) / 2  # Punto medio
        if func(c) == 0:  # Si c es la raíz exacta
            return c
        elif func(a) * func(c) < 0:
            b = c  # La raíz está en el intervalo [a, c]
        else:
            a = c  # La raíz está en el intervalo [c, b]
        iteracion += 1
    
    return (a + b) / 2  # Aproximación de la raíz

# Función para ingresar la función matemática
def obtener_funcion():
    print("Las funciones disponibles son:")
    print("1. x^2 - 4")
    print("2. x^3 - x - 2")
    print("3. x^2 - 2")
    
    opcion = int(input("Elige una función (1, 2 o 3): "))
    
    if opcion == 1:
        return lambda x: x**2 - 4
    elif opcion == 2:
        return lambda x: x**3 - x - 2
    elif opcion == 3:
        return lambda x: x**2 - 2
    else:
        print("Opción no válida.")
        return None

# Ejemplo de uso
if __name__== "__main__":
    func = obtener_funcion()  # Obtener la función
    if func:
        a = float(input("Introduce el valor inicial a: "))
        b = float(input("Introduce el valor inicial b: "))
        raiz = biseccion(func, a, b)
        
        if raiz is not None:
            print(f"La raíz aproximada es: {raiz}")