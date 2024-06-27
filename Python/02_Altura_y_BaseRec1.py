print("inicio del programa")
a1= float(input("elija una medida para la base de su primer rectangulo "))
b1= float(input("elija una medida para la altura de su primer rectangulo"))

a2= float(input("elija una medida para la base de su segundo rectangulo "))
b2= float(input("elija una medida para la altura de su segundo rectangulo"))

a3= float(input("elija una medida para la base de su tercer rectangulo "))
b3= float(input("elija una medida para la altura de su tercer rectangulo"))
r1= a1*b1
r2= a2*b2
r3= a3*b3   #Primeros programas, se puede hacer con un while
if r1>r2:
    if r1>r3:
        print("Rectangulo 1 es mayor que los demas")
if r2>r1:
    if r2>r3:
        print("Rectangulo 2 es mayor que los demas")
if r3>r1:
    if r3>r2:
        print("Rectangulo 3 es mayor que los demas")
        
if r1<r2:
    if r1<r3:
        print("Rectangulo 1 es menor que lso demas")
if r2<r1:
    if r2<r3:
        print("Rectangulo 2 es menor que los demas")
if r3<r1:
    if r3<r2:
        print("Rectangulo 3 es menor que los demas")
        
if r1 == r2 == r3:
    print("los 3 rectangulos son iguales")
elif r1 == r2:
    print (" los primeros dos rectangulos son iguales")
elif r1 == r3:
    print(" el primer y tercer rectangulo son iguales")
elif r2 == r3:
    print(" el segundo y tercer rectangulo son iguales")
print("fin")