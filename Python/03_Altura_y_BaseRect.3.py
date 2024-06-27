print("inicio")

listarea = []   #aca se van a guardar los valores

while True:
    try:
        cantidad = int(input("cuantos rectangulos quiere comparar: " )) #iteraciones del for
        for i in range (cantidad):
            base=int(input(f"ingrese la base de su rectangulo {i+1}: "))
            altura=int(input(f"ingrese la altura de su rectangulo {i+1}: "))
            area= base*altura
            listarea.append(area)   #Se guardan los valores en la lista

        print(listarea)
        
        salir=int(input("ingrese 0 para salir o 1 para volver a comparar"))
        if salir==0:
            break
        elif salir==1:
            print("reiniciando")
    except ValueError:
        print("lo siento el valor ingreso es incorrecto, por favor ingresa un numero entero")


print("fin")