'''
Problema: Encuentra la suma de todos los números enteros entre 1 y 100 que sean divisibles por 3 o por 5.
'''
print("Inicio")
divisiblesPorTres = []
divisiblesPorCinco = []

i = 0
while True:
    i = i + 1
    if i % 3 == 0:
        divisiblesPorTres.append(i)
    if i % 5 == 0:
        divisiblesPorCinco.append(i)
    if i > 100:
        break

Total = sum(divisiblesPorTres) + sum(divisiblesPorCinco)
print(Total)

print("Fin")