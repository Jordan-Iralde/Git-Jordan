print("inicio")     #   (largo - 2 * h) * (ancho - 2 * h)

ValoresEncontrados = []

while True:
    iteraciones = int(input("Ingrese la cantidad de iteraciones: "))
    largo = int(input("Ingrese el valor de largo: "))
    ancho = int(input("Ingrese el valor de ancho: "))
    h = 0
    
    for i in range(iteraciones):
        h = h + 1
        volumen = (largo - h) * (ancho - h) * h
        ValoresEncontrados.append(volumen)
        if volumen <= 0:
            print("No")
            break
    
    break
print(ValoresEncontrados)
print("El valor maximo que se encontro fue: ", max(ValoresEncontrados))
print("fin")