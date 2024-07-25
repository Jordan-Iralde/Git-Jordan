print("Inicio")

voltaje = int(input("Ingrese Volaje: "))
resistencias = []
resistenciasParalelos = []

CantidadResistencias = int(input("Ingrese la cantidad de resistencias que se encuentran: "))
while True:
    i = 0

    serieParalelo = input("Su resistencia es en serie o paralelo: ")
    if serieParalelo == 'serie':
        resistencia = int(input(f"Resistencia {i+1}: \n"))
        resistencias.append(resistencia)
    elif serieParalelo == 'paralelo':
        CuantasResistenciasP = int(input("Cuantas resistencias en paralelo"))
        for j in range(CuantasResistenciasP):
            resistencia = int(input(f"Resistencia {j+1}: \n"))
            calculoResistenciaparalelo = 
    else:
        print("mal ingresado")
        exit()



resistenciaTotal = sum(resistencias)

print("Resistencia Total: ", resistenciaTotal)

'''
ntensidadTotal = voltaje / calcularResistenciaTotal

print("Intensidad Total: ", intensidadTotal)

voltaje1 = intensidadTotal * resistencia1
voltaje23 = intensidadTotal * resistencia23
voltaje4 = intensidadTotal * resistencia4

print(f"Voltaje 1: {voltaje1}, Voltaje 2: {voltaje23}, Voltaje 3: {voltaje23}, Voltaje 4: {voltaje4}")

intensidad1 = voltaje1 / resistencia1
intensidad2 = voltaje23 / resistencia2
intensidad3 = voltaje23 / resistencia3
intensidad4 = voltaje4 / resistencia4

print(f"Intensidad 1: {intensidad1}, Intensidad 2: {intensidad2}, Intensidad 3: {intensidad3}, Intensidad 4: {intensidad4}")
'''

print("Fin")