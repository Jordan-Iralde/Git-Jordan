'''
Es una carrera donde se dan los valores(Tiempo) de cada competidor donde se busca conocer el que tiene
el mejor tiempo, el peor tiempo, tiempos iguales
'''
print("Inicio")

listaAutos = []
listaTiempo = []


while True:
    try:
        cantidad_de_autos = int(input("ingrese la cantidad de competidores que desee: "))
        for i in range(cantidad_de_autos):
            auto = int(input("\nIngrese el numero del auto: "))
            tiempo_de_auto = float(input("Ingrese el tiempo registrado: "))

            listaAutos.append(auto)
            listaTiempo.append(tiempo_de_auto)
            print(max(listaTiempo))
        break
    except ValueError():
        print("no valido")

    
print(listaAutos)
print(listaTiempo)
print("fin")