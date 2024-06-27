print("inicio")

a= int(input("Ingrese el primer numero: "))
b= int(input("Ingrese el segundo numero: "))
print(a)
#def crea una funcion/define una funcion, no puede ser una palabra reservada como if, for o while
def menu():
    opcion = int(input("Ingrese 1 para sumar, 2 para restar, 3 para salir"))
    if opcion == 1:
        print(suma())
    elif opcion == 2:
        print(resta())
    else:
        exit()

def suma():
        #a=12   #12+5, es una mala practica, si en una funcion no hay una variable definida, defiir una variable
    """
        a=15 
        c=10
        
            #si no esta definida la busca fuera de la funcion, ejemplo=b
        
        print(f'''
        Suma a+b+c
        {a+b+c}
        ''')

        #return print(f"c vale: {c}")
    """
    
    return (a+b)

def resta():
    return (a-b)

menu()
#suma()     #si no se llama a la funcion no va a hacer nada, solo se va a mostrar inicio y fin
#resta()

#print(a)

    #print(c)

#print(suma())#aca vuelve c (return)
#print(resta())
    #print(a)
"""
    Resolver los numeros, hacer para salir
"""

#Buena Practica
#las funciones print pantalla deberian ir al inicio del programa, separar por secciones
#Seccion de funciones que aparecen en pantalla
#Seccion de funciones que son condiciones

print("fin")