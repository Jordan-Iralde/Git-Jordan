print("inicio")
import random
NumeroRandom = random.randint(1,50)
NumerosProbados = []

while True:
    try:
        NumeroJugador = int(input("Ingrese un numero para adivinar: "))

        if NumeroJugador == NumeroRandom:
            print("Felicidades, Ganaste")
            NumerosProbados.append(NumeroJugador)
            break
        elif NumeroJugador > NumeroRandom:
            print("Demasiado alto \n")
            NumerosProbados.append(NumeroJugador)
        else:
            print("Demasiado bajo\n")
            NumerosProbados.append(NumeroJugador)
    except ValueError:
        print("error, dato no valido")
print(NumerosProbados)

print("fin")