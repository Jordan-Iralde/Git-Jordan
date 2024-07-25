print("inicio")

def calcularEC():
    masa = float(input("Ingrese la masa: "))
    Velocidad = float(input("Ingrese la Velocidad: "))
    calculo = 0.5 * masa * (Velocidad ** 2)

    return calculo

def calcularEP():
    gravedad = 9.8
    masa = float(input("Ingrese la masa: "))
    altura = float(input("Ingrese la altura: "))
    calculo = masa * gravedad * altura

    return calculo

def calcularEM():
    Ec = calcularEC()
    Ep = calcularEP()
    Em = (Ec + Ep)

    return print(f"La energia mecanica es {Em}")

def calcularH():
    gravedad = 9.8
    Ep = float(input("Ingrese su EP: "))
    masa = float(input("Ingrese la masa: "))
    calculo = Ep / (masa * gravedad)

    return print(f"La Altura es: {calculo}")

def calcularMetroSegundo():
    kilometros = float(input("Ingrese los kilometros: "))
    calculo = kilometros * (1000/3600)

    return print(calculo)


def menu():
    menuInicio = '''
    1- EC
    2- EP
    3- EM
    4- Altura
    5- Metro sobre Segundo
    '''
    return print(menuInicio)
while True:
    try:
        menu()
        eleccion = int(input("Eleccion: "))
        if eleccion == 1:
            print(calcularEC())
        elif eleccion == 2:
            print(calcularEP())
        elif eleccion == 3:
            calcularEM()
        elif eleccion == 4:
            calcularH()
        elif eleccion == 5:
            calcularMetroSegundo()
        else:
            break
    except ValueError():
        print("Error")
print("fin")