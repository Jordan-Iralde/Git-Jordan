print("inicio")

'''
Act: Realiza un programa en python donde el usuario pueda elegir en un menu el calculo del area de una
figura correspondiente a una figura geometrica definida en una funcion, cada figura (opcion) debe estar
desarrollada en una funcion.
'''
feleccion=0
def menu():
    print('''
    ************************************************
    *    Ingrese 1 para calcular el triangulo      *
    *    Ingrese 2 para calcular el rectangulo     *   
    *    Ingrese 3 para calcular el circulo        *
    *    ingrese 4 para salir del programa         *
    ************************************************
    Deja que los grandes programen
                                mateo - 2023
    ''')

menu()
def triangulo():
    base = int(input("Ingrese el valor de la base "))
    altura = int(input("Ingrese el valor de la altura "))
    areatri= (base * altura) / 2
    print(f" su rectangulo tiene un area de: {areatri}")

def rectangulo():
    base = int(input("Ingrese el valor de la base "))
    altura = int(input("Ingrese el valor de la altura "))
    arearectangulo= base * altura
    print(f" su rectangulo tiene un area de: {arearectangulo}")

def radio():
    radio= float(input("ingrese el valor del radio de su circulo "))
    multiplor= radio*radio
    calculo0= multiplor * 3.1416
    print(f"el area de su circunferencia es: {calculo0}")

while True:
    try: 
        feleccion=int(input("Ingrese..."))

        if feleccion == 0 or feleccion >= 5:
            print("por favor ingrese un numero en el rango que le pedimos")
        
        elif feleccion == 1:
            print(f"[{feleccion}], Area de Triangulo")
            triangulo()
            
        elif feleccion == 2:
            print(f"[{feleccion}], Area de Rectangulo")
            rectangulo()
            
        elif feleccion == 3:
            print(f"[{feleccion}], Area de circulo")
            radio()

        else:
            print(f"[{feleccion}], Saliendo del programa...")
            break



    except ValueError:
        print("el dato ingresado es incorrecto, por favor ingrese un dato entero")
        menu()

print("fin")