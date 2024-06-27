'''
Actividad de programación orientada a objetos de a dos
Desarrollar un código que contenga dos clases con sus atributos y métodos. 
Luego crear las instancias y simular una interacción entre objetos de diferentes clases.
Pueden ampliar o agregar funcionalidades a dichas clases

NO se pueden calculos entre datos y metodos

1- Responsabilidad única.              S
2- Abierto/Cerrado                     O
3- Sustitución de Liskov.              L
4- Segregación de interfaz.            I
5-  Inversión de dependencia.          D

DRY
WET
YAGNI (You aren't gonna need it)
KISS
'''
print("inicio")

#---------------------------------------------------PERSONAJES------------------------------------------------------
class Personaje:
    ''' 
        Esta clase va a ser la maqueta de los personajes, los personajes cuentan con:
        Vida, Armadura y Fuerza
                                    Los personajes pueden:
        Atacar
        Defender
        Comer
    '''

    vida = 100   #Vida Default
    velocidad = 5   #Variable de la clase
    fuerza = 20

    
    def __init__(self, armadura, nombre, encapsuladoPoder) -> None:
        self.armadura = armadura
        self.nombre = nombre                           
        self.__encapsuladoPoder = encapsuladoPoder
        
    def Defender(self):
        self.defensa = self.vida + self.armadura
        return print("Los puntos de defensa son: ", self.defensa)   
    
    def PuntosAtaque(self):
        Daño = self.fuerza * self.velocidad
        print(Daño)
        return Daño

    def Comer(self):
        self.vida = 100
        return print("Se restauro la vida , vida es: ", self.vida)
    
PersonajeJugador = Personaje(50, 'Jordan', 50)    


PersonajeJugador.__encapsuladoPoder()
print(PersonajeJugador.__encapsuladoPoder)
#---------------------------------------------------------Auto---------------------------------------------------------

class Auto():     #Por convencion la primera letra es en mayuscula
    ''' Documentacion de la funcion de la clase '''

    vida = 500
    ruedas = 4
    color = 'rojo'
    velocidad = 0
    
    def __init__(self, color, aceleracion, nombre) -> None:
        self.color = color
        self.nombre = nombre
        self.aceleracion = aceleracion

    def Subirse(self):
        return print("---------------Estas en el auto---------------")
        
    def Bajarse(self):
        return print("---------------Bajaste del auto---------------")
        
    def Acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion
        return print("El auto acelero, la velocidad es", self.velocidad)

    def Frenar(self):
        v = self.velocidad 
        if v > 0:
            v -= self.aceleracion
            print(v)
        self.velocidad = v
        return print("freno, la velocidad es ",v)

#--------------------------------------------------FUNCIONES----------------------------------------------------


AutoDeJugador = Auto('rojo', 50, 'Auto del Jugador')

def AccionesDeJugador():
    MenuOpciones = ('''
            Acciones Del Jugador
    1-  Acciones del auto
    2-  Defenderse
    3-  Atacar
    4-  Comer
    ''')
    return print(MenuOpciones)

def AccionesDeJugadorParaAuto():
    MenuAuto = ('''
            Acciones Para El Auto
    1-  Subirse
    2-  No hacer nada
    3-  Pegarle
    ''')
    MenuEnAuto = '''
    1-  Bajar
    2-  Acelerar
    3-  Frenar
    '''
    while True:
        try:
            print(MenuAuto)
            Eleccion = int(input("Ingrese acciones en el auto: "))
            if Eleccion == 1:           #1 Si se sube
                AutoDeJugador.Subirse()
                print("la velocidad es: ", AutoDeJugador.velocidad)
                print(MenuEnAuto)
                EleccionEnAuto = int(input("Ingrese acciones en el auto: "))

                if EleccionEnAuto == 1 and AutoDeJugador.velocidad == 0:        #Si la velocidad es cero, se baja
                    AutoDeJugador.Bajarse()     #6 GRADOS DE IDENTACION, MALA PRACTICA
                    break

                elif EleccionEnAuto == 2:                                       #Acelerar
                    AutoDeJugador.Acelerar()

                elif EleccionEnAuto == 3:                                       #Frenars
                    AutoDeJugador.Frenar()

                else:
                    print("No hizo nada")
            elif Eleccion == 2:         #Si no se sube, no hace nada y vuelve al menu
                print("No esta pasando nada")
                break

            elif Eleccion == 3:         #3 Le esta pegando al auto
                SistemaDeAtaque()
            else:
                print(f"{MenuAuto},Elija una de las opciones")
        except ValueError:
            print("dato no valido")



#--------------------------------------------------------------------------------------------------------------
while True:
    AccionesDeJugador()
    Eleccion = int(input("Eleccion "))
    if Eleccion == 1:
        AccionesDeJugadorParaAuto()

    elif Eleccion == 2:
        PersonajeJugador.Defender()
        print("te defendiste de algo")

    elif Eleccion == 3:
        SistemaDeAtaque()
        print("Atacaste")

    elif Eleccion == 4:
        PersonajeJugador.Comer()

    else:
        break

print("fin")