import math

# Definir la ecuación diferencial
def f(t, y):
    return -2 * y

# Método de Euler para resolver la ODE
def euler_method(f, y0, t0, tf, h):
    t_values = []
    y_values = []
    
    t = t0
    y = y0
    
    # Guardar los valores iniciales
    t_values.append(t)
    y_values.append(y)
    
    # Iteraciones del método de Euler
    while t < tf:
        y = y + h * f(t, y)  # Fórmula de Euler
        t = t + h  # Incrementar t por el paso h
        
        # Guardar el valor en las listas
        t_values.append(t)
        y_values.append(y)
    
    return t_values, y_values

# Parámetros
y0 = 1  # Condición inicial
t0 = 0  # Tiempo inicial
tf = 5  # Tiempo final
h = 0.1  # Paso de tiempo

# Resolver la ecuación con el método de Euler
t_values, y_approx = euler_method(f, y0, t0, tf, h)

# Solución exacta para comparar
y_exact = [math.exp(-2 * t) for t in t_values]

# Calcular el error relativo
error = [abs(ye - ya) / ye if ye != 0 else 0 for ye, ya in zip(y_exact, y_approx)]

# Mostrar resultados
for i in range(len(t_values)):
    print(f"Iteración {i}: t = {t_values[i]:.2f}, Aproximación = {y_approx[i]:.4f}, Exacta = {y_exact[i]:.4f}, Error = {error[i]:.4f}")