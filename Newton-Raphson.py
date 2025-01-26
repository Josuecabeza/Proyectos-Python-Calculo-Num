# Definir la función y su derivada
def funcion(x):
    return x**3 - x - 2  # Ejemplo de función

def derivada(x):
    return 3*x**2 - 1  # Derivada de la función

# Método de Newton-Raphson
def newton_raphson(func, dfunc, x0, tol=1e-5, max_iter=100):
    # Inicializar la iteración
    x_n = x0
    iteracion = 0

    print(f"{'Iteración':<10}{'x_n':<15}{'f(x_n)':<15}{'f\'(x_n)':<15}{'Error':<15}")
    while iteracion < max_iter:
        # Evaluar la función y su derivada
        fx_n = func(x_n)
        dfx_n = dfunc(x_n)

        # Evitar división por cero
        if dfx_n == 0:
            print("Error: Derivada cero, no se puede continuar.")
            break

        # Método de Newton-Raphson
        x_next = x_n - fx_n / dfx_n
        error = abs(x_next - x_n)

        # Mostrar la iteración
        print(f"{iteracion:<10}{x_n:<15.5f}{fx_n:<15.5f}{dfx_n:<15.5f}{error:<15.5f}")

        # Si el error es menor que la tolerancia, salir
        if error < tol:
            print(f"\nLa raíz aproximada es: {x_next:.5f}")
            print(f"Se alcanzó la convergencia en {iteracion + 1} iteraciones.")
            break

        # Actualizar para la siguiente iteración
        x_n = x_next
        iteracion += 1
    else:
        print("\nNo se alcanzó la convergencia en el número máximo de iteraciones.")

# Definir el valor inicial (x0) para el método
x0 = 1.5

# Llamar al método de Newton-Raphson
newton_raphson(funcion, derivada, x0)