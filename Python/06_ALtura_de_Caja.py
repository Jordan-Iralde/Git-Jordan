print("inicio")     #   (largo - 2 * h) * (ancho - 2 * h)
listaVolumen = []
h = 0
i = 0
while True:
    try:
        largo = int(input("largo de la caja "))
        ancho = int(input("ancho de la caja "))
        while True:
            print(f"calculo numero {i+1} \n")
            h = h+1
            print(f"el valor de h es {h}")
            largo2h = largo - 2 * h
            ancho2h = ancho - 2 * h
            volumen = largo2h * ancho2h
            listaVolumen.append(volumen)
            print(f"largo2h= {largo} - 2 * {h} = {largo2h}")
            print(f"ancho2h= {ancho} - 2 * {h} = {ancho2h}")
            print(f"volumen= {largo2h} * {ancho2h} = {volumen}")
            print("_______________________________\n")
            if largo2h and ancho2h < 1:
                print("$$$valores inferiores a 1$$$")
                break
        print(listaVolumen)
        print(f"El valor maximo es= {max(listaVolumen)}")
        break
    except ValueError:
        print("error")
print("fin")