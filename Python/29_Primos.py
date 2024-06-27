print("Inicio")

numeroPrimo = int(input("Ingrese el numero para comprobar"))

'''
for i in range(numeroPrimo):
    i = i + 1
    print("El ciclo de iteracion es, ", i)
    if numeroPrimo % i:
        print("No se divide por ", i)
    elif numeroPrimo % i == 0:
        print("Es")
    else:
        print("Se divide por ", i)
'''
x = 1
i = 1
for x in range(numeroPrimo):
    x = x + 1
    print("x es igual a ", x)
    print("i es ", i)
    print(f"{numeroPrimo} % {i} = ", numeroPrimoxi)
    if numeroPrimo % x == 0:
        i += 1
        print(f"{numeroPrimo} % {i} = ", numeroPrimo%i)

if i == 2:
    print("es")
else:
    print("no es")

print("Fin")