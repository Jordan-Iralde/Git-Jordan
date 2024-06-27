print("inicio")

a1 = int(input("altura1 "))
b1 = int(input("base1 "))
r1 = a1*b1


a2 = int(input("altura2 "))
b2 = int(input("base2 "))
r2 = a2*b2


a3 = int(input("altura1 "))
b3 = int(input("base2 "))
r3 = a3*b3


"""
Para Clasificar el mayor
"""

if r1>r2:
    if r1>r3:
        print("Rectangulo 1 es mayor que ambos")
if r2>r1:
    if r2>r3:
        print("Rectangulo 2 es mayor que ambos")
if r3>r1:
    if r3>r2:
        print("Rectangulo 3 es mayor que ambos")



"""
Para Clasificar los iguales
"""

if r1 == r2:
    if r1 == r3:
        print("todos son iguales")
if r2 == r3:
        print("Rectangulo 2 y Rectangulo 3 son iguales")
if r3 == r1:
    print("Rectangulo 1 y Rectangulo 3 son iguales")



"""
Para Clasificar el menor
"""

if r1<r2:
    if r1<r3:
        print("Rectangulo 1 es menor que ambos")
if r2<r1:
    if r2<r3:
        print("Rectangulo 2 es menor que ambos")
if r3<r1:
    if r3<r2:
        print("Rectangulo 3 es menor que ambos")

print("final")