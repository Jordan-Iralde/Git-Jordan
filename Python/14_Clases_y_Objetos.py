class Auto:     #Por convencion la primera letra es en mayuscula
    ''' Documentacion de la funcion de la clase '''

    ruedas = 4
    color = 'rojo'
    
    def __init__(self, velocidad, aceleracion):
        self.aceleracion = aceleracion
        self.velocidad = velocidad

            
    def Aceleracion(self):
        velocidad = self.velocidad + self.aceleracion
        return  velocidad

    def frenar(self):
        v = self.velocidad - self.aceleracion
        if v - self.aceleracion < 0:
            v = 0
        self.velocidad = v
        return v

obj1 = Auto(10, 50)
print(f"La cantidad de Ruedas es: {obj1.ruedas}")
print(f"El color del auto es: {obj1.color}")
print("La veocidad es: ", obj1.velocidad)
print("La velocidad del auto es ", obj1.Aceleracion())
print("El auto freno, la velocidad es: ", obj1.frenar())

obj2 = Auto(20, 30)
print(f"La cantidad de Ruedas es: {obj2.ruedas}")
print(f"El color del auto es: {obj2.color}")
print("La veocidad es: ", obj2.velocidad)
print("La velocidad del auto es ", obj2.Aceleracion())
print("El auto freno, la velocidad es: ", obj2.frenar())

def res():
    diferenciaAceleracion = obj1.Aceleracion() - obj2.Aceleracion()
    print("la diferencia de acelaracion es :", diferenciaAceleracion)

def usuario():
    opciones = int(input("si quiere crear un objeto auto elija 1 y sino elija 2"))
    if opciones == 1:
        vel = int(input("ingrese la velovidad: "))
        acel = int(input("ingrese la aceleracion: "))
        obj3 = Auto(vel,acel)
        print (obj3.frenar())
        print (obj3.Aceleracion())
    if opciones == 2:
        print("fin")
        
res()
usuario()
