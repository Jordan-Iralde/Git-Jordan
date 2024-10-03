N = 1
prev_euler = 0
tolerance = 1e-100  # Puedes ajustar la tolerancia según la precisión que desees

while True:
    Euler = (1 + 1/N)**N
    
    # Comparar la diferencia entre la aproximación actual y la anterior
    if abs(Euler - prev_euler) < tolerance:
        break
    
    prev_euler = Euler
    N += 1

print("El número Euler aproximado es:", Euler)
print("Calculado en N =", N)
