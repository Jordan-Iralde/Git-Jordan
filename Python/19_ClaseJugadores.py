class personas():

    def __init__(self,nombre,edad,altura) -> None:
        self.nombre =nombre
        self.edad   =edad
        self.altura =altura

    def hablar(self):
        mensaje = input("Mensaje: ")
        return(mensaje)

persona1 = personas('Jordan', 15, 150)
persona2 = personas('Maxi', 15, 260)

while True:
    print("Persona 1")
    persona1.hablar()
    print()
    print("Persona 2")
    persona2.hablar()
    print("------------------------")