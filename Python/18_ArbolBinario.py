
print("Inicio")

NumerosDeArbol = [2,1,5,6,10,9,15]

#si fuera 1 pasaria de menos a mas

'''         Asi se tendria que ver
                6                       Raiz
        2/          \10                 Ramas
    1/      5     9/    \15             Hojas
'''


ramaIzquierda = []
ramaDerecha = []
raiz = NumerosDeArbol[3]

def RamasIzq(i):
    ramaIzquierda.append(i)
    print("----------------IZQUIERDA------------")
    print(NumerosDeArbol)
    print("el Indic es: ",i)
    print("---------------------------")

def RamasDer(i):
    ramaDerecha.append(i)
    print("----------------DERECHA------------")
    print(NumerosDeArbol)
    print("el Indic es: ",i)
    print("---------------------------")


def ArbolBi():
    i = 1
    rama = raiz     #6
    for i in NumerosDeArbol:
        print(NumerosDeArbol)
        print("raiz es: ",rama)
        print("el indice es: ",i)

        if rama > i:        #si es menor se crea una rama
            RamasIzq(i)

        elif rama < i:
            RamasDer(i)

        else:               #si no se crea otra rama
            print("---------------------------Se Saltea------------------------------ \n")



def Hoja():
    print()

ArbolBi()

print([raiz])
print(ramaIzquierda)
print(ramaDerecha)

print("Fin")