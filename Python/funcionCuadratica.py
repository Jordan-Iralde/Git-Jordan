import math

def Menu():
    menuInicio = '''
    #################################################
    #                                               #
    #    1- Ingresar Funcion                        #
    #    2- Calcular vertices                       #
    #    3- Calcular Raices                         #
    #                                               #
    #################################################
    '''
    return print(menuInicio)

def FuncionCuadratica():

    print("Desea ingresar valores? ingrese 1")
    ingresarValores=int(input("ingrese valores: "))
    if ingresarValores == 1:
        a= int(input("ingrese los valores para su funcion(a): "))
        b= int(input("ingrese los valores para su funcion(b): "))
        c= int(input("ingrese los valores para su funcion(c): "))
    else:
        funcionCuadratica1 = ax + bx + c
        FuncionCuadratica2 = ax + bx - c
        funcionCuadratica3 = ax - bx - c
        funcionCuadratica4 = ax - bx + c

        funcionCuadratica1 = ax + bx + c
        FuncionCuadratica2 = ax + bx - c
        funcionCuadratica3 = ax - bx - c
        funcionCuadratica4 = ax - bx + c
        #por ejemplo (-(x+2)(x-6))/4 = -ax**2 + bx + c
        #-(ax**2) = -1/4
        #bx     = 4/4
        #c      =12/4
        for i in range(3):  
            print
    return a, b, c


def calcularVertices():
    tuplas=FuncionCuadratica()
    (a, b , c) = tuplas
    
    x= -(b)/(2*a)

    ax2 = (a*(x**2))
    bx= b*x
    y= ax2+bx+c
    return print(f"Xv={x}; Yv={y}")



def CalcularRaices():
    tuplasR=FuncionCuadratica()
    (a, b , c) = tuplasR

    print(
        a,
        b,
        c
    )

    '''
    (-b ± √ (b**2 -((4 * a) * c) )) / 2*a
    '''
    raices1 = (-b + math.sqrt((b**2) - ((4 * a) * c)))/ (2 * a)
    raices2 = (-b - math.sqrt((b**2) - ((4 * a) * c)))/ (2 * a)
    #una funcion con la solucion de la raiz > 0,  => tiene 2 raices
    #una funcion con la solucion de la raiz = 0,  => tiene 1 raiz
    #una funcion con la solucion de la raiz < 0,  => no tiene raiz, es numero imaginario
    return print(raices1, raices2)

#tuplas
while True:
    try:
        Menu()
        eleccion = int(input("Ingrese su eleccion: "))
        if eleccion == 1:
            FuncionCuadratica()
        elif eleccion == 2:
            calcularVertices()
        elif eleccion == 3:
            CalcularRaices() #Si no tiene raices, le faltan los numeros imaginarios
    except ValueError():
        print("Error")
