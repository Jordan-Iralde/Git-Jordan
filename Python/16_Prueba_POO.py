class Rectangulo():
    #Perimetro es la suma de todos los lados
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho              #!  self.anch0

    def calcular_area(self):
        area = self.ancho * self.longitud
        return area                     #!  return area (identacion)
    
    def calcular_perimetro(self):       #! def calcular_perimetro(self): (:)
        perimetro = (self.ancho + self.longitud) * 2
        return perimetro
    
MiRectangulo = Rectangulo(4,5)          #Crear un segundo objeto (Mi2doRectangulo = Rectangulo(3,5))
Mi2doRectangulo = Rectangulo(3,5)       #!  Mi2doRectangulo = Rectangulo(3;5))

print(f"EL area es: {MiRectangulo.calcular_area()}")    #Utilizar f
print("El area es: ", MiRectangulo.calcular_area())
print("El perimetro es: ", MiRectangulo.calcular_perimetro())
